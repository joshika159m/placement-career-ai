# Exploratory Data Analysis (EDA) Report

**Dataset:** `data/processed/campus_recruitment_encoded.csv`  
**Purpose:** Comprehensive statistical profiling, distribution analysis, target relationship exploration, correlation mapping, and outlier assessment.

---

## 1. Dataset Shape and Data Types

- **Total Rows:** `9,928`
- **Total Columns:** `11`
- **Memory Usage:** ~853 KB

| Column Name | Data Type | Encoding / Description |
|---|---|---|
| `CGPA` | `float64` | Continuous collegiate GPA (scale 6.5 to 9.1) |
| `Internships` | `int64` | Discrete count of completed internships (0, 1, 2) |
| `Projects` | `int64` | Discrete count of completed academic/personal projects (0 to 3) |
| `Workshops_Certifications` | `int64` | Discrete count of certifications and workshops attended (0 to 3) |
| `AptitudeTestScore` | `int64` | Standardized placement drive/screening aptitude exam score (60 to 90) |
| `SoftSkillsRating` | `float64` | Behavioral and communication rating (3.0 to 4.8) |
| `ExtracurricularActivities` | `int64` | Binary flag: `1` = Yes, `0` = No |
| `PlacementTraining` | `int64` | Binary flag: `1` = Yes, `0` = No |
| `SSC_Marks` | `int64` | Secondary School Certificate (10th grade) percentage (55 to 90) |
| `HSC_Marks` | `int64` | Higher Secondary Certificate (12th grade) percentage (57 to 88) |
| `PlacementStatus` | `int64` | **Target variable:** `1` = Placed, `0` = NotPlaced |

---

## 2. Missing Values

| Column | Null / Missing Count | % Missing |
|---|---|---|
| `CGPA` | 0 | 0.0% |
| `Internships` | 0 | 0.0% |
| `Projects` | 0 | 0.0% |
| `Workshops_Certifications` | 0 | 0.0% |
| `AptitudeTestScore` | 0 | 0.0% |
| `SoftSkillsRating` | 0 | 0.0% |
| `ExtracurricularActivities` | 0 | 0.0% |
| `PlacementTraining` | 0 | 0.0% |
| `SSC_Marks` | 0 | 0.0% |
| `HSC_Marks` | 0 | 0.0% |
| `PlacementStatus` | 0 | 0.0% |

**Summary:** The dataset has zero missing values across all columns.

---

## 3. Target Distribution (`PlacementStatus`)

Visualized in `docs/eda/target_distribution.png`:

| Class Label | Value | Student Count | Percentage (%) |
|---|---|---|---|
| **Not Placed** | `0` | 5,801 | **58.43%** |
| **Placed** | `1` | 4,127 | **41.57%** |
| **Total** | - | **9,928** | **100.00%** |

### Insights:
- The target classes are well-balanced (approximately 58% unplaced vs 42% placed).
- There is no severe class imbalance, meaning standard cross-validation (Stratified 5-Fold) and evaluation metrics (Accuracy, ROC-AUC, F1-Score, Precision, Recall) will be stable and reliable without synthetic oversampling (e.g., SMOTE).

---

## 4. Descriptive Statistics for Numerical Features

| Feature | Count | Mean | Median (50%) | Std Dev | Min | Max |
|---|---|---|---|---|---|---|
| `CGPA` | 9,928 | 7.69 | 7.70 | 0.64 | 6.50 | 9.10 |
| `Internships` | 9,928 | 1.04 | 1.00 | 0.66 | 0.00 | 2.00 |
| `Projects` | 9,928 | 2.02 | 2.00 | 0.87 | 0.00 | 3.00 |
| `Workshops_Certifications` | 9,928 | 1.01 | 1.00 | 0.90 | 0.00 | 3.00 |
| `AptitudeTestScore` | 9,928 | 79.38 | 80.00 | 8.14 | 60.00 | 90.00 |
| `SoftSkillsRating` | 9,928 | 4.32 | 4.40 | 0.41 | 3.00 | 4.80 |
| `SSC_Marks` | 9,928 | 69.09 | 70.00 | 10.43 | 55.00 | 90.00 |
| `HSC_Marks` | 9,928 | 74.43 | 73.00 | 8.90 | 57.00 | 88.00 |

Visualized in `docs/eda/feature_distributions.png`.

---

## 5. Feature Distribution Highlights

