# Final Project Report

# Machine Learning-Based Placement Prediction and Career Recommendation System

---

## 1. ABSTRACT

Campus recruitment is a pivotal milestone in tertiary engineering education, presenting students with critical decisions regarding academic preparation, skill acquisition, and career trajectory. Conventional placement support systems rely primarily on post-hoc outcomes, subjective mentoring, or blunt GPA cutoffs without offering actionable diagnostic insights. This project develops an end-to-end, interpretable **Machine Learning-Based Placement Prediction and Career Recommendation System** implemented in pure Python and Streamlit. 

The system integrates three distinct analytical pillars:
1. An empirical binary classification model trained on 9,928 cleaned campus recruitment records to predict baseline campus placement probability.
2. Independent interactive assessments—a 15-question cognitive aptitude assessment and a 15-question domain-specific technical assessment (supporting IT, Core Engineering, and Combined tracks).
3. A transparent, deterministic rule-based Career Recommendation Engine.

Using a rigorous 80/20 stratified holdout protocol, multiple classifiers (Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting) were evaluated and tuned via 5-fold stratified cross-validation. Tuned Logistic Regression achieved a test F1 score of **0.7762** and ROC-AUC of **0.8855**, exhibiting superior stability and linear explainability. Global and local feature contributions are extracted directly from standardized model coefficients, explaining predictions without opaque heuristics. The Career Recommendation Engine combines Technical Mastery ($50\%$), Cognitive Aptitude ($25\%$), and Placement Readiness ($25\%$) across 12 engineering career roles, diagnosing specific topic gaps below a $70\%$ threshold and generating actionable learning roadmaps. The system is verified by a 50-test automated suite and hosted on a unified single-page Streamlit interface.

---

## 2. INTRODUCTION

### 2.1 Background
Higher educational institutions face increasing pressure to ensure positive placement outcomes for engineering graduates. In modern campus recruitment drives, companies employ multi-tier screening processes comprising standardized aptitude tests, technical coding assessments, domain interviews, and behavioral screenings. Consequently, placement readiness is inherently multi-faceted, requiring students to balance academic consistency, project portfolio strength, communicative aptitude, and specialized technical knowledge.

### 2.2 Motivation
Undergraduate engineering students frequently lack objective feedback regarding their placement readiness prior to their final year. Traditional advising often provides generic advice, failing to quantify how individual profile attributes (such as project completion, internships, or placement training) contribute to hiring likelihood. Furthermore, students frequently struggle to identify which industrial career tracks (e.g., Software Development, Data Analytics, DevOps, or Embedded Systems) align with their technical and cognitive strengths, resulting in misallocated preparation effort.

### 2.3 Problem Statement
To design, implement, and validate an integrated, interpretable machine learning and assessment system that:
1. Predicts campus placement probability from student academic and co-curricular metrics with calibrated confidence.
2. Explains the statistical basis of individual predictions via local feature contribution analysis.
3. Evaluates real-time student aptitude and technical competencies through balanced diagnostic assessments.
4. Synthesizes empirical readiness with assessment outcomes to recommend ranked career paths and actionable skill-gap improvement plans.

### 2.4 Need for the System
An automated, transparent platform bridges the gap between academic education and corporate recruitment expectations. By decoupling static historical metrics from dynamic real-time assessments and avoiding uninterpretable black-box models, the system empowers students with clear diagnostics: identifying precisely where their profile stands, what specific topics require upskilling, and which career paths offer the highest probability of professional success.

---

## 3. OBJECTIVES

1. **Empirical Dataset Curation & Cleaning:** Ingest and statistically audit benchmark campus recruitment data, resolve duplicate vectors, and establish a data leakage-free preprocessing pipeline.
2. **Predictive Modeling & Tuning:** Evaluate multiple baseline machine learning algorithms using stratified validation, tune hyperparameters using cross-validation on training data alone, and deploy the optimal calibrated classifier.
3. **Transparent Explainability:** Implement global and local log-odds feature importance decomposition to clarify model predictions without surrogate approximations.
4. **Interactive Cognitive & Technical Diagnostics:** Construct verified question banks and dynamic 15-question assessment modules enforcing strict category quotas across Aptitude, IT, and Core engineering domains.
5. **Deterministic Career Matching:** Formulate a weighted, explainable career recommendation engine spanning 12 defined roles with automated skill-gap identification and targeted remediation.
6. **Unified Web Interface:** Assemble an interactive, single-page Streamlit dashboard managing state persistence across the end-to-end evaluation lifecycle.

