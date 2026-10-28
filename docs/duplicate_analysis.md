# Investigation Report: Duplicate Rows Analysis

## 1. Executive Summary
An exhaustive investigation of the duplicate rows in `data/raw/campus_recruitment.csv` was conducted.

- **Total Dataset Size:** 10,000 rows
- **Completely Identical Redundant Rows (`df.duplicated()`):** 72 rows
- **Total Rows Involved in Duplicate Groups (`keep=False`):** 138 rows
- **Unique Duplicate Patterns:** 66 unique patterns
- **Target Distribution of Duplicates:** **97.10% Placed** (134 rows) vs **2.90% NotPlaced** (4 rows)
- **Primary Finding:** The duplicates are **not** random natural student collisions. They are clustered at the extreme upper-tail ceiling of performance metrics (max internships, max projects, max aptitude scores), and 28 duplicate patterns were found to cross-leak across the original upstream train, validation, and test splits.
- **Final Recommendation:** **B. Remove exact duplicates** (deduplicate dataset to 9,928 unique rows during preprocessing).

---

## 2. Duplicate Breakdown & Quantities

| Metric | Count | Percentage of Dataset |
|---|---|---|
| Total Rows | 10,000 | 100.0% |
| Unique Rows | 9,928 | 99.28% |
| Extra Duplicate Rows (`keep='first'`) | 72 | 0.72% |
| Total Rows in Duplicate Groups (`keep=False`) | 138 | 1.38% |
| Non-Duplicate Unique Rows | 9,862 | 98.62% |
| Unique Duplicate Patterns | 66 patterns | - |

### Repetition Frequency Breakdown
- **Patterns repeated 2 times:** 60 patterns ($60 \times 2 = 120$ rows)
- **Patterns repeated 3 times:** 6 patterns ($6 \times 3 = 18$ rows)
- **Total:** 66 unique patterns accounting for 138 rows (66 original + 72 redundant copies)

---

## 3. Top Most Repeated Duplicate Patterns

Below are the 6 patterns that appear with the maximum repetition count of **3**:

| # | CGPA | Internships | Projects | Workshops/Cert | Aptitude | SoftSkills | ExtraCurr | Training | SSC | HSC | Target | Frequency |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 8.5 | 2 | 3 | 3 | 90 | 4.8 | Yes | Yes | 88 | 87 | **Placed** | **3** |
| 2 | 8.2 | 2 | 3 | 3 | 90 | 4.8 | Yes | Yes | 77 | 83 | **Placed** | **3** |
| 3 | 8.5 | 2 | 3 | 3 | 90 | 4.8 | Yes | Yes | 89 | 88 | **Placed** | **3** |
| 4 | 8.3 | 2 | 3 | 3 | 90 | 4.8 | Yes | Yes | 89 | 87 | **Placed** | **3** |
| 5 | 8.4 | 2 | 3 | 3 | 90 | 4.8 | Yes | Yes | 89 | 86 | **Placed** | **3** |
| 6 | 8.7 | 2 | 3 | 3 | 90 | 4.8 | Yes | Yes | 88 | 85 | **Placed** | **3** |

*Notice:* Every single 3-time repeated pattern is an ultra-high performer profile with **AptitudeTestScore = 90 (max)**, **SoftSkillsRating = 4.8 (max)**, **Projects = 3 (max)**, **Internships = 2 (max)**, **PlacementTraining = Yes**, and **Target = Placed**.

---

## 4. Target Distribution Comparison

| Cohort | Total Rows | Placed Count | Placed % | NotPlaced Count | NotPlaced % |
|---|---|---|---|---|---|
| **Full Raw Dataset** | 10,000 | 4,197 | **41.97%** | 5,803 | **58.03%** |
| **All Duplicate Rows (138)** | 138 | 134 | **97.10%** | 4 | **2.90%** |
| **Extra Redundant Copies (72)** | 72 | 70 | **97.22%** | 2 | **2.78%** |
| **Non-Duplicate Subset (9,862)** | 9,862 | 4,063 | **41.20%** | 5,799 | **58.80%** |
| **Deduplicated Dataset (9,928)** | 9,928 | 4,127 | **41.57%** | 5,801 | **58.43%** |

### Key Observation:
The duplicate rows are **heavily skewed toward `Placed` (97.10%)** compared to the general dataset population where `Placed` is only **41.97%**.

---