1. **`CGPA`:** Bell-shaped continuous distribution centered tightly around mean 7.69 and median 7.70.
2. **`Internships`:** Discrete distribution with high concentration at 1 internship (5,537 students), 0 internships (2,001 students), and 2 internships (2,390 students).
3. **`Projects`:** Right-leaning discrete distribution; the majority completed 2 projects (4,756 students) or 3 projects (3,047 students).
4. **`Workshops_Certifications`:** Uniform-to-exponential decline; 0 (3,398 students), 1 (3,668 students), 2 (2,228 students), 3 (634 students).
5. **`AptitudeTestScore`:** Approximately normal distribution with peak density between 75 and 85, spanning from 60 to 90.
6. **`SoftSkillsRating`:** Left-skewed distribution spanning 3.0 to 4.8, with high density between 4.2 and 4.6.
7. **`SSC_Marks` & `HSC_Marks`:** Broad, smooth distributions representing academic percentages across secondary schooling.

---

## 6. Numerical Comparison: Placed (`1`) vs Not Placed (`0`)

Visualized in `docs/eda/numerical_by_placement_boxplots.png` and `docs/eda/numerical_by_placement_kde.png`:

| Feature | Metric | Not Placed (`0`) | Placed (`1`) | Absolute Difference ($\Delta$) | Direction |
|---|---|---|---|---|---|
| **`CGPA`** | Mean ± Std<br>Median | 7.47 ± 0.60<br>7.50 | **8.01 ± 0.55**<br>**8.20** | **+0.54** | Placed students have significantly higher GPA |
| **`Internships`** | Mean ± Std<br>Median | 0.90 ± 0.59<br>1.00 | **1.24 ± 0.71**<br>1.00 | **+0.34** | 38% higher internship average |
| **`Projects`** | Mean ± Std<br>Median | 1.68 ± 0.77<br>1.00 | **2.50 ± 0.75**<br>**3.00** | **+0.82** | Median jump from 1 to 3 projects |
| **`Workshops_Certifications`** | Mean ± Std<br>Median | 0.73 ± 0.79<br>1.00 | **1.39 ± 0.91**<br>**2.00** | **+0.66** | Placed students completed nearly $2\times$ more workshops |
| **`AptitudeTestScore`** | Mean ± Std<br>Median | 75.83 ± 7.48<br>76.00 | **84.36 ± 6.18**<br>**86.00** | **+8.53** | Substantial separation in screening aptitude |
| **`SoftSkillsRating`** | Mean ± Std<br>Median | 4.17 ± 0.41<br>4.20 | **4.53 ± 0.32**<br>**4.60** | **+0.36** | Placed students consistently rated above 4.5 |
| **`SSC_Marks`** | Mean ± Std<br>Median | 65.00 ± 9.53<br>62.00 | **74.85 ± 8.79**<br>**76.00** | **+9.85** | +14-point jump in median 10th marks |
| **`HSC_Marks`** | Mean ± Std<br>Median | 70.67 ± 7.74<br>69.00 | **79.71 ± 7.65**<br>**83.00** | **+9.04** | +14-point jump in median 12th marks |

---

## 7. Categorical Feature Analysis & Placement Rates

Visualized in `docs/eda/categorical_placement_rates.png`:

### A. `ExtracurricularActivities`
| Category | Total Students | Not Placed (`0`) | Placed (`1`) | **Placement Rate (%)** |
|---|---|---|---|---|
| **No (`0`)** | 4,144 | 3,577 | 567 | **13.68%** |
| **Yes (`1`)** | 5,784 | 2,224 | 3,560 | **61.55%** |
| **Total** | 9,928 | 5,801 | 4,127 | 41.57% |

- **Impact:** Students with extracurricular activities have a **4.5x higher placement probability** (61.55% vs 13.68%).

### B. `PlacementTraining`
| Category | Total Students | Not Placed (`0`) | Placed (`1`) | **Placement Rate (%)** |
|---|---|---|---|---|
| **No (`0`)** | 2,682 | 2,264 | 418 | **15.59%** |
| **Yes (`1`)** | 7,246 | 3,537 | 3,709 | **51.19%** |
| **Total** | 9,928 | 5,801 | 4,127 | 41.57% |

- **Impact:** Formal college placement training increases the placement likelihood from **15.59% to 51.19%** (a **3.3x increase**).

---

## 8. Correlation Analysis

Visualized in `docs/eda/correlation_heatmap.png`:

### Rank-Ordered Correlations with `PlacementStatus`:
| Rank | Feature | Correlation with `PlacementStatus` ($r$) | Strength & Interpretation |
|---|---|---|---|
| 1 | **`AptitudeTestScore`** | **+0.517** | Strongest predictor; initial recruitment screening round |
| 2 | **`HSC_Marks`** | **+0.501** | Strong predictor; 12th cutoff threshold |
| 3 | **`ExtracurricularActivities`** | **+0.479** | Strong predictor; soft-skill & leadership differentiator |
| 4 | **`Projects`** | **+0.470** | Strong predictor; hands-on technical validation |
| 5 | **`SSC_Marks`** | **+0.466** | Strong predictor; secondary school foundation |
| 6 | **`SoftSkillsRating`** | **+0.422** | Moderate-strong; interview/HR clearance |
| 7 | **`CGPA`** | **+0.419** | Moderate-strong; collegiate eligibility benchmark |
| 8 | **`Workshops_Certifications`**| **+0.357** | Moderate; continuous learning and upskilling |
| 9 | **`PlacementTraining`** | **+0.321** | Moderate; preparation and mock interview training |
| 10 | **`Internships`** | **+0.252** | Moderate; professional experience |

