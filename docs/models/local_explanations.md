# Local Explainability Report for Example Students

**Model Pipeline:** `models/placement_model.pkl` (Logistic Regression)  
**Methodology:** Exact decomposition of the log-odds decision boundary ($z = \beta_0 + \sum_{j=1}^p \beta_j x_j'$), converted to probability via the sigmoid link function:
$$P(\text{Placed}) = \frac{1}{1 + e^{-z}}$$

---

### Student 1 (High Performer)
- **Predicted Placement Status:** **Placed (1)**
- **Placement Probability:** **91.88%** *(Not Placed: 8.12%)*
- **Final Log-Odds ($z$):** `2.4267` *(Base Intercept: `-1.3989`)*

#### Profile Summary:
- CGPA: `8.5` | Internships: `2` | Projects: `3` | Certifications: `2`
- Aptitude: `88` | Soft Skills: `4.6` | SSC: `85%` | HSC: `84%`
- Extracurricular Activities: `Yes` | Placement Training: `Yes`

#### Top Positive Contributors (Pushed Probability Up):
| Feature | Raw Value | Scaled Value ($x'$) | Coefficient ($\beta$) | Logit Contribution ($\beta \cdot x'$) |
|---|---|---|---|---|
| **PlacementTraining** | 1.0 | +1.00 | +0.9053 | **+0.9053** |
| **ExtracurricularActivities** | 1.0 | +1.00 | +0.7536 | **+0.7536** |
| **AptitudeTestScore** | 88.0 | +1.06 | +0.5638 | **+0.5972** |
| **SSC_Marks** | 85.0 | +1.53 | +0.2901 | **+0.4426** |
| **CGPA** | 8.5 | +1.26 | +0.2432 | **+0.3063** |
| **HSC_Marks** | 84.0 | +1.08 | +0.2466 | **+0.2652** |
| **Projects** | 3.0 | +1.13 | +0.2206 | **+0.2494** |
| **SoftSkillsRating** | 4.6 | +0.68 | +0.2658 | **+0.1806** |
| **Workshops_Certifications** | 2.0 | +1.10 | +0.1217 | **+0.1338** |

#### Top Negative Contributors (Pulled Probability Down):
| Feature | Raw Value | Scaled Value ($x'$) | Coefficient ($\beta$) | Logit Contribution ($\beta \cdot x'$) |
|---|---|---|---|---|
| **Internships** | 2.0 | +1.44 | -0.0057 | **-0.0082** |

---

### Student 2 (Average / Moderate)
- **Predicted Placement Status:** **NotPlaced (0)**
- **Placement Probability:** **18.99%** *(Not Placed: 81.01%)*
- **Final Log-Odds ($z$):** `-1.4506` *(Base Intercept: `-1.3989`)*

#### Profile Summary:
- CGPA: `7.4` | Internships: `1` | Projects: `1` | Certifications: `1`
- Aptitude: `76` | Soft Skills: `4.1` | SSC: `66%` | HSC: `70%`
- Extracurricular Activities: `No` | Placement Training: `Yes`

#### Top Positive Contributors (Pushed Probability Up):
| Feature | Raw Value | Scaled Value ($x'$) | Coefficient ($\beta$) | Logit Contribution ($\beta \cdot x'$) |
|---|---|---|---|---|
| **PlacementTraining** | 1.0 | +1.00 | +0.9053 | **+0.9053** |
| **Internships** | 1.0 | -0.06 | -0.0057 | **+0.0004** |

#### Top Negative Contributors (Pulled Probability Down):
| Feature | Raw Value | Scaled Value ($x'$) | Coefficient ($\beta$) | Logit Contribution ($\beta \cdot x'$) |
|---|---|---|---|---|
| **Projects** | 1.0 | -1.18 | +0.2206 | **-0.2595** |
| **AptitudeTestScore** | 76.0 | -0.41 | +0.5638 | **-0.2338** |
| **SoftSkillsRating** | 4.1 | -0.54 | +0.2658 | **-0.1427** |
| **HSC_Marks** | 70.0 | -0.50 | +0.2466 | **-0.1226** |
| **CGPA** | 7.4 | -0.46 | +0.2432 | **-0.1117** |
| **SSC_Marks** | 66.0 | -0.30 | +0.2901 | **-0.0861** |
| **Workshops_Certifications** | 1.0 | -0.01 | +0.1217 | **-0.0009** |

---

### Student 3 (Underprepared / Low)
- **Predicted Placement Status:** **NotPlaced (0)**
- **Placement Probability:** **0.61%** *(Not Placed: 99.39%)*
- **Final Log-Odds ($z$):** `-5.0914` *(Base Intercept: `-1.3989`)*

#### Profile Summary:
- CGPA: `6.6` | Internships: `0` | Projects: `0` | Certifications: `0`
- Aptitude: `62` | Soft Skills: `3.2` | SSC: `58%` | HSC: `60%`
- Extracurricular Activities: `No` | Placement Training: `No`

#### Top Positive Contributors (Pushed Probability Up):
| Feature | Raw Value | Scaled Value ($x'$) | Coefficient ($\beta$) | Logit Contribution ($\beta \cdot x'$) |
|---|---|---|---|---|
| **Internships** | 0.0 | -1.57 | -0.0057 | **+0.0089** |

#### Top Negative Contributors (Pulled Probability Down):
| Feature | Raw Value | Scaled Value ($x'$) | Coefficient ($\beta$) | Logit Contribution ($\beta \cdot x'$) |
|---|---|---|---|---|
| **AptitudeTestScore** | 62.0 | -2.13 | +0.5638 | **-1.2034** |
| **SoftSkillsRating** | 3.2 | -2.73 | +0.2658 | **-0.7245** |
| **Projects** | 0.0 | -2.33 | +0.2206 | **-0.5140** |
| **CGPA** | 6.6 | -1.71 | +0.2432 | **-0.4157** |
| **HSC_Marks** | 60.0 | -1.62 | +0.2466 | **-0.3996** |
| **SSC_Marks** | 58.0 | -1.06 | +0.2901 | **-0.3086** |
| **Workshops_Certifications** | 0.0 | -1.11 | +0.1217 | **-0.1356** |


---

## Technical Note on Local Explanations
1. **Scaled Values ($x'$):** Represents the student's deviation from the population mean in units of standard deviations for numerical features.
   - $x' > 0$: Student performed above average for this feature.
   - $x' < 0$: Student performed below average for this feature.
2. **Logit Contribution ($\beta \cdot x'$):**
   - For positive coefficients ($\beta > 0$), being above average ($x' > 0$) adds positively to the logit, increasing placement probability.
   - Being below average ($x' < 0$) produces a negative contribution, reducing placement probability.
   - Binary attributes (`ExtracurricularActivities`, `PlacementTraining`) directly add their coefficient weight when active ($x'=1$).
