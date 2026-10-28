# Career Recommendation Engine Specification & Evaluation Report

**Module:** Career Recommendation Engine (`utils/career_recommendation.py`)  
**Role Definitions:** `data/career_roles.py`  
**Evaluation Type:** Transparent Rule-Based Scoring, Skill-Gap Analysis, and Actionable Guidance  
**Unit Test Suite:** `tests/test_career_recommendation.py` (20/20 Passed)

---

## 1. System Overview & Architecture

The **Career Recommendation Engine** is a deterministic, rule-based matching and ranking framework. Unlike opaque "black-box" recommender models, this engine provides 100% explainable recommendations suitable for engineering placement viva defense.

The engine synthesizes three signals:
1. **Live Technical Assessment:** Assesses mastery of role-specific programming, software engineering, and hardware concepts.
2. **Live Aptitude Assessment:** Evaluates Quantitative Aptitude, Logical Reasoning, Verbal Ability, and Data Interpretation.
3. **ML Placement Probability:** Reflects overall academic and co-curricular placement readiness from the trained Logistic Regression model.

```
                           +-------------------------------------+
                           |      Student Input & Testing        |
                           +-------------------------------------+
                                  /            |            \
                                 /             |             \
            +-----------------------+   +---------------+   +-----------------------+
            |  Technical Assessment |   | Aptitude Test |   | Placement Model (ML)  |
            |     (IT / Core)       |   | (4 Categories)|   | (Historical Predictor)|
            +-----------------------+   +---------------+   +-----------------------+
                        |                       |                       |
                  Topic Mastery          Cognitive Ability      Placement Readiness
                     (0 - 100%)              (0 - 100%)              (0 - 100%)
                        |                       |                       |
                  Weight = 50%            Weight = 25%            Weight = 25%
                        \                       |                      /
                         \                      |                     /
                          +------------------------------------------+
                          |   Deterministic Scoring & Ranking Engine |
                          +------------------------------------------+
                                               |
                                     Top 3 Career Matches
                                    + Match Level Ratings
                                    + "Why Recommended" Rationale
                                    + Skill Gaps (< 70% threshold)
                                    + Actionable Learning Roadmap
```

---

## 2. Career Roles Taxonomy

Twelve industry-aligned career roles are defined across IT and Core engineering disciplines:

| # | Role | Domain | Core Focus Areas / Important Topics | Preferred Aptitude Strengths |
|---|---|---|---|---|
| 1 | **Software Developer** | IT | Programming, Data Structures & Algorithms, OOP, Operating Systems | Logical Reasoning, Quantitative Aptitude |
| 2 | **Frontend Developer** | IT | Programming, OOP, Computer Networks | Logical Reasoning, Verbal Ability |
| 3 | **Backend Developer** | IT | Programming, OOP, DBMS, SQL | Logical Reasoning, Quantitative Aptitude |
| 4 | **Full Stack Developer** | IT | Programming, OOP, DBMS, SQL, Computer Networks | Logical Reasoning, Quantitative Aptitude |
| 5 | **Data Analyst** | IT | Programming, DBMS, SQL | Data Interpretation, Quantitative Aptitude |
| 6 | **Data Scientist** | IT | Programming, Data Structures & Algorithms, DBMS, SQL | Quantitative Aptitude, Data Interpretation |
| 7 | **ML Engineer** | IT | Programming, Data Structures & Algorithms, DBMS, Operating Systems | Quantitative Aptitude, Logical Reasoning |
| 8 | **DevOps Engineer** | IT | Programming, Operating Systems, Computer Networks | Logical Reasoning, Quantitative Aptitude |
| 9 | **QA Engineer** | IT | Programming, OOP, DBMS | Logical Reasoning, Verbal Ability |
| 10 | **Cloud Engineer** | IT | Computer Networks, Operating Systems, DBMS | Logical Reasoning, Quantitative Aptitude |
| 11 | **Cybersecurity Analyst** | IT | Computer Networks, Operating Systems, Programming | Logical Reasoning, Verbal Ability |
| 12 | **Embedded Engineer** | Core | Embedded Systems, Microcontrollers, Digital Electronics, Microprocessors, Electronic Devices | Logical Reasoning, Quantitative Aptitude |

---

## 3. Mathematical Scoring Methodology

For each candidate role $R$, the overall **Match Score** $S(R) \in [0, 100]$ is computed as:

$$S(R) = w_{\text{tech}} \cdot T(R) + w_{\text{apt}} \cdot A(R) + w_{\text{place}} \cdot P$$

Where:
- $w_{\text{tech}} = 0.50$ (50% Technical Weight)
- $w_{\text{apt}} = 0.25$ (25% Aptitude Weight)
- $w_{\text{place}} = 0.25$ (25% Placement Readiness Weight)

### A. Technical Match $T(R)$
Evaluates the student's average score across the specific technical topics designated as important for role $R$:

$$T(R) = \frac{1}{|K_R|} \sum_{t \in K_R} \text{Score}(t)$$

Where $K_R$ is the set of tested topics relevant to role $R$. If none of the specific topics were directly tested, the engine falls back to the student's domain-level average.

### B. Aptitude Match $A(R)$
Blends preferred aptitude competency with general cognitive readiness:

$$A(R) = 0.70 \times \left(\frac{1}{|C_R|} \sum_{c \in C_R} \text{Score}(c)\right) + 0.30 \times \text{Score}_{\text{overall}}$$