### Inter-Feature Correlation Summary:
- No pair of input features exhibits problematic multicollinearity ($r \ge 0.80$).
- Highest inter-feature correlations:
  - `AptitudeTestScore` & `HSC_Marks`: $r = 0.56$
  - `Projects` & `HSC_Marks`: $r = 0.53$
  - `SSC_Marks` & `HSC_Marks`: $r = 0.52$
  - `AptitudeTestScore` & `SSC_Marks`: $r = 0.51$
- Every feature contributes distinct, complementary variance without feature redundancy.

---

## 9. Outlier Analysis

Visualized in `docs/eda/outliers_boxplots.png`:

### A. Interquartile Range (IQR) Method ($1.5 \times \text{IQR}$)
| Feature | Q1 | Q3 | IQR | Lower Bound | Upper Bound | Outlier Count | % Outliers | Diagnosis |
|---|---|---|---|---|---|---|---|---|
| `CGPA` | 7.40 | 8.20 | 0.80 | 6.20 | 9.40 | **0** | 0.00% | Clean continuous |
| `Internships` | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 | *4,391* | *44.23%* | **Artifact of discrete IQR (Q1=Q3=1)** |
| `Projects` | 1.00 | 3.00 | 2.00 | -2.00 | 6.00 | **0** | 0.00% | Clean discrete |
| `Workshops_Certifications` | 0.00 | 2.00 | 2.00 | -3.00 | 5.00 | **0** | 0.00% | Clean discrete |
| `AptitudeTestScore` | 73.00 | 87.00 | 14.00 | 52.00 | 108.00 | **0** | 0.00% | Clean continuous |
| `SoftSkillsRating` | 4.00 | 4.70 | 0.70 | 2.95 | 5.75 | **0** | 0.00% | Clean continuous |
| `SSC_Marks` | 59.00 | 78.00 | 19.00 | 30.50 | 106.50 | **0** | 0.00% | Clean continuous |
| `HSC_Marks` | 67.00 | 83.00 | 16.00 | 43.00 | 107.00 | **0** | 0.00% | Clean continuous |

### B. Standard Z-Score Method ($|Z| > 3$)
- **Continuous Features (`CGPA`, `AptitudeTestScore`, `SSC_Marks`, `HSC_Marks`):** **0 outliers** ($|Z| > 3$).
- **Discrete Features (`Internships`, `Projects`, `Workshops_Certifications`):** **0 outliers** ($|Z| > 3$).
- **`SoftSkillsRating`:** 20 records (0.20% of data) with $Z \approx -3.22$ corresponding to rating `3.0`.
  - **Verdict:** These represent legitimate minimum ratings on a 3.0–5.0 evaluation rubric, not erroneous data entry or measurement errors.

### Summary:
There are **no extreme anomalies or corrupted outliers** in the dataset. All numerical ranges fall within valid academic bounds ($CGPA \in [6.5, 9.1]$, Marks $\in [55, 90]$, Counts $\in [0, 3]$). Outlier truncation or clipping is unnecessary.

---

## 10. Key Takeaways & Recommendations for Modeling

1. **Balanced Target:** 58.43% `NotPlaced` vs 41.57% `Placed`. Modeling does not require re-sampling or cost-sensitive class weights.
2. **Top Separation Drivers:** `AptitudeTestScore`, `HSC_Marks`, `ExtracurricularActivities`, `Projects`, and `SSC_Marks` provide the greatest separation between placed and unplaced candidates.
3. **No Multicollinearity Bottleneck:** No pairwise correlation exceeds $0.60$. All 10 features can be safely supplied to machine learning models (e.g., Logistic Regression, Random Forest, XGBoost/LightGBM).
4. **Data Scaling Strategy:** Features with wider ranges (`AptitudeTestScore` [60-90], `SSC_Marks` [55-90], `HSC_Marks` [57-88]) should be standardized (`StandardScaler`) when evaluating linear or distance-based models; tree models are invariant.
5. **Clear Application Distinction:** The model's input for `AptitudeTestScore` should remain clearly designated as general mock aptitude score, leaving the app's internal 15-question test for interactive assessment and recommendation.