---

## 4. EXISTING SYSTEM

### 4.1 Existing Approach
Current academic approaches to placement forecasting and career advising typically utilize:
- **Minimum Eligibility Thresholds:** Rigid eligibility criteria enforced by institutional training and placement cells (e.g., cutoffs of 60% in secondary schooling and 7.0 CGPA).
- **Ad-Hoc Manual Counseling:** Subjective mentoring conducted by faculty advisors based on informal student self-assessment.
- **Generic Question Portals:** Disconnected mock test portals that provide aggregate percentage scores without correlating results to recruitment probabilities or target career tracks.
- **Opaque Black-Box Classifiers:** Academic prototypes utilizing complex neural networks or uncalibrated classifiers that output binary labels without interpretable explanations.

### 4.2 Limitations of Existing System
- **Lack of Interpretability:** Students receiving a negative prediction are not informed which specific factors depressed their score or what remediation would reverse it.
- **Conflation of Signals:** Existing systems either rely entirely on past academic grades or entirely on test scores, failing to synthesize historical performance with real-time competency.
- **Absence of Actionable Roadmaps:** General platforms output pass/fail ratings but do not diagnose granular topic weaknesses (e.g., SQL normalization or RTOS scheduling) against specific job roles.
- **Data Leakage in Research Prototypes:** Many published placement models apply preprocessing scalers or synthetic sampling across entire datasets prior to splitting, producing overly optimistic, non-generalizable results.

---

## 5. PROPOSED SYSTEM

### 5.1 Overview
The proposed system establishes a cohesive, multi-stage analytical framework. It takes raw student profile metrics, standardizes them through an isolated preprocessing pipeline, and generates a calibrated placement probability. Simultaneously, it administers live, quota-controlled aptitude and technical assessments. These distinct signals converge in a rule-based Career Recommendation Engine that scores and ranks 12 defined career paths, highlighting skill deficits below a 70% mastery threshold.

```
+-----------------------------------------------------------------------------------+
|                                 PROPOSED SYSTEM                                   |
+-----------------------------------------------------------------------------------+
   [ Student Profile ]               [ Live Aptitude ]            [ Live Technical ]
   (10 Acad/Skill Features)         (15 Balanced MCQs)           (IT / Core / Both)
             |                              |                             |
             v                              v                             v
   [ ML Placement Model ]           [ Cognitive Score ]           [ Topic Mastery ]
   (Logistic Regression)             (0 - 100% Scale)             (0 - 100% Scale)
             |                              |                             |
             v                              |                             |
    Placement Probability (25%) <-----------+-----------------------------+ (50%)
             +------------------------------+ (25%)
             |
             v
   [ Deterministic Career Engine ] ---> Top 3 Roles (Strong / Good / Moderate)
             |
             +------------------------> Skill Gap Diagnostics (< 70% Cutoff)
             |
             +------------------------> Actionable Improvement Roadmap
```

### 5.2 Key Features
- **Separation of Measurement Signals:** The model's historical `AptitudeTestScore` feature is strictly isolated from the live 15-question interactive aptitude test.
- **Local Log-Odds Explainability:** Real-time decomposition of individual student feature contributions ($x_{\text{trans}} \cdot \beta$), visually distinguishing features that support placement from those that increase risk.
- **Multi-Track Technical Assessment:** Flexible assessment modes supporting Pure IT (7 topics), Pure Core Electronics (8 topics), and Combined Tracks (8 IT + 7 Core).
- **Rule-Based Career Synthesis:** Predictable 50/25/25 scoring formula ensuring transparency during institutional review and project viva.
- **Granular Skill-Gap Mapping:** Automated identification of unassessed prerequisites and underperforming topics mapped directly to concrete study tasks.

### 5.3 Advantages
- 100% transparent and mathematically defensible.
- Zero data leakage in machine learning validation.
- Requires no external database, user authentication, or third-party paid APIs.
- Instant, client-side inference and assessment evaluation.
- Highly actionable, student-centric guidance.

---

## 6. SYSTEM REQUIREMENTS

### 6.1 Hardware Requirements
- **Processor:** Intel Core i3 / AMD Ryzen 3 or higher (Dual-Core 2.0 GHz minimum).
- **RAM:** 4 GB minimum (8 GB recommended for local development).
- **Storage:** 500 MB free hard disk space for code, model weights, and datasets.
- **Display:** Minimum 1280x720 screen resolution.

