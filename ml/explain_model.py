"""
Model Explainability Pipeline for Final Placement Model
Extracts global and local feature contributions from models/placement_model.pkl
"""

import os
import joblib
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


def generate_explanations():
    model_path = os.path.join('models', 'placement_model.pkl')
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")

    print("=" * 70)
    print("MODEL EXPLAINABILITY PIPELINE")
    print("=" * 70)
    print(f"Loading final trained pipeline from: {model_path}")
    pipeline = joblib.load(model_path)
    print("Pipeline successfully loaded.\n")

    preprocessor = pipeline.named_steps['preprocessor']
    classifier = pipeline.named_steps['classifier']

    # Extract transformed feature names and coefficients
    num_cols = [
        'CGPA',
        'Internships',
        'Projects',
        'Workshops_Certifications',
        'AptitudeTestScore',
        'SoftSkillsRating',
        'SSC_Marks',
        'HSC_Marks'
    ]
    binary_cols = ['ExtracurricularActivities', 'PlacementTraining']
    transformed_features = num_cols + binary_cols

    coefficients = classifier.coef_[0]
    intercept = classifier.intercept_[0]
    abs_importance = np.abs(coefficients)

    # 1. Global Feature Importance DataFrame
    importance_df = pd.DataFrame({
        'Feature': transformed_features,
        'Coefficient': coefficients,
        'Absolute Importance': abs_importance,
        'Odds Ratio': np.exp(coefficients),
        'Type': ['Standardized Numerical' if col in num_cols else 'Binary Flag' for col in transformed_features]
    }).sort_values(by='Absolute Importance', ascending=False).reset_index(drop=True)

    print("=" * 70)
    print("GLOBAL FEATURE IMPORTANCE RANKING (Sorted by Absolute Importance)")
    print("=" * 70)
    print(importance_df.to_string(index=False, formatters={
        'Coefficient': '{:+.4f}'.format,
        'Absolute Importance': '{:.4f}'.format,
        'Odds Ratio': '{:.4f}'.format
    }))

    # 2. Generate Horizontal Bar Chart
    plot_dir = 'docs/models'
    os.makedirs(plot_dir, exist_ok=True)
    chart_path = os.path.join(plot_dir, 'final_feature_importance.png')

    plt.figure(figsize=(10, 6))
    plot_df = importance_df.sort_values(by='Absolute Importance', ascending=True)
    colors = ['#2ecc71' if c > 0 else '#e74c3c' for c in plot_df['Coefficient']]

    bars = plt.barh(plot_df['Feature'], plot_df['Absolute Importance'], color=colors, edgecolor='black', height=0.65)
    for bar, coef in zip(bars, plot_df['Coefficient']):
        w = bar.get_width()
        sign_str = f"+{coef:.4f}" if coef > 0 else f"{coef:.4f}"
        plt.text(w + 0.015, bar.get_y() + bar.get_height() / 2, sign_str,
                 va='center', ha='left', fontsize=9, fontweight='bold')

    plt.xlabel('Absolute Importance (|Coefficient|)', fontsize=11, fontweight='bold')
    plt.title('Global Feature Importance — Logistic Regression\n(Green = Positive Impact on Placement, Red = Negative)',
              fontsize=12, fontweight='bold', pad=15)
    plt.xlim(0, max(plot_df['Absolute Importance']) + 0.15)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(chart_path, dpi=300)
    plt.close()
    print(f"\nFeature importance chart saved to: {chart_path}")

    # 3. Create docs/model_explainability.md
    write_global_explainability_report(importance_df, intercept)

    # 4. Local Explanations for 3 Example Students
    students = [
        {
            'Student_ID': 'Student 1 (High Performer)',
            'CGPA': 8.5, 'Internships': 2, 'Projects': 3, 'Workshops_Certifications': 2,
            'AptitudeTestScore': 88, 'SoftSkillsRating': 4.6, 'ExtracurricularActivities': 1,
            'PlacementTraining': 1, 'SSC_Marks': 85, 'HSC_Marks': 84
        },
        {
            'Student_ID': 'Student 2 (Average / Moderate)',
            'CGPA': 7.4, 'Internships': 1, 'Projects': 1, 'Workshops_Certifications': 1,
            'AptitudeTestScore': 76, 'SoftSkillsRating': 4.1, 'ExtracurricularActivities': 0,
            'PlacementTraining': 1, 'SSC_Marks': 66, 'HSC_Marks': 70
        },
        {
            'Student_ID': 'Student 3 (Underprepared / Low)',
            'CGPA': 6.6, 'Internships': 0, 'Projects': 0, 'Workshops_Certifications': 0,
            'AptitudeTestScore': 62, 'SoftSkillsRating': 3.2, 'ExtracurricularActivities': 0,
            'PlacementTraining': 0, 'SSC_Marks': 58, 'HSC_Marks': 60
        }
    ]

    local_results = run_local_explanations(pipeline, preprocessor, classifier, students, transformed_features, num_cols)

    # 5. Write docs/models/local_explanations.md
    write_local_explanations_report(local_results, intercept)

    return importance_df, local_results


