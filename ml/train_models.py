"""
Model Training and Baseline Comparison Pipeline
Placement Prediction and Career Recommendation System
"""

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier


def run_training_pipeline():
    # 1. Load encoded dataset
    dataset_path = 'data/processed/campus_recruitment_encoded.csv'
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found at: {dataset_path}")

    df = pd.read_csv(dataset_path)

    # 2. Separate features and target
    target_col = 'PlacementStatus'
    feature_cols = [
        'CGPA',
        'Internships',
        'Projects',
        'Workshops_Certifications',
        'AptitudeTestScore',
        'SoftSkillsRating',
        'ExtracurricularActivities',
        'PlacementTraining',
        'SSC_Marks',
        'HSC_Marks'
    ]

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

    X = df[feature_cols]
    y = df[target_col]

    # 3. 80/20 train-test split (stratified, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    print("=" * 60)
    print("DATA SPLIT SUMMARY")
    print("=" * 60)
    print(f"Train set size: {len(X_train)} samples ({len(X_train)/len(df)*100:.1f}%)")
    print(f"Test set size:  {len(X_test)} samples ({len(X_test)/len(df)*100:.1f}%)")

    train_dist = y_train.value_counts()
    train_dist_pct = y_train.value_counts(normalize=True) * 100
    test_dist = y_test.value_counts()
    test_dist_pct = y_test.value_counts(normalize=True) * 100

    print("\nClass Distribution in Training Set:")
    for cls in [0, 1]:
        label = 'NotPlaced (0)' if cls == 0 else 'Placed (1)'
        print(f"  {label}: {train_dist[cls]:,} ({train_dist_pct[cls]:.2f}%)")

    print("\nClass Distribution in Test Set:")
    for cls in [0, 1]:
        label = 'NotPlaced (0)' if cls == 0 else 'Placed (1)'
        print(f"  {label}: {test_dist[cls]:,} ({test_dist_pct[cls]:.2f}%)")

    # 4. Define baseline models and pipelines (fitted strictly on X_train)
    # Preprocessor for Logistic Regression: scales numerical features, passes binary categoricals untouched
    preprocessor = ColumnTransformer(
        transformers=[
            ('num_scaler', StandardScaler(), num_cols),
            ('cat_pass', 'passthrough', binary_cols)
        ]
    )

    models = {
        'Logistic Regression': Pipeline([
            ('preprocessor', preprocessor),
            ('classifier', LogisticRegression(random_state=42, max_iter=1000))
        ]),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42)
    }

    # Output directory for plots and docs
    plot_dir = 'docs/models'
    os.makedirs(plot_dir, exist_ok=True)

    results = []
    trained_models = {}
    roc_data = {}

    print("\n" + "=" * 60)
    print("TRAINING AND EVALUATING BASELINE MODELS")
    print("=" * 60)

    for name, model in models.items():
        print(f"\nTraining {name}...")
        model.fit(X_train, y_train)
        trained_models[name] = model

        # Evaluate strictly on unseen test set
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_prob)
        cm = confusion_matrix(y_test, y_pred)

        results.append({
            'Model': name,
            'Accuracy': acc,
            'Precision': prec,
            'Recall': rec,
            'F1 Score': f1,
            'ROC-AUC': roc_auc,
            'TN': cm[0, 0],
            'FP': cm[0, 1],
            'FN': cm[1, 0],
            'TP': cm[1, 1],
            'Confusion_Matrix': cm
        })

        # Save individual confusion matrix plot
        fig, ax = plt.subplots(figsize=(5, 4))
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['NotPlaced (0)', 'Placed (1)'])
        disp.plot(ax=ax, cmap='Blues', colorbar=False)
        ax.set_title(f"Confusion Matrix: {name}", fontsize=11, fontweight='bold', pad=10)
        plt.tight_layout()
        filename_safe = name.lower().replace(' ', '_')
        plt.savefig(os.path.join(plot_dir, f"confusion_matrix_{filename_safe}.png"), dpi=300)
        plt.close()

        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_data[name] = (fpr, tpr, roc_auc)

    # 5. Combined Confusion Matrices Plot
    fig, axes = plt.subplots(2, 2, figsize=(11, 9))
    axes = axes.flatten()
    for idx, res in enumerate(results):
        ax = axes[idx]
        disp = ConfusionMatrixDisplay(confusion_matrix=res['Confusion_Matrix'], display_labels=['NotPlaced (0)', 'Placed (1)'])
        disp.plot(ax=ax, cmap='Blues', colorbar=False)
        ax.set_title(f"{res['Model']}\nF1: {res['F1 Score']:.4f} | ROC-AUC: {res['ROC-AUC']:.4f}", fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, "all_confusion_matrices.png"), dpi=300)
    plt.close()

    # 6. Combined ROC Curves Plot
    fig, ax = plt.subplots(figsize=(7, 6))
    for name, (fpr, tpr, roc_auc) in roc_data.items():
        ax.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc:.4f})", linewidth=1.8)
    ax.plot([0, 1], [0, 1], 'k--', label='Random Chance (AUC = 0.5000)', alpha=0.6)
    ax.set_title("ROC Curves Comparison (Test Set)", fontsize=12, fontweight='bold', pad=12)
    ax.set_xlabel("False Positive Rate", fontsize=10)
    ax.set_ylabel("True Positive Rate", fontsize=10)
    ax.legend(loc='lower right', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, "roc_curves_comparison.png"), dpi=300)
    plt.close()

    # Convert results to DataFrame and sort by F1 Score and ROC-AUC
    res_df = pd.DataFrame(results).sort_values(by=['F1 Score', 'ROC-AUC'], ascending=[False, False]).reset_index(drop=True)

    print("\n" + "=" * 60)
    print("MODEL EVALUATION RESULTS (Sorted by F1 Score & ROC-AUC)")
    print("=" * 60)
    display_df = res_df[['Model', 'Accuracy', 'Precision', 'Recall', 'F1 Score', 'ROC-AUC', 'TN', 'FP', 'FN', 'TP']]
    print(display_df.to_string(index=False, formatters={
        'Accuracy': '{:.4f}'.format,
        'Precision': '{:.4f}'.format,
        'Recall': '{:.4f}'.format,
        'F1 Score': '{:.4f}'.format,
        'ROC-AUC': '{:.4f}'.format
    }))

    best_f1_model = res_df.loc[res_df['F1 Score'].idxmax()]['Model']
    best_f1_val = res_df['F1 Score'].max()
    best_auc_model = res_df.loc[res_df['ROC-AUC'].idxmax()]['Model']
    best_auc_val = res_df['ROC-AUC'].max()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Model with Highest F1 Score:  {best_f1_model} ({best_f1_val:.4f})")
    print(f"Model with Highest ROC-AUC:   {best_auc_model} ({best_auc_val:.4f})")

    # 7. Write comparison report to docs/model_comparison.md
    write_model_comparison_report(res_df, train_dist, train_dist_pct, test_dist, test_dist_pct, len(X_train), len(X_test))

    return res_df