### 6.2 Software Requirements
- **Operating System:** Windows 10/11, Ubuntu 20.04+, or macOS 12+.
- **Runtime Environment:** Python 3.10, 3.11, or 3.12.
- **Key Python Libraries:**
  - `streamlit` ($\ge 1.30$): Interactive web application framework.
  - `scikit-learn` ($\ge 1.3$): Preprocessing pipelines and model estimators.
  - `pandas` ($\ge 2.0$) & `numpy` ($\ge 1.24$): Data transformation and numerical operations.
  - `joblib` ($\ge 1.3$): Pipeline serialization and disk persistence.
  - `matplotlib` ($\ge 3.7$) & `seaborn` ($\ge 0.12$): Visualization and figure generation.
- **Browser:** Google Chrome, Mozilla Firefox, Microsoft Edge, or Safari with JavaScript enabled.

---

## 7. SYSTEM ARCHITECTURE

The application follows a clean modular pipeline pattern with unidirectional data flow:

```
                           +-------------------------------------+
                           |            Student Input            |
                           +-------------------------------------+
                                              |
                                              v
                           +-------------------------------------+
                           |      Data Preprocessing Pipeline    |
                           |   (StandardScaler + Passthrough)    |
                           +-------------------------------------+
                                              |
                                              v
                           +-------------------------------------+
                           |      Logistic Regression Model      |
                           |    (C=0.5, class_weight='balanced') |
                           +-------------------------------------+
                                              |
                       +----------------------+----------------------+
                       |                                             |
                       v                                             v
        +-----------------------------+               +-----------------------------+
        |     Placement Probability   |               |     Local Logit Effects     |
        |       (P_placed in [0, 1])  |               |  (x_i * beta_i Contributions)|
        +-----------------------------+               +-----------------------------+
                       |                                             |
                       |                                             v
                       |                              +-----------------------------+
                       |                              |  Explainability Bar Chart   |
                       |                              +-----------------------------+
                       |
                       +----------------------+
                                              |
                                              v
+-------------------------------+   +-------------------------------+
|    Live Aptitude Assessment   |   |   Live Technical Assessment   |
|   (15 Balanced Cognitive MCQs)|   |   (15 IT / Core / Both MCQs)  |
+-------------------------------+   +-------------------------------+
                |                                   |
                v                                   v
+-------------------------------+   +-------------------------------+
|     Aptitude Match (25%)      |   |     Technical Match (50%)     |
+-------------------------------+   +-------------------------------+
                \                                   /
                 \                                 /
                  v                               v
             +-----------------------------------------+
             |    Career Recommendation Engine (50/25/25)|
             +-----------------------------------------+
                                  |
                                  v
             +-----------------------------------------+
             |      Top 3 Career Recommendations       |
             |       + Match Confidence Levels         |
             |       + "Why Recommended" Rationales    |
             |       + Skill Gaps (< 70% Cutoff)       |
             |       + Actionable Improvement Roadmap  |
             +-----------------------------------------+
```

---

## 8. DATASET DESCRIPTION

- **Source:** Hugging Face benchmark repository (`Krooz/Campus_Recruitment_CSV`).
- **Raw Dimensions:** 10,000 student records across 11 columns.
- **Target Variable:** `PlacementStatus` (Binary: `Placed` vs `NotPlaced`).
- **Completeness:** 0 missing, null, or NaN values across all 10,000 records (100% complete).

### Feature Inventory:
| Column Name | Type | Domain / Range | Description |
|---|---|---|---|
| `CGPA` | Continuous Float | 6.50 – 9.10 | Cumulative Grade Point Average in undergraduate study |
| `Internships` | Discrete Integer | 0 – 2 | Count of completed professional internships |
| `Projects` | Discrete Integer | 0 – 3 | Count of completed technical academic/personal projects |
| `Workshops_Certifications` | Discrete Integer | 0 – 3 | Count of workshops or industry certifications attended |
| `AptitudeTestScore` | Discrete Integer | 60 – 90 | Screening score from institutional mock aptitude tests |
| `SoftSkillsRating` | Continuous Float | 3.00 – 4.80 | Faculty/mentor rating of behavioral and communication skills |
| `ExtracurricularActivities`| Binary Categorical| `Yes` / `No` | Active involvement in collegiate clubs, sports, or leadership |
| `PlacementTraining` | Binary Categorical| `Yes` / `No` | Completion of formal institutional placement preparation training |
| `SSC_Marks` | Discrete Integer | 55 – 90 | Secondary School Certificate (10th standard) percentage |
| `HSC_Marks` | Discrete Integer | 57 – 88 | Higher Secondary Certificate (12th standard) percentage |
| `PlacementStatus` | Binary Categorical| `Placed` / `NotPlaced` | Recruitment outcome (Target Variable) |