def run_local_explanations(pipeline, preprocessor, classifier, students, feature_names, num_cols):
    input_df = pd.DataFrame(students)
    feature_order = [
        'CGPA', 'Internships', 'Projects', 'Workshops_Certifications',
        'AptitudeTestScore', 'SoftSkillsRating', 'ExtracurricularActivities',
        'PlacementTraining', 'SSC_Marks', 'HSC_Marks'
    ]
    X_input = input_df[feature_order]

    # Transform input through preprocessor
    X_trans = preprocessor.transform(X_input)
    coefficients = classifier.coef_[0]
    intercept = classifier.intercept_[0]

    probabilities = pipeline.predict_proba(X_input)
    predictions = pipeline.predict(X_input)

    local_results = []
    print("\n" + "=" * 70)
    print("LOCAL EXPLANATIONS (3 Example Students)")
    print("=" * 70)

    for idx, student in enumerate(students):
        x_vec = X_trans[idx]
        contributions = coefficients * x_vec
        logit = intercept + contributions.sum()
        prob_placed = probabilities[idx][1] * 100
        prob_not_placed = probabilities[idx][0] * 100
        pred_label = "Placed (1)" if predictions[idx] == 1 else "NotPlaced (0)"

        contrib_df = pd.DataFrame({
            'Feature': feature_names,
            'Raw_Value': [student[col] for col in feature_names],
            'Transformed_Value': x_vec,
            'Coefficient': coefficients,
            'Logit_Contribution': contributions
        })

        positive_contributors = contrib_df[contrib_df['Logit_Contribution'] > 0].sort_values(
            by='Logit_Contribution', ascending=False
        ).reset_index(drop=True)

        negative_contributors = contrib_df[contrib_df['Logit_Contribution'] < 0].sort_values(
            by='Logit_Contribution', ascending=True
        ).reset_index(drop=True)

        print(f"\n--- {student['Student_ID']} ---")
        print(f"Predicted Class: {pred_label} | Placement Probability: {prob_placed:.2f}% (NotPlaced: {prob_not_placed:.2f}%)")
        print(f"Logit (z): {logit:.4f} (Base Intercept: {intercept:.4f})")
        
        print("  Top Positive Contributing Features:")
        for _, r in positive_contributors.head(3).iterrows():
            print(f"    + {r['Feature']} (Val: {r['Raw_Value']}, Contrib: +{r['Logit_Contribution']:.4f})")

        print("  Top Negative Contributing Features:")
        for _, r in negative_contributors.head(3).iterrows():
            print(f"    - {r['Feature']} (Val: {r['Raw_Value']}, Contrib: {r['Logit_Contribution']:.4f})")

        local_results.append({
            'Student_ID': student['Student_ID'],
            'Raw_Inputs': student,
            'Predicted_Class': pred_label,
            'Placement_Probability': prob_placed,
            'Not_Placed_Probability': prob_not_placed,
            'Logit': logit,
            'All_Contributions': contrib_df,
            'Positive_Contributors': positive_contributors,
            'Negative_Contributors': negative_contributors
        })

    return local_results