Where $C_R$ is the set of aptitude categories preferred by role $R$.

### C. Placement Readiness $P$
The calibrated placement probability output from the trained Logistic Regression model, scaled to $[0, 100]$:

$$P = \hat{p}_{\text{placement}} \times 100$$

---

## 4. Match Level Classification

Scores are categorized into intuitive readiness tiers:

| Score Range | Match Level | Interpretation |
|---|---|---|
| **$80.0\% - 100.0\%$** | **Strong Match** | Exceptional alignment; student possesses strong foundational competency. |
| **$65.0\% - 79.9\%$** | **Good Match** | High potential; student meets core prerequisites with minor gaps. |
| **$50.0\% - 64.9\%$** | **Moderate Match** | Viable career track requiring focused upskilling in key areas. |
| **Below $50.0\%$** | **Weak Match** | Substantial prerequisites missing; significant foundational study needed. |

---

## 5. Skill-Gap Identification & Actionable Guidance

The engine implements a strict **70% mastery threshold**:
1. Any topic relevant to the role where the student scored **$< 70\%$** is flagged as a **Skill Gap**.
2. Untested prerequisite topics are flagged for **Verification & Self-Assessment**.
3. For every identified gap, the engine maps a concrete, actionable learning recommendation (e.g., LeetCode practice, ACID transaction review, RTOS study, or OSI protocol revision).

---

## 6. Synthetic Student Evaluations

### Profile A: High IT Specialist
- **Inputs:** Placement Probability = 0.90, Aptitude = 85.0% (Quant: 90%, Logical: 85%), IT Technical = 88.0% (Prog: 95%, DSA: 90%, OOP: 90%, DBMS: 85%, OS: 80%), Core Technical = 27.5%.
- **Domain Selection:** `Both`
- **Output:**
  1. **Frontend Developer:** 89.56% (Strong Match) | Tech: 92.5%, Apt: 83.5%, Placement: 90.0%
  2. **Backend Developer:** 89.19% (Strong Match) | Tech: 90.0%, Apt: 86.8%, Placement: 90.0%
  3. **Full Stack Developer:** 89.19% (Strong Match) | Tech: 90.0%, Apt: 86.8%, Placement: 90.0%
- **Observations:** IT roles dominate the top ranks; Core roles are filtered to the bottom due to weak hardware scores.

### Profile B: Strong Core / Embedded Specialist
- **Inputs:** Placement Probability = 0.90, Aptitude = 85.0%, Core Technical = 90.0% (Digital: 95%, $\mu$P: 90%, $\mu$C: 85%, Embedded: 90%), IT Technical = 25.0%.
- **Domain Selection:** `Both`
- **Output:**
  1. **Embedded Engineer:** 89.19% (Strong Match) | Tech: 90.0%, Apt: 86.8%, Placement: 90.0%
  2. **Software Developer:** 59.19% (Moderate Match) | Tech: 30.0%, Apt: 86.8%, Placement: 90.0%
  3. **DevOps Engineer:** 59.19% (Moderate Match) | Tech: 30.0%, Apt: 86.8%, Placement: 90.0%
- **Observations:** Embedded Engineer ranked #1 with an 89.19% match score, while general software roles fell to Moderate Match due to low programming and DBMS scores.

### Profile C: Balanced / Mixed Performer
- **Inputs:** Placement Probability = 0.60, Aptitude = 60.0%, Technical = 75.0% across both IT and Core topics.
- **Domain Selection:** `Both`
- **Output:**
  1. **Software Developer:** 67.94% (Good Match) | Tech: 75.0%, Apt: 61.8%, Placement: 60.0%
  2. **Backend Developer:** 67.94% (Good Match) | Tech: 75.0%, Apt: 61.8%, Placement: 60.0%
  3. **Full Stack Developer:** 67.94% (Good Match) | Tech: 75.0%, Apt: 61.8%, Placement: 60.0%
- **Observations:** Consistently placed in the "Good Match" band across diverse tracks, reflecting solid baseline skills across domains.

---

## 7. Verification & Test Suite Summary

The unit test suite validates scoring accuracy, edge cases, domain filtering, and data contracts:

```
tests/test_career_recommendation.py:
  [PASS] Career role definitions load successfully
  [PASS] All 12 specified roles exist
  [PASS] Role definitions contain all required fields
  [PASS] IT filtering works and excludes Core roles
  [PASS] Core filtering works and excludes IT roles
  [PASS] Both mode evaluates all roles across domains
  [PASS] Recommendation returns at most 3 roles
  [PASS] Match scores remain strictly within [0, 100]
  [PASS] Match levels follow standard thresholds
  [PASS] Technical match increases with higher topic score
  [PASS] Aptitude match responds to aptitude assessment percentage
  [PASS] Placement readiness responds to model probability
  [PASS] Relevant topics below 70% become skill gaps
  [PASS] Unrelated topics are not included in a role's skill gaps
  [PASS] High-performing student receives Strong Match level
  [PASS] Low-performing student receives clear skill gaps and guidance
  [PASS] Invalid domain input raises descriptive ValueError
  [PASS] Synthetic Student A (High IT)
  [PASS] Synthetic Student B (Strong Core)
  [PASS] Synthetic Student C (Mixed IT + Core)

Total Project Tests Executed: 50
Total Passed: 50 (10 Aptitude + 20 Technical + 20 Career Recommendation)
Total Execution Time: < 0.010s
```