## 5. Statistical Profile: Duplicate Cohort vs Full Population

| Feature | Full Dataset Mean | Duplicate Subset Mean (138) | Dataset Max | Observation in Duplicates |
|---|---|---|---|---|
| `CGPA` | 7.70 | **8.25** | 9.1 | +0.55 above population mean |
| `Internships` | 1.05 | **1.93** | 2.0 | At near-maximum capacity |
| `Projects` | 2.03 | **2.94** | 3.0 | At near-maximum capacity |
| `Workshops/Certifications` | 1.01 | **1.88** | 3.0 | Nearly double population mean |
| `AptitudeTestScore` | 79.45 | **89.59** | 90.0 | Clustered directly at ceiling (90) |
| `SoftSkillsRating` | 4.32 | **4.78** | 4.8 | Clustered directly at ceiling (4.8) |
| `PlacementTraining` | 73.2% Yes | **100.0% Yes** | - | 138 out of 138 took training |
| `ExtracurricularActivities`| 58.5% Yes | **97.1% Yes** | - | 134 out of 138 active |
| `SSC_Marks` | 69.16 | **78.19** | 90.0 | +9.0 points above mean |
| `HSC_Marks` | 74.50 | **84.90** | 88.0 | +10.4 points above mean |

---

## 6. Origin & Legitimacy Assessment: Natural Collisions vs Accidental Artifacts

### Are these legitimate repeated student profiles?
**Conclusion: Highly unlikely.** They are almost certainly **accidental artifacts or synthetic sampling anomalies**.

### Supporting Evidence:
1. **Combinatorial Collision Probability:**
   With 10 features containing $27 \times 3 \times 4 \times 4 \times 31 \times 19 \times 2 \times 2 \times 36 \times 32 \approx 1.34 \times 10^9$ possible profile permutations, exact 10-feature matches across 10,000 independent students are statistically improbable unless features cluster around the mode.
2. **Anomaly in Collision Location:**
   If collisions were natural, they would occur around the distribution modes (e.g., CGPA $\approx 7.7$, Aptitude $\approx 79$, SSC $\approx 69$). Instead, collisions occur almost exclusively at the **extreme upper boundary** (Aptitude = 90, SoftSkills = 4.8, Projects = 3, Internships = 2).
3. **Cross-Split Contamination in Upstream Repository:**
   Investigating the original Hugging Face source splits revealed:
   - 43 duplicates existed within `train.csv`.
   - **28 duplicate patterns spanned across splits** (appearing simultaneously in `train.csv` and `validation.csv` or `test.csv`).
   This indicates that the source dataset creators either used duplicate augmentation on high-performing profiles or generated them via automated sampling without post-split deduplication.

---

## 7. Impact of Keeping vs Removing Duplicates on Model Training

### Potential Bias if KEPT:
- **Artificial Sample Weighting:** Repeating identical high-performing profiles 2 to 3 times gives those specific data points extra weight in loss functions (e.g. Cross-Entropy, Gini impurity, Mean Squared Error).
- **Data Leakage in Validation:** If the raw data is split into train and test sets, duplicate rows can land in both splits. The evaluation metrics (Accuracy, ROC-AUC) will be artificially inflated because the model will be evaluated on records it has memorized identically from training.
- **Distorted Decision Boundaries:** Boundary trees may create excessively granular terminal leaves specifically fitting these duplicated ceiling points.

### Impact if REMOVED:
- **Minimal Class Shift:** Deduplicating removes 70 `Placed` rows and 2 `NotPlaced` rows. The percentage of `Placed` shifts from 41.97% to 41.57% (a negligible shift of just 0.40%).
- **Guaranteed Independence:** Ensures that every training, validation, and test sample is distinct and independent.
- **Zero Evaluation Leakage:** Eliminates the risk of exact test-set memorization.

---

## 8. Final Recommendation

### **Recommendation: B. Remove exact duplicates**

**Rationale:**
1. Removing exact duplicates prior to train/test splitting guarantees data integrity, prevents cross-split data leakage, and avoids artificial sample re-weighting.
2. Option A (**Keep duplicates**) introduces data leakage risk and artificial weighting.
3. Option C (**Remove duplicates only from training split**) leaves duplicate profiles in the test/validation set, creating inconsistent evaluation criteria.
4. Pruning the 72 redundant copies reduces the dataset cleanly from 10,000 to **9,928 rows** without any loss of unique student information.