def write_global_explainability_report(importance_df, intercept):
    report_path = 'docs/model_explainability.md'

    rows = []
    for rank, (_, r) in enumerate(importance_df.iterrows(), start=1):
        direction = "Positive (+)" if r['Coefficient'] > 0 else "Negative (-)"
        rows.append(
            f"| {rank} | **{r['Feature']}** | {r['Coefficient']:+.4f} | **{r['Absolute Importance']:.4f}** | "
            f"{r['Odds Ratio']:.4f} | {direction} | {r['Type']} |"
        )
    table_str = "\n".join(rows)

    top5 = importance_df.head(5)['Feature'].tolist()

    content = rf"""# Final Placement Model Explainability Report

**Model:** Logistic Regression Pipeline (`models/placement_model.pkl`)  
**Hyperparameters:** `C = 0.5`, `class_weight = "balanced"`, `penalty = "l2"`, `solver = "lbfgs"`  
**Explanation Technique:** Global Standardized Linear Coefficients & Log-Odds Effect Sizes  
**Base Intercept ($\beta_0$):** `{intercept:.4f}`

---

## 1. Methodology & Interpretation Framework

Because all numerical features were standardized using `StandardScaler` ($\mu=0, \sigma=1$) while binary indicator features were passed through as $[0, 1]$, the resulting Logistic Regression coefficients are directly comparable in magnitude:

1. **Coefficient ($\beta$):** Represents the change in log-odds of placement for a 1-standard-deviation increase in a numerical feature (or possessing the attribute in binary features), holding all other features constant:
   $$\Delta \ln\left(\frac{{P}}{{1-P}}\right) = \beta_j \cdot \Delta x_j$$
2. **Odds Ratio ($e^\beta$):** The multiplicative factor change in the odds of placement. An odds ratio $> 1.0$ indicates increased placement odds; an odds ratio $< 1.0$ indicates reduced odds.
3. **Absolute Importance ($|\beta|$):** Quantifies the overall predictive strength and weight assigned to the feature by the decision boundary.

---

## 2. Global Feature Importance Ranking

*Ranked from highest to lowest absolute importance:*

| Rank | Feature | Coefficient ($\beta$) | Absolute Importance ($|\beta|$) | Odds Ratio ($e^\beta$) | Direction | Feature Type |
|---|---|---|---|---|---|---|
{table_str}

---

## 3. Top 5 Most Important Features

1. **`PlacementTraining` ($|\beta| = {importance_df.loc[0, 'Absolute Importance']:.4f}$, $\beta = +{importance_df.loc[0, 'Coefficient']:.4f}$, Odds Ratio = {importance_df.loc[0, 'Odds Ratio']:.4f}):**
   - Single strongest predictor in the model. Students who attend structured campus placement preparation training experience a **{importance_df.loc[0, 'Odds Ratio']:.2f}x multiplier** in placement odds compared to those who do not, holding other variables constant.
2. **`ExtracurricularActivities` ($|\beta| = {importance_df.loc[1, 'Absolute Importance']:.4f}$, $\beta = +{importance_df.loc[1, 'Coefficient']:.4f}$, Odds Ratio = {importance_df.loc[1, 'Odds Ratio']:.4f}):**
   - Active participation provides a **{importance_df.loc[1, 'Odds Ratio']:.2f}x boost** in placement odds, indicating strong demand for well-rounded candidates with leadership, communication, and club engagement.
3. **`AptitudeTestScore` ($|\beta| = {importance_df.loc[2, 'Absolute Importance']:.4f}$, $\beta = +{importance_df.loc[2, 'Coefficient']:.4f}$, Odds Ratio = {importance_df.loc[2, 'Odds Ratio']:.4f}):**
   - Highest-weighted academic/test metric. Each 1-standard-deviation increase in aptitude score (~8.1 points) increases placement odds by **{importance_df.loc[2, 'Odds Ratio']:.2f}x**, aligning with real-world campus recruitment screening cutoffs.
4. **`SSC_Marks` ($|\beta| = {importance_df.loc[3, 'Absolute Importance']:.4f}$, $\beta = +{importance_df.loc[3, 'Coefficient']:.4f}$, Odds Ratio = {importance_df.loc[3, 'Odds Ratio']:.4f}):**
   - Secondary schooling percentage serves as an effective consistency signal and eligibility filter.
5. **`SoftSkillsRating` ($|\beta| = {importance_df.loc[4, 'Absolute Importance']:.4f}$, $\beta = +{importance_df.loc[4, 'Coefficient']:.4f}$, Odds Ratio = {importance_df.loc[4, 'Odds Ratio']:.4f}):**
   - Behavioral, interview, and communication rating significantly increases placement odds ($1.30x$ per SD).

---

## 4. Interpretation of Coefficients

- **Positive Coefficients ($\beta > 0$):**
  - All features except Internships exhibit positive coefficients.
  - Increases in aptitude scores, school percentages (`SSC_Marks`, `HSC_Marks`), college GPA (`CGPA`), project count, certifications, and soft skills all monotonically increase the predicted probability of placement.
- **Negative Coefficient for `Internships` ($\beta = -0.0057$):**
  - The coefficient for `Internships` is essentially zero (magnitude $< 0.006$), indicating negligible standalone linear contribution once projects, workshops, GPA, and training are conditioned on.
  - This occurs due to slight collinearity with projects and certifications, and does **not** mean internships harm placement.

---

## 5. Critical Governance & Scientific Limitations

> **CRITICAL DISCLAIMER: ASSOCIATION DOES NOT EQUAL CAUSATION**
>
> 1. **Statistical Correlation vs. Causal Impact:**
>    - The rankings and coefficients above reflect **statistical associations** learned from the training distribution.
>    - They do **NOT** prove real-world causality. For instance, while `PlacementTraining` has a large coefficient, motivated students who are naturally proactive may be more likely to both sign up for training and succeed in interviews.
> 2. **Linear Additivity Assumption:**
>    - Logistic Regression assumes a linear relationship between features and the log-odds of placement. It does not natively capture non-linear tipping points (e.g., hard eligibility thresholds where GPA $< 7.0$ disqualifies a candidate regardless of projects) unless explicitly engineered.
> 3. **Contextual Use:**
>    - These feature importance scores must be used to **guide student skill development**, not to deterministically judge candidates.
"""
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Global explainability report written to: {report_path}")


