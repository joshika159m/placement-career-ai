# Placement Probability & System Architecture Documentation

## 1. Architectural Overview & System Distinction

The **Placement Prediction and Career Recommendation System** is structured around three distinct, mathematically rigorous analytical pillars:

1. **Machine Learning Placement Prediction Model (Research Benchmark)**
2. **Weighted Student-Facing Placement Probability Model (Interactive Assessment)**
3. **Transparent Rule-Based Career Recommendation Engine (Role Compatibility)**

---

## 2. Institutional Viva Explanation

> **Official Project Viva Statement:**
> 
> *"The project contains a trained machine-learning placement prediction model based on historical recruitment data. For the final interactive student assessment, we use a separate weighted placement probability formula because the live aptitude and technical assessments are current student-performance signals and were not present in the historical ML training dataset. The final student-facing estimate gives 70% weight to live aptitude and technical performance and 30% to SSC and HSC performance."*

---

## 3. Detailed Component Breakdown

### Component 1: Machine Learning Placement Model (Research Benchmark)
- **Purpose:** Historical predictive modeling and baseline machine-learning analysis.
- **Data Source:** Cleaned benchmark campus recruitment records (`campus_recruitment_clean.csv`, $N=9,928$).
- **Algorithm:** Calibrated Logistic Regression (Linear Log-Odds Classifier).
- **Features Evaluated:**
  - Original 10-Feature Pipeline: `CGPA`, `Internships`, `Projects`, `Workshops/Certifications`, `AptitudeTestScore`, `SoftSkillsRating`, `ExtracurricularActivities`, `PlacementTraining`, `SSC_Marks`, `HSC_Marks`.
  - Reduced 5-Feature Pipeline: `CGPA`, `AptitudeTestScore`, `SoftSkillsRating`, `SSC_Marks`, `HSC_Marks`.
- **Role in System:** Preserved in the repository (`models/placement_model.pkl` and `models/placement_model_reduced.pkl`) for empirical comparison, ML methodology documentation, and academic explainability. It is **not** used to generate the final interactive 70/30 probability because real-time test performance was not a feature in the historical dataset.

---

### Component 2: Weighted Student-Facing Placement Probability Model
- **Terminology:** Deterministic **Weighted Placement Probability Model** (or **Weighted Placement Readiness Formula**).
- **Rationale:** A student's current hiring potential is primarily defined by demonstrated live problem-solving capability (Aptitude & Technical), anchored by foundational academic consistency (SSC & HSC).
- **Mathematical Formulation:**
  $$\text{Placement Probability} = 0.35 \times \text{Aptitude} + 0.35 \times \text{Technical} + 0.15 \times \text{SSC} + 0.15 \times \text{HSC}$$
- **Weight Distribution:**
  - **Live Assessment Contribution (70%):**
    - Live 15-Question Cognitive Aptitude Performance: **35%**
    - Live 15-Question Domain Technical Performance: **35%**
  - **Academic Indicators Contribution (30%):**
    - Secondary School Certificate (SSC / 10th Marks %): **15%**
    - Higher Secondary Certificate (HSC / 12th Marks %): **15%**
- **Excluded Features:**
  - `CGPA`, `Internships`, `Projects`, `Workshops`, `Extracurricular Activities`, and `Placement Training` do **not** alter this probability.
- **Output Bounds:** Strictly bounded within $[0.00\%, 100.00\%]$.
- **UI Policy:** Displays exact numerical percentage and performance breakdown. Strictly **no** binary labels (`PLACED` / `NOT PLACED`) or surrogate pass/fail classifications.

#### Verified Numerical Test Cases
| Test Case | Aptitude (%) | Technical (%) | SSC (%) | HSC (%) | Expected Placement Probability | Verified Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Case 1** | 95.0% | 95.0% | 60.0% | 60.0% | $0.35(95) + 0.35(95) + 0.15(60) + 0.15(60) = \mathbf{84.50\%}$ | **PASS** |
| **Case 2** | 40.0% | 40.0% | 95.0% | 95.0% | $0.35(40) + 0.35(40) + 0.15(95) + 0.15(95) = \mathbf{56.50\%}$ | **PASS** |
| **Case 3** | 80.0% | 70.0% | 85.0% | 90.0% | $0.35(80) + 0.35(70) + 0.15(85) + 0.15(90) = \mathbf{78.75\%}$ | **PASS** |
| **Case 4** | 100.0% | 100.0% | 100.0% | 100.0% | $0.35(100) + 0.35(100) + 0.15(100) + 0.15(100) = \mathbf{100.00\%}$ | **PASS** |
| **Case 5** | 0.0% | 0.0% | 0.0% | 0.0% | $0.35(0) + 0.35(0) + 0.15(0) + 0.15(0) = \mathbf{0.00\%}$ | **PASS** |

---

### Component 3: Career Recommendation Engine
- **Formula:**
  $$\text{Final Match Score} = 0.40 \cdot \text{Technical Match} + 0.20 \cdot \text{Aptitude Match} + 0.20 \cdot \text{Placement Probability} + 0.20 \cdot \text{Interest Match}$$
- **Weights:**
  - **Technical Match (40%):** Performance on role-relevant technical topics from the live assessment.
  - **Aptitude Match (20%):** 70% domain-relevant aptitude categories + 30% overall test score.
  - **Placement Probability (20%):** The 70/30 Weighted Placement Probability from Component 2.
  - **Interest Match (20%):** Proportional overlap with role interest definitions.
- **Top 3 Recommendations:** Ranks roles into confidence tiers (`Strong Match`, `Good Match`, `Moderate Match`, `Weak Match`).
