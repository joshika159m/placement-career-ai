# Dataset Analysis Report: Campus Recruitment Dataset

## 1. Overview & Source
- **Dataset Name:** `Krooz/Campus_Recruitment_CSV`
- **Source URL:** [Hugging Face: Krooz/Campus_Recruitment_CSV](https://huggingface.co/datasets/Krooz/Campus_Recruitment_CSV)
- **Local File Path:** `data/raw/campus_recruitment.csv`
- **Task Type:** Binary Classification (Campus Placement Prediction)

---

## 2. Dataset Dimensions & Basic Health
- **Total Rows:** 10,000
- **Total Columns:** 11
- **Missing / Null Values:** 0 across all columns (100% complete)
- **Duplicate Rows:** 72 duplicate rows (0.72% of dataset; represents duplicate feature vectors resulting from low-cardinality discrete fields over 10,000 records)

### Column Names and Data Types
| # | Column Name | Raw Data Type | Recommended Role |
|---|-------------|---------------|------------------|
| 1 | `CGPA` | `float64` | Numerical Feature |
| 2 | `Internships` | `int64` | Numerical Feature (Discrete) |
| 3 | `Projects` | `int64` | Numerical Feature (Discrete) |
| 4 | `Workshops/Certifications` | `int64` | Numerical Feature (Discrete) |
| 5 | `AptitudeTestScore` | `int64` | Numerical Feature |
| 6 | `SoftSkillsRating` | `float64` | Numerical Feature |
| 7 | `ExtracurricularActivities` | `object` (`str`) | Categorical Feature (Binary) |
| 8 | `PlacementTraining` | `object` (`str`) | Categorical Feature (Binary) |
| 9 | `SSC_Marks` | `int64` | Numerical Feature |
| 10 | `HSC_Marks` | `int64` | Numerical Feature |
| 11 | `PlacementStatus` | `object` (`str`) | **Target Variable** |

---

## 3. Target Distribution (`PlacementStatus`)
- **Target Column:** `PlacementStatus`
- **Class Breakdown:**
  - `NotPlaced`: 5,803 (58.03%)
  - `Placed`: 4,197 (41.97%)
- **Total:** 10,000
- **Distribution Assessment:** Well-balanced distribution. Does not exhibit extreme class imbalance, so standard evaluation metrics (Accuracy, ROC-AUC, Precision, Recall, F1-Score) along with stratified splitting will perform reliably without mandatory oversampling techniques like SMOTE.

---

## 4. Categorical Columns Summary
| Column | Unique Values | Counts | Placement Rate (%) |
|--------|---------------|--------|---------------------|
| `ExtracurricularActivities` | `['No', 'Yes']` | No: 4,146 (41.5%)<br>Yes: 5,854 (58.5%) | No: 13.68% placed<br>Yes: 62.01% placed |
| `PlacementTraining` | `['No', 'Yes']` | No: 2,682 (26.8%)<br>Yes: 7,318 (73.2%) | No: 15.59% placed<br>Yes: 51.64% placed |
| `PlacementStatus` (Target) | `['NotPlaced', 'Placed']` | NotPlaced: 5,803<br>Placed: 4,197 | Target variable |

---

## 5. Statistical Profile of Numerical Features
| Feature | Min | 25% | Median (50%) | 75% | Max | Mean | Std Dev | Correlation with Placed (r) |
|---------|-----|-----|--------------|-----|-----|------|---------|-----------------------------|
| `AptitudeTestScore` | 60.0 | 73.0 | 80.0 | 87.0 | 90.0 | 79.45 | 8.16 | **+0.522** |
| `HSC_Marks` | 57.0 | 67.0 | 73.0 | 83.0 | 88.0 | 74.50 | 8.92 | **+0.506** |
| `Projects` | 0.0 | 1.0 | 2.0 | 3.0 | 3.0 | 2.03 | 0.87 | **+0.475** |
| `SSC_Marks` | 55.0 | 59.0 | 70.0 | 78.0 | 90.0 | 69.16 | 10.43 | **+0.470** |
| `SoftSkillsRating` | 3.0 | 4.0 | 4.4 | 4.7 | 4.8 | 4.32 | 0.41 | **+0.427** |
| `CGPA` | 6.5 | 7.4 | 7.7 | 8.2 | 9.1 | 7.70 | 0.64 | **+0.423** |
| `Workshops/Certifications` | 0.0 | 0.0 | 1.0 | 2.0 | 3.0 | 1.01 | 0.90 | **+0.362** |
| `Internships` | 0.0 | 1.0 | 1.0 | 1.0 | 2.0 | 1.05 | 0.67 | **+0.260** |

---

## 6. Feature-by-Feature Detailed Analysis

### 1. `CGPA`
- **Relevance:** High. Major baseline eligibility criterion for campus placement eligibility across tech and core companies. Placed students average 8.02 vs 7.47 for unplaced students.
- **Data Leakage Risk:** None. CGPA is documented and verified prior to campus recruitment drives.
- **Redundant Information:** Moderate correlation with HSC Marks ($r=0.46$) and SSC Marks ($r=0.41$), but represents collegiate academic performance and must be retained.
- **Preprocessing Requirements:** Numeric float. Standard scaling (`StandardScaler` or `MinMaxScaler`) for linear/logistic models; tree-based models can consume directly.

### 2. `Internships`
- **Relevance:** Moderate to High ($r=0.26$). Direct signal of practical industry experience. Placed students average 1.25 internships vs 0.90 for unplaced.
- **Data Leakage Risk:** None. Completed prior to placement interviews.
- **Redundant Information:** Low correlation with all other features ($r < 0.32$). Unique real-world experience signal.
- **Preprocessing Requirements:** Discrete numeric integer range $[0, 2]$.

### 3. `Projects`
- **Relevance:** Very High ($r=0.475$). Hands-on projects demonstrate software building and technical problem-solving capabilities. Placed students average 2.51 projects vs 1.68 for unplaced.
- **Data Leakage Risk:** None.
- **Redundant Information:** Positive correlation with HSC ($r=0.54$) and SSC ($r=0.50$), but captures technical output rather than test grades.
- **Preprocessing Requirements:** Discrete integer range $[0, 3]$.

### 4. `Workshops/Certifications`
- **Relevance:** Moderate ($r=0.362$). Indicates self-learning, skill acquisition, and proactive training.
- **Data Leakage Risk:** None. Completed before hiring season.
- **Redundant Information:** Distinct metric.
- **Preprocessing Requirements:** Rename column to eliminate special characters (`Workshops_Certifications` instead of `Workshops/Certifications`) to prevent syntax and serialization issues. Discrete integer range $[0, 3]$.

### 5. `AptitudeTestScore`
- **Relevance:** Highest numerical correlation with placement ($r=0.522$). Represents aptitude and general problem-solving rounds common to campus placement screening tests.
- **Data Leakage Risk:** Low as a screening score, but must be clearly contextualized in the application.
- **Crucial System Distinction:**
  > **Important Project Boundary:** The application's live 15-question aptitude test and IT/Core/Both technical assessment are **separate interactive application features**. Their scores must NOT be conflated or assumed equivalent to this dataset's `AptitudeTestScore`. In the student input form, this feature represents the student's standardized placement mock/drive aptitude score (range 60-90 / percentage).
- **Preprocessing Requirements:** Numeric integer range $[60, 90]$. Scaling recommended for linear classifiers.

### 6. `SoftSkillsRating`
- **Relevance:** High ($r=0.427$). Reflects behavioral competency, communication clarity, and teamwork evaluated during HR/managerial rounds.
- **Data Leakage Risk:** Low if captured via student self-assessment or mentor evaluation prior to final placement.
- **Redundant Information:** Distinct signal, moderately correlated with aptitude ($0.47$) and marks ($0.43$).
- **Preprocessing Requirements:** Continuous numeric float range $[3.0, 4.8]$ (or normalized on a $[1, 5]$ scale).

### 7. `ExtracurricularActivities`
- **Relevance:** Very High. Demonstrates dramatic placement differentiation: students with activities have a 62.0% placement rate vs only 13.7% for students without. Indicates leadership, teamwork, and active campus engagement.
- **Data Leakage Risk:** None.
- **Redundant Information:** None.
- **Preprocessing Requirements:** Binary mapping (`'Yes' -> 1`, `'No' -> 0`).

### 8. `PlacementTraining`
- **Relevance:** High. Students who took institutional placement training have a 51.6% placement rate vs 15.6% for those who did not.
- **Data Leakage Risk:** None. Represents pre-placement preparation programs offered by colleges.
- **Redundant Information:** None.
- **Preprocessing Requirements:** Binary mapping (`'Yes' -> 1`, `'No' -> 0`).

### 9. `SSC_Marks` (10th Standard Marks)
- **Relevance:** High ($r=0.470$). Represents foundational schooling consistency and is often used by companies as an initial shortlisting filter (e.g., minimum 60% or 70%).
- **Data Leakage Risk:** None (historical school marks).
- **Redundant Information:** Correlated with HSC marks ($r=0.525$), which is natural for academic performance across educational milestones.
- **Preprocessing Requirements:** Continuous integer percentage $[55, 90]$.

### 10. `HSC_Marks` (12th Standard Marks)
- **Relevance:** Very High ($r=0.506$). Key criterion in corporate and tech hiring eligibility cutoffs.
- **Data Leakage Risk:** None (historical school marks).
- **Redundant Information:** Moderate collinearity with SSC ($0.525$) and Aptitude ($0.565$), but widely demanded by campus eligibility policies.
- **Preprocessing Requirements:** Continuous integer percentage $[57, 88]$.

---

## 7. Recommended Features for Placement Prediction Model

All 10 features provide distinct, meaningful signals without data leakage or extreme multicollinearity (all pairwise correlation coefficients are below $0.60$).

### Recommended Feature Matrix:
| Feature Name | Clean Name | Type | Encoding / Preprocessing | Form Input Type |
|---|---|---|---|---|
| `CGPA` | `CGPA` | Numeric Float | Pass-through / Scaler | Numeric input (6.5 – 10.0) |
| `Internships` | `Internships` | Numeric Integer | Pass-through | Stepper / Number input (0 – 5) |
| `Projects` | `Projects` | Numeric Integer | Pass-through | Stepper / Number input (0 – 10) |
| `Workshops/Certifications` | `Workshops_Certifications` | Numeric Integer | Pass-through | Stepper / Number input (0 – 10) |
| `AptitudeTestScore` | `AptitudeTestScore` | Numeric Integer | Pass-through / Scaler | Score input (0 – 100) |
| `SoftSkillsRating` | `SoftSkillsRating` | Numeric Float | Pass-through / Scaler | Rating slider (1.0 – 5.0) |
| `ExtracurricularActivities` | `ExtracurricularActivities` | Categorical Binary | Binary (Yes: 1, No: 0) | Radio / Selectbox ('Yes', 'No') |
| `PlacementTraining` | `PlacementTraining` | Categorical Binary | Binary (Yes: 1, No: 0) | Radio / Selectbox ('Yes', 'No') |
| `SSC_Marks` | `SSC_Marks` | Numeric Integer | Pass-through / Scaler | Percentage input (0 – 100) |
| `HSC_Marks` | `HSC_Marks` | Numeric Integer | Pass-through / Scaler | Percentage input (0 – 100) |

### Key Takeaway for Implementation:
- **No data leakage exists** in these 10 features.
- Target column `PlacementStatus` should be encoded as `{'Placed': 1, 'NotPlaced': 0}`.
- Special character in `Workshops/Certifications` should be cleanly renamed to `Workshops_Certifications`.
- The live aptitude test and domain assessments remain decoupled and serve the recommendation and skill-gap features of the application.