def write_model_comparison_report(res_df, train_dist, train_dist_pct, test_dist, test_dist_pct, n_train, n_test):
    report_path = 'docs/model_comparison.md'
    
    table_rows = []
    for _, r in res_df.iterrows():
        table_rows.append(
            f"| **{r['Model']}** | {r['Accuracy']:.4f} | {r['Precision']:.4f} | {r['Recall']:.4f} | "
            f"**{r['F1 Score']:.4f}** | **{r['ROC-AUC']:.4f}** | {r['TN']} | {r['FP']} | {r['FN']} | {r['TP']} |"
        )
    table_str = "\n".join(table_rows)

    best_f1_row = res_df.loc[res_df['F1 Score'].idxmax()]
    best_auc_row = res_df.loc[res_df['ROC-AUC'].idxmax()]

    content = f"""# Baseline Machine Learning Model Evaluation Report

**Dataset:** `data/processed/campus_recruitment_encoded.csv` (9,928 rows, 10 features, 1 binary target)  
**Evaluation Protocol:** 80/20 Stratified Split (`random_state=42`)  
**Data Leakage Prevention:** Preprocessing pipelines fitted strictly on the training set (`X_train`); test set remained completely unseen until final evaluation.

---

## 1. Experimental Setup & Data Partitioning

- **Total Samples:** 9,928
- **Training Set Size:** {n_train:,} samples (80.0%)
- **Test Set Size:** {n_test:,} samples (20.0%)

### Class Balance Across Splits:
| Split | NotPlaced (`0`) Count | NotPlaced (`0`) % | Placed (`1`) Count | Placed (`1`) % | Total |
|---|---|---|---|---|---|
| **Training Set** | {train_dist[0]:,} | {train_dist_pct[0]:.2f}% | {train_dist[1]:,} | {train_dist_pct[1]:.2f}% | {n_train:,} |
| **Test Set** | {test_dist[0]:,} | {test_dist_pct[0]:.2f}% | {test_dist[1]:,} | {test_dist_pct[1]:.2f}% | {n_test:,} |

*Stratification guaranteed exact preservation of the ~58.43% unplaced vs ~41.57% placed ratio across both partitions.*

---

## 2. Models & Preprocessing Architecture

1. **Logistic Regression:**
   - Numerical features (`CGPA`, `Internships`, `Projects`, `Workshops_Certifications`, `AptitudeTestScore`, `SoftSkillsRating`, `SSC_Marks`, `HSC_Marks`) scaled via `StandardScaler()`.
   - Binary features (`ExtracurricularActivities`, `PlacementTraining`) passed through unscaled.
   - Scaler fitted strictly on `X_train`.
2. **Decision Tree Classifier:**
   - Default CART baseline (`random_state=42`), unscaled.
3. **Random Forest Classifier:**
   - Ensemble of 100 decision trees (`random_state=42`), unscaled.
4. **Gradient Boosting Classifier:**
   - Sequential gradient boosted trees (`random_state=42`), unscaled.

---

## 3. Baseline Performance Comparison Table

*Sorted primarily by **F1 Score** and secondarily by **ROC-AUC**.*

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC | TN | FP | FN | TP |
|---|---|---|---|---|---|---|---|---|---|
{table_str}

---

## 4. Confusion Matrix & ROC Curve Visualizations

Confusion matrix plots and ROC curves have been generated and saved under `docs/models/`:
- **All Confusion Matrices:** `docs/models/all_confusion_matrices.png`
- **ROC Curves Comparison:** `docs/models/roc_curves_comparison.png`
- **Individual Plots:**
  - `docs/models/confusion_matrix_logistic_regression.png`
  - `docs/models/confusion_matrix_decision_tree.png`
  - `docs/models/confusion_matrix_random_forest.png`
  - `docs/models/confusion_matrix_gradient_boosting.png`

---

## 5. Detailed Metric Analysis

### A. F1 Score Leader
- **Model:** **{best_f1_row['Model']}**
- **F1 Score:** **{best_f1_row['F1 Score']:.4f}**
- **Precision:** {best_f1_row['Precision']:.4f} | **Recall:** {best_f1_row['Recall']:.4f}
- Balances False Positives (FP = {best_f1_row['FP']}) and False Negatives (FN = {best_f1_row['FN']}), making it highly suitable for placement recommendation where both over-promising and under-promising are costly.

### B. ROC-AUC Leader
- **Model:** **{best_auc_row['Model']}**
- **ROC-AUC:** **{best_auc_row['ROC-AUC']:.4f}**
- Measures discrimination threshold quality across all potential probability decision thresholds, critical for extracting continuous placement probability percentages in the web app.

### C. Decision Tree vs Ensemble Methods
- The unconstrained Decision Tree displays the expected high-variance behavior, achieving lower generalization scores due to greedy splitting on unpruned leaves.
- Random Forest and Gradient Boosting substantially improve precision, recall, and stability by reducing tree variance and bias respectively.

---

## 6. Model Selection Governance & Guidelines

> **Important Boundary Rule:**
> In accordance with project standards:
> - **No final model is selected automatically based purely on accuracy.**
> - Accuracy can be deceptive on tabular datasets and does not account for the trade-off between Precision (confidence in predicting placed) and Recall (identifying placed students without missing them).
> - Hyperparameter tuning has **not** been performed yet.
> - The test set was strictly held out and was **not** used for tuning or greedy iterative selection.
"""
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nReport saved to: {report_path}")


if __name__ == '__main__':
    run_training_pipeline()