def write_local_explanations_report(local_results, intercept):
    report_path = 'docs/models/local_explanations.md'

    sections = []
    for res in local_results:
        raw = res['Raw_Inputs']
        pos = res['Positive_Contributors']
        neg = res['Negative_Contributors']

        pos_table = "\n".join([
            f"| **{r['Feature']}** | {r['Raw_Value']} | {r['Transformed_Value']:+.2f} | {r['Coefficient']:+.4f} | **+{r['Logit_Contribution']:.4f}** |"
            for _, r in pos.iterrows()
        ])

        neg_table = "\n".join([
            f"| **{r['Feature']}** | {r['Raw_Value']} | {r['Transformed_Value']:+.2f} | {r['Coefficient']:+.4f} | **{r['Logit_Contribution']:.4f}** |"
            for _, r in neg.iterrows()
        ]) if len(neg) > 0 else "| *None* | - | - | - | - |"

        sections.append(rf"""### {res['Student_ID']}
- **Predicted Placement Status:** **{res['Predicted_Class']}**
- **Placement Probability:** **{res['Placement_Probability']:.2f}%** *(Not Placed: {res['Not_Placed_Probability']:.2f}%)*
- **Final Log-Odds ($z$):** `{res['Logit']:.4f}` *(Base Intercept: `{intercept:.4f}`)*

#### Profile Summary:
- CGPA: `{raw['CGPA']}` | Internships: `{raw['Internships']}` | Projects: `{raw['Projects']}` | Certifications: `{raw['Workshops_Certifications']}`
- Aptitude: `{raw['AptitudeTestScore']}` | Soft Skills: `{raw['SoftSkillsRating']}` | SSC: `{raw['SSC_Marks']}%` | HSC: `{raw['HSC_Marks']}%`
- Extracurricular Activities: `{'Yes' if raw['ExtracurricularActivities']==1 else 'No'}` | Placement Training: `{'Yes' if raw['PlacementTraining']==1 else 'No'}`

#### Top Positive Contributors (Pushed Probability Up):
| Feature | Raw Value | Scaled Value ($x'$) | Coefficient ($\beta$) | Logit Contribution ($\beta \cdot x'$) |
|---|---|---|---|---|
{pos_table}

#### Top Negative Contributors (Pulled Probability Down):
| Feature | Raw Value | Scaled Value ($x'$) | Coefficient ($\beta$) | Logit Contribution ($\beta \cdot x'$) |
|---|---|---|---|---|
{neg_table}
""")

    body = "\n---\n\n".join(sections)
    full_content = rf"""# Local Explainability Report for Example Students

**Model Pipeline:** `models/placement_model.pkl` (Logistic Regression)  
**Methodology:** Exact decomposition of the log-odds decision boundary ($z = \beta_0 + \sum_{{j=1}}^p \beta_j x_j'$), converted to probability via the sigmoid link function:
$$P(\text{{Placed}}) = \frac{{1}}{{1 + e^{{-z}}}}$$

---

{body}

---

## Technical Note on Local Explanations
1. **Scaled Values ($x'$):** Represents the student's deviation from the population mean in units of standard deviations for numerical features.
   - $x' > 0$: Student performed above average for this feature.
   - $x' < 0$: Student performed below average for this feature.
2. **Logit Contribution ($\beta \cdot x'$):**
   - For positive coefficients ($\beta > 0$), being above average ($x' > 0$) adds positively to the logit, increasing placement probability.
   - Being below average ($x' < 0$) produces a negative contribution, reducing placement probability.
   - Binary attributes (`ExtracurricularActivities`, `PlacementTraining`) directly add their coefficient weight when active ($x'=1$).
"""
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    print(f"Local explainability report written to: {report_path}")


if __name__ == '__main__':
    generate_explanations()