---

## 9. DATA PREPROCESSING

### 9.1 Duplicate Row Analysis & Removal
An exhaustive audit of the 10,000 raw records identified 72 completely identical feature-and-target duplicate rows (comprising 138 rows across 66 unique patterns). Detailed inspection revealed that these duplicates were heavily concentrated at the extreme upper-performance ceiling (97.1% Placed), with identical profiles repeating across theoretical split boundaries. To prevent artificial performance inflation, exact duplicate rows were dropped:
- **Raw records:** 10,000
- **Duplicates removed:** 72 rows
- **Cleaned dataset:** **9,928 unique records**

### 9.2 Feature Standardization & Encoding
1. **Identifier & Column Normalization:** Renamed `Workshops/Certifications` to `Workshops_Certifications` to ensure cross-platform serialization safety.
2. **Binary Encoding:**
   - `ExtracurricularActivities`: `Yes` $\rightarrow 1$, `No` $\rightarrow 0$
   - `PlacementTraining`: `Yes` $\rightarrow 1$, `No` $\rightarrow 0$
   - `PlacementStatus`: `Placed` $\rightarrow 1$, `NotPlaced` $\rightarrow 0$
3. **Data Leakage Elimination:** Continuous and discrete numerical features (`CGPA`, `Internships`, `Projects`, `Workshops_Certifications`, `AptitudeTestScore`, `SoftSkillsRating`, `SSC_Marks`, `HSC_Marks`) were scaled using `StandardScaler`. The transformation was packaged into a `ColumnTransformer` fitted strictly on training partitions (`X_train`), leaving test vectors completely unseen prior to inference.

---

## 10. EXPLORATORY DATA ANALYSIS (EDA)

### 10.1 Target Distribution
In the cleaned dataset (9,928 rows):
- `NotPlaced (0)`: **5,801 students (58.43%)**
- `Placed (1)`: **4,127 students (41.57%)**
The distribution exhibits a natural, mild imbalance (~58:42), confirming that synthetic oversampling (e.g., SMOTE) is unnecessary and that standard stratified metrics remain robust.

### 10.2 Feature Comparison: Placed vs Not Placed
Placed students consistently display statistically significant shifts in academic and co-curricular metrics:
- **`CGPA`:** Placed students averaged **8.01** ($\pm 0.55$) vs **7.47** ($\pm 0.60$) for unplaced students.
- **`Projects`:** Median jumped from **1.0 project** (unplaced) to **3.0 projects** (placed).
- **`AptitudeTestScore`:** Placed mean of **84.36** vs unplaced mean of **75.83** (+8.53 point difference).
- **`SSC_Marks` & `HSC_Marks`:** Median jumped by **+14 percentage points** for placed candidates.

### 10.3 Categorical Placement Rates
- **`ExtracurricularActivities`:** Students participating in activities achieved a **61.55% placement rate**, compared to only **13.68%** for non-participants (a **4.5x multiplier**).
- **`PlacementTraining`:** Students completing formal training achieved a **51.19% placement rate**, compared to **15.59%** for untrained students (a **3.3x multiplier**).

### 10.4 Correlation Structure
No inter-feature correlation exceeded $r = 0.56$ (the highest being `AptitudeTestScore` vs `HSC_Marks` at $0.56$). Multicollinearity is absent, confirming that all 10 features provide distinct, complementary predictive signals.

---

## 11. MACHINE LEARNING METHODOLOGY

### 11.1 Experimental Design
- **Split Ratio:** 80% Training ($N = 7,942$) and 20% Testing ($N = 1,986$).
- **Partitioning Method:** Stratified sampling (`random_state=42`), locking identical target ratios ($58.44\%$ unplaced vs $41.56\%$ placed) across both sets.
- **Algorithms Evaluated:**
  1. *Logistic Regression:* Generalized linear classifier modeling the log-odds of placement.
  2. *Decision Tree (CART):* Non-linear recursive partitioning baseline.
  3. *Random Forest:* Bagged ensemble of 100 decorrelated decision trees.
  4. *Gradient Boosting Classifier:* Sequential boosting minimizing log-loss via gradient descent.
