# Machine Learning-Based Placement Prediction and Career Recommendation System

A standalone Python and Streamlit application for placement prediction, career recommendation, and model explainability.

## Project Scope
This application is designed as a standalone machine learning tool. It does not require or use an external database or backend server.

### Core Features
1. **Student Input Form**: Capture academic metrics, technical skills, projects, and interview preparation details.
2. **ML-Based Placement Prediction**: Predict placement outcomes using trained machine learning models.
3. **Placement Probability**: Display confidence and probability scores for placement likelihood.
4. **Career Recommendation**: Suggest suitable career paths aligned with student profiles.
5. **Career Match Scores**: Quantify role alignment across diverse domains (e.g., Software Engineering, Data Science).
6. **Skill-Gap Analysis**: Identify missing or weak skills required for recommended career paths.
7. **Personalized Improvement Recommendations**: Provide actionable suggestions to improve placement chances.
8. **Model Explanation**: Visual feature attribution and explainability powered by SHAP.

### Explicitly Excluded (Out of Scope)
- No user accounts or authentication (login/register)
- No user storage or profile persistence
- No prediction history logging
- No admin panel or role-based access
- No databases (No SQLite, PostgreSQL, etc.)
- No external frameworks (No React, Node.js, Express, FastAPI)

---

## Tech Stack
- **Language:** Python (3.12)
- **UI & Web Framework:** Streamlit
- **Data Manipulation & Math:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **Model Explainability:** SHAP

---

## Project Structure
```
placement-career-ai/
│
├── app.py
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── ml/
├── pages/
├── utils/
├── notebooks/
├── requirements.txt
└── README.md
```

---

## Setup & Running
1. Activate the Python 3.12 virtual environment:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
2. Install dependencies (if not already installed):
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```powershell
   streamlit run app.py
   ```