- **Primary Metric:** **F1-Score** (harmonic mean of Precision and Recall), balancing detection of placed candidates against false positive alarms. Secondary metric: **ROC-AUC**.

---

## 12. BASELINE MODEL RESULTS

Each baseline pipeline was trained on `X_train` and evaluated on the untouched test partition ($N = 1,986$):

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | TN | FP | FN | TP |
|---|---|---|---|---|---|---|---|---|---|
| **Logistic Regression** | **0.8097** | 0.7732 | **0.7676** | **0.7704** | **0.8854** | 974 | 186 | 192 | 634 |
| **Gradient Boosting** | 0.8072 | **0.7772** | 0.7518 | 0.7643 | **0.8858** | 982 | 178 | 205 | 621 |
| **Random Forest** | 0.7966 | 0.7755 | 0.7191 | 0.7462 | 0.8747 | 988 | 172 | 232 | 594 |
| **Decision Tree** | 0.7266 | 0.6758 | 0.6586 | 0.6671 | 0.7187 | 899 | 261 | 282 | 544 |

*Summary:* Logistic Regression and Gradient Boosting performed comparably as top baseline contenders, achieving ~81% accuracy and ~0.885 ROC-AUC. Single Decision Trees suffered from severe variance ($F1 = 0.6671$).

---

## 13. HYPERPARAMETER TUNING

Hyperparameters were systematically tuned using **Stratified 5-Fold Cross-Validation strictly on `X_train`** (`scoring='f1'`). The test set was held out completely unseen during grid searching.

### Cross-Validation Search & Selected Configurations:
1. **Logistic Regression:** Regularization strength $C \in \{0.01, 0.1, 0.5, 1.0, 5.0, 10.0\}$, class weighting $\in \{\text{None}, \text{'balanced'}\}$, solver $\in \{\text{'lbfgs'}\}$.
   - *Best Params:* `C=0.5`, `class_weight='balanced'`, `penalty='l2'`, `solver='lbfgs'`.
   - *Mean CV F1:* **0.7609** ($\pm 0.0085$), *Mean CV ROC-AUC:* **0.8735** ($\pm 0.0056$).
2. **Gradient Boosting:** Estimators $\in \{50, 100, 150\}$, learning rate $\in \{0.03, 0.05, 0.1\}$, max depth $\in \{3, 4\}$.
   - *Best Params:* `n_estimators=100`, `learning_rate=0.03`, `max_depth=3`, `subsample=0.85`.
   - *Mean CV F1:* **0.7491** ($\pm 0.0110$), *Mean CV ROC-AUC:* **0.8727** ($\pm 0.0064$).
3. **Random Forest:** Estimators $\in \{100, 200\}$, max depth $\in \{8, 10, 12, \text{None}\}$.
   - *Best Params:* `n_estimators=200`, `max_depth=10`, `min_samples_split=2`, `min_samples_leaf=2`.
   - *Mean CV F1:* **0.7454** ($\pm 0.0115$), *Mean CV ROC-AUC:* **0.8711** ($\pm 0.0064$).

### Tuned Models Evaluated on Untouched Test Set ($N = 1,986$):
| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | TN | FP | FN | TP |
|---|---|---|---|---|---|---|---|---|---|
| **Logistic Regression (Tuned)** | 0.8051 | 0.7431 | **0.8123** | **0.7762** | **0.8855** | 928 | 232 | 155 | 671 |
| **Gradient Boosting (Tuned)** | **0.8152** | **0.7909** | 0.7554 | 0.7728 | **0.8881** | 995 | 165 | 202 | 624 |
| **Random Forest (Tuned)** | 0.8026 | 0.7761 | 0.7385 | 0.7568 | 0.8851 | 984 | 176 | 216 | 610 |

---

## 14. FINAL MODEL SELECTION & DEPLOYMENT

### Justification for Final Model Selection:
While Gradient Boosting attained slightly higher raw accuracy ($81.52\%$) and precision ($79.09\%$), **Tuned Logistic Regression** was selected as the final operational model based on key engineering criteria:
1. **Highest F1-Score (0.7762) & Highest Recall (0.8123):** Crucial in placement advising to minimize False Negatives (students predicted unplaced when they possess placement potential).
2. **Minimal Generalization Variance:** CV F1 ($0.7609$) to Test F1 ($0.7762$) demonstrates high stability without tree overfitting.
3. **Deterministic Mathematical Interpretability:** Direct log-odds decomposition allows instantaneous local feature explanations in the user interface without running secondary surrogate explainers.

### Final Pipeline Production Training:
The final pipeline:
$$\text{Pipeline}\Big(\text{preprocessor}=\text{ColumnTransformer}(\text{StandardScaler}, \text{passthrough}), \text{classifier}=\text{LogisticRegression}(C=0.5, \text{class\_weight}=\text{'balanced'})\Big)$$
was refitted on all **9,928 cleaned records** and serialized to [`models/placement_model.pkl`](file:///e:/clg/placement-career-ai/models/placement_model.pkl).

---

## 15. MODEL EXPLAINABILITY

### 15.1 Global Feature Importance
Because numerical inputs were standardized ($\mu=0, \sigma=1$) while binary flags entered as $[0, 1]$, the fitted logistic coefficients ($\beta_j$) directly indicate effect size on the log-odds of placement:
$$\Delta \ln\left(\frac{P}{1-P}\right) = \beta_j \cdot \Delta x_j \quad \iff \quad \text{Odds Ratio} = e^{\beta_j}$$

| Rank | Feature | Coefficient ($\beta$) | Absolute Importance ($|\beta|$) | Odds Ratio ($e^\beta$) | Directional Impact |
|---|---|---|---|---|---|
| 1 | **PlacementTraining** | +0.9053 | **0.9053** | **2.47x** | Positive (+) |
| 2 | **ExtracurricularActivities** | +0.7536 | **0.7536** | **2.12x** | Positive (+) |
| 3 | **AptitudeTestScore** | +0.5638 | **0.5638** | **1.76x** | Positive (+) |
| 4 | **SSC_Marks** | +0.2901 | **0.2901** | **1.34x** | Positive (+) |
| 5 | **SoftSkillsRating** | +0.2658 | **0.2658** | **1.30x** | Positive (+) |
| 6 | **HSC_Marks** | +0.2466 | **0.2466** | **1.28x** | Positive (+) |
| 7 | **CGPA** | +0.2432 | **0.2432** | **1.28x** | Positive (+) |
| 8 | **Projects** | +0.2206 | **0.2206** | **1.25x** | Positive (+) |
| 9 | **Workshops_Certifications** | +0.1217 | **0.1217** | **1.13x** | Positive (+) |
| 10 | **Internships** | -0.0057 | **0.0057** | **0.99x** | Negligible ($\approx 0$) |
*Model Base Intercept ($\beta_0$):* `-1.3989`.

### 15.2 Association vs. Causation Disclaimer
A fundamental principle of the system is that **correlation does not prove real-world causality**. While `PlacementTraining` carries the highest coefficient ($\beta = +0.9053$, $2.47\times$ odds multiplier), this reflects statistical association within the recruitment distribution—motivated, proactive candidates naturally enroll in placement training and also perform better in interviews. The application explicitly labels these outputs as *"Model contribution, not causation"*.

---

## 16. LIVE APTITUDE ASSESSMENT MODULE

To assess real-time problem solving independently of historical records, a dedicated cognitive testing module was implemented in [`utils/aptitude_assessment.py`](file:///e:/clg/placement-career-ai/utils/aptitude_assessment.py).

- **Question Bank:** 80 multiple-choice questions (20 each across 4 categories) defined in [`data/aptitude_questions.py`](file:///e:/clg/placement-career-ai/data/aptitude_questions.py).
- **Quota per Assessment:** Exactly **15 randomized questions**:
  - Quantitative Aptitude: **4 questions**
  - Logical Reasoning: **4 questions**
  - Verbal Ability: **4 questions**
  - Data Interpretation: **3 questions**
- **Evaluation Rubric:**
  - Scoring: 1 mark per correct answer ($0 \text{ to } 15$, converted to percentage).
  - Diagnostic Threshold: $\ge 70.0\%$ denotes **Strong Proficiency**; $< 70.0\%$ flags an **Area for Improvement**.
- **Architectural Boundary:** The live assessment score is strictly isolated from the historical `AptitudeTestScore` feature utilized by the tabular ML model.

---

## 17. LIVE TECHNICAL ASSESSMENT MODULE

Implemented in [`utils/technical_assessment.py`](file:///e:/clg/placement-career-ai/utils/technical_assessment.py), this module evaluates engineering concepts across IT and Core disciplines.

- **Question Bank:** 127 multiple-choice questions defined in [`data/technical_questions.py`](file:///e:/clg/placement-career-ai/data/technical_questions.py):
  - **IT Domain (63 questions):** Programming (9), DSA (9), OOP (9), DBMS (9), SQL (9), OS (9), Computer Networks (9).
  - **Core Domain (64 questions):** Digital Electronics (8), Analog Electronics (8), Microprocessors (8), Microcontrollers (8), Communication Systems (8), Signals & Systems (8), Electronic Devices (8), Embedded Systems (8).
- **Assessment Modes:**
  1. **IT Mode:** Exactly 15 IT questions distributed across the 7 IT topics.
  2. **Core Mode:** Exactly 15 Core questions distributed across the 8 Core topics.
  3. **Both Mode:** Exactly **8 IT questions + 7 Core questions** for dual-competency evaluation.
- **Evaluation:** Evaluates overall percentage, domain-level scores, topic-level performance, and applies the 70% mastery cutoff.

---

## 18. CAREER RECOMMENDATION SYSTEM

Implemented in [`utils/career_recommendation.py`](file:///e:/clg/placement-career-ai/utils/career_recommendation.py), the Career Recommendation Engine is a deterministic rule-based framework evaluating **12 defined career paths**:

### 18.1 Career Taxonomy
1. **Software Developer** (IT): Programming, DSA, OOP, OS
2. **Frontend Developer** (IT): Programming, OOP, Networks
3. **Backend Developer** (IT): Programming, OOP, DBMS, SQL
4. **Full Stack Developer** (IT): Programming, OOP, DBMS, SQL, Networks
5. **Data Analyst** (IT): Programming, DBMS, SQL
6. **Data Scientist** (IT): Programming, DSA, DBMS, SQL
7. **ML Engineer** (IT): Programming, DSA, DBMS, OS
8. **DevOps Engineer** (IT): Programming, OS, Networks
9. **QA Engineer** (IT): Programming, OOP, DBMS
10. **Cloud Engineer** (IT): Networks, OS, DBMS
11. **Cybersecurity Analyst** (IT): Networks, OS, Programming
12. **Embedded Engineer** (Core): Embedded Systems, Microcontrollers, Digital Electronics, Microprocessors, Devices

### 18.2 Mathematical Formulation
For each eligible role $R$, the overall **Match Score** $S(R) \in [0, 100]$ is computed as:
$$S(R) = 0.50 \cdot T(R) + 0.25 \cdot A(R) + 0.25 \cdot P$$
Where:
- **Technical Match $T(R)$:** The average percentage score achieved in the specific technical topics designated as critical for role $R$.
- **Aptitude Match $A(R)$:** A weighted combination of role-preferred aptitude categories ($70\%$) and overall cognitive score ($30\%$).
- **Placement Readiness $P$:** Calibrated model placement probability ($\hat{p} \times 100$).

### 18.3 Classification Tiers & Remediation
- **$\ge 80.0\%$:** *Strong Match*
- **$65.0\% - 79.9\%$:** *Good Match*
- **$50.0\% - 64.9\%$:** *Moderate Match*
- **$< 50.0\%$:** *Weak Match*
- **Skill Gaps:** Any role-critical topic where the candidate scored below 70% (or unassessed prerequisites) is flagged with specific actionable learning recommendations.

---

## 19. STREAMLIT APPLICATION ARCHITECTURE

The user interface ([`app.py`](file:///e:/clg/placement-career-ai/app.py)) is implemented as a cohesive single-page application avoiding multi-page session resets:

1. **Sidebar Navigation (`st.sidebar.radio`):** Routes between 5 unified views (`🏠 Home`, `📊 Placement Prediction`, `🧠 Aptitude Assessment`, `💻 Technical Assessment`, `🚀 Career Recommendation`).
2. **Session State Persistence (`st.session_state`):** Caches 10 core variables (`placement_result`, `aptitude_questions`, `aptitude_result`, `technical_questions`, `technical_result`, etc.), ensuring assessment state and predictions persist indefinitely across view switches.
3. **Reactive Visualizations:** Real-time generation of local logit contribution bar charts via Matplotlib with dynamic positive (green) and negative (red) color coding.
4. **Prerequisite Gating:** Restricts access to the Career Recommendation dashboard until all three preliminary analytical stages are completed, preventing runtime exceptions.

---

## 20. TESTING AND VALIDATION

The application was validated across a comprehensive multi-tier testing protocol:

### 20.1 Automated Test Suite
- **Unit Tests:** **50 / 50 PASSED** in **0.027 seconds** via Python `unittest`:
  - `tests/test_aptitude_assessment.py`: 10/10 Passed (Question schema, quotas, scoring, 70% threshold).
  - `tests/test_technical_assessment.py`: 20/20 Passed (IT/Core/Both distribution, topic breakdown).
  - `tests/test_career_recommendation.py`: 20/20 Passed (Scoring bounds, domain filtering, synthetic profiles A, B, C).

### 20.2 Programmatic & Manual UI Validation
- **Syntax Compilation:** `python -m py_compile app.py` executed with return code 0.
- **Server Health:** `http://localhost:8501/_stcore/health` returned HTTP 200 OK.
- **AppTest View Simulation:** Simulated programmatic user navigation across all 5 views with 0 runtime exceptions.
- **Functional Journey Testing:** Verified all 10 scenarios (Home, Placement Prediction, Explainability Chart, Aptitude Quota, Technical IT/Core/Both, Career Unlocking, Prerequisite Blocking).
- **UX Lifecycle Finding:** Verified that submitted results and generated question sets persist permanently across navigation tabs. Noted a minor Streamlit UX limitation where unsubmitted radio-button clicks inside an active form reset to empty if the user leaves the tab before clicking "Submit". This does not affect submitted results or core computation.

---

## 21. RESULTS AND DISCUSSION

The experimental results validate the efficacy of combining empirical machine learning with diagnostic assessments:
1. **Predictive Reliability:** Tuned Logistic Regression delivers balanced, dependable classification ($F1 = 0.7762$, $ROC-AUC = 0.8855$). The high recall ($81.23\%$) ensures that candidates with viable placement prospects are rarely overlooked.
2. **Explainability Impact:** Decomposing logit contributions provides concrete transparency. For example, a student with high CGPA (8.5) but no placement training can immediately observe how the lack of training lowers their placement log-odds, motivating participation.
3. **Decoupled Assessment Value:** Providing independent aptitude and technical testing ensures that students with modest past academic records can demonstrate current technical competence, directly boosting their career match scores.

---

## 22. SYSTEM LIMITATIONS

To maintain technical and scientific integrity, the following limitations are documented:
1. **Distributional Dependency:** The machine learning model is trained on a benchmark campus recruitment dataset; predictions are most reliable when student inputs conform to the training distribution ($CGPA \in [6.5, 9.1]$, Marks $\in [50, 90]$).
2. **Non-Causal Statistical Association:** Feature importance reflects observational correlation within recruitment data, not guaranteed real-world causality.
3. **Fixed Rule-Based Career Weights:** The 50/25/25 weighting formula is a deterministic institutional heuristic and does not account for variable corporate hiring weightings across specific niche recruiters.
4. **No External Job-Market Tracking:** The system does not ingest live real-time job postings or scrape external job boards.
5. **Stateless Deployment:** Data is held within active session state memory and is cleared upon browser session termination (no permanent database persistence).

---

## 23. FUTURE ENHANCEMENTS

1. **Multi-Institutional Dataset Expansion:** Expanding training data across diverse tiers of engineering colleges, polytechnics, and regional universities to enhance cross-demographic generalization.
2. **Dynamic Company-Specific Match Weights:** Allowing students or placement officers to adjust weighting profiles based on specific target recruiters (e.g., product companies weighting technical skills at 70%, service companies weighting aptitude at 40%).
3. **Longitudinal Profile Tracking:** Implementing secure, encrypted database persistence (e.g., PostgreSQL) allowing students to track progress over consecutive semesters.
4. **Adaptive Assessment Testing:** Integrating Computerized Adaptive Testing (CAT) based on Item Response Theory (IRT) to adjust question difficulty dynamically.
5. **Cloud Containerization:** Packaging the application into a Docker container for deployment to institutional cloud infrastructure (e.g., AWS ECS, GCP Cloud Run, or Kubernetes).

---

## 24. CONCLUSION

This project successfully designs and validates an interpretable, integrated **Machine Learning-Based Placement Prediction and Career Recommendation System**. By uniting a rigorously tuned Logistic Regression model ($F1 = 0.7762$, $ROC-AUC = 0.8855$) with real-time cognitive and multi-track technical diagnostics, the platform addresses the opacity and fragmentation of traditional placement counseling. Global and local feature contributions provide transparent explanations, while the deterministic 50/25/25 Career Recommendation Engine delivers tailored role rankings and actionable remediation for skill deficits. Validated by 50 automated tests and a production-ready Streamlit interface, the system represents an objective, mathematically sound tool for engineering students and academic placement cells.
