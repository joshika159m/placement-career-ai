"""
Placement Prediction and Career Recommendation System
Simple, Professional, Global Student Career Assessment Web Application
"""

import os
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
import streamlit as st

# Import backend question & assessment utilities
from utils.aptitude_assessment import (
    select_assessment_questions,
    evaluate_assessment
)
from utils.technical_assessment import (
    select_technical_questions,
    evaluate_technical_assessment
)
from utils.career_recommendation import (
    recommend_careers,
    get_match_level,
    TOPIC_RECOMMENDATIONS
)
from utils.placement_scoring import calculate_weighted_placement_probability

# =============================================================================
# 1. PAGE CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title="Placement Prediction and Career Recommendation System",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom minimal CSS for clean, professional typography and layout (strictly no emojis)
st.markdown("""
<style>
    /* Hide Streamlit default sidebar and header decoration */
    [data-testid="stSidebar"] {
        display: none;
    }
    .main .block-container {
        max-width: 760px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }
    .stButton button {
        border-radius: 6px;
        font-weight: 500;
        padding: 0.5rem 1.25rem;
    }
    .badge-tag {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 4px;
        background-color: #f1f3f4;
        font-size: 13px;
        font-weight: 500;
        color: #3c4043;
        margin-right: 6px;
        margin-bottom: 6px;
        border: 1px solid #dadce0;
    }
</style>
""", unsafe_allow_html=True)

BASE_DIR = Path(__file__).resolve().parent
REDUCED_MODEL_PATH = BASE_DIR / "models" / "placement_model_reduced.pkl"


@st.cache_resource
def load_reduced_model():
    """Loads the validated 5-feature placement prediction model (for academic research & comparisons)."""
    if not REDUCED_MODEL_PATH.exists():
        return None
    try:
        return joblib.load(REDUCED_MODEL_PATH)
    except Exception as e:
        st.error(f"Failed to load placement model: {e}")
        return None


# =============================================================================
# 2. SESSION STATE MANAGEMENT
# =============================================================================

def init_session_state():
    """Initializes empty state for student session."""
    defaults = {
        "current_step": "student_info",
        # Student Info (initially empty)
        "student_name": "",
        "student_dept": "Select Department",
        "other_dept": "",
        "student_year": "Select Year",
        # Academic Profile (initially empty)
        "academic_cgpa": None,
        "academic_aptitude": None,
        "academic_soft_skills": None,
        "academic_ssc": None,
        "academic_hsc": None,
        # Weighted Placement Probability & Historical ML benchmark
        "placement_prob": None,
        "historical_ml_prob": None,
        # Aptitude Assessment
        "aptitude_questions": None,
        "aptitude_answers": {},
        "aptitude_q_idx": 0,
        "aptitude_result": None,
        # Technical Assessment
        "technical_domain": "Both",
        "technical_questions": None,
        "technical_answers": {},
        "tech_q_idx": 0,
        "technical_result": None,
        # Skill Assessment (Familiarity / Self-Rating)
        "skill_assessment_selections": [],
        "skill_levels": {},
        # Areas of Interest
        "interests": [],
        # Career Recommendation
        "career_result": None
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


init_session_state()

# Assessable Industry Skill Areas for Step 5
SKILL_ASSESSMENT_AREAS = [
    "Programming",
    "Web Development",
    "React / Frontend",
    "Backend Development",
    "Cloud Computing",
    "DevOps",
    "Artificial Intelligence",
    "Machine Learning",
    "Data Science",
    "Cybersecurity",
    "Data Analytics",
    "Embedded Systems",
    "VLSI / Semiconductor"
]

# 15 Standardized Areas of Interest for Step 6
AREAS_OF_INTEREST = [
    "Software Development",
    "Web Development",
    "UI/UX",
    "Cloud Computing",
    "DevOps",
    "Artificial Intelligence",
    "Machine Learning",
    "Data Science & AI",
    "Data Analytics",
    "Cybersecurity",
    "Networking",
    "Testing / QA",
    "Embedded Systems",
    "Electronics & Communication",
    "VLSI / Semiconductor"
]


# Plain text progress indicator (strictly no emojis)
def render_progress_bar(current_stage_idx: int):
    stages = ["About You", "Academics", "Aptitude", "Technical", "Skills", "Interests", "Results"]
    items = []
    for idx, stage in enumerate(stages):
        if idx == current_stage_idx:
            items.append(f"<span style='font-weight: 700; color: #1a73e8; border-bottom: 2px solid #1a73e8; padding-bottom: 2px;'>{stage}</span>")
        elif idx < current_stage_idx:
            items.append(f"<span style='color: #2e7d32; font-weight: 500;'>{stage}</span>")
        else:
            items.append(f"<span style='color: #888888;'>{stage}</span>")
    separator = " <span style='color: #aaaaaa; margin: 0 4px;'>→</span> "
    progress_html = f"<div style='text-align: center; font-size: 0.88rem; margin-bottom: 1.25rem; line-height: 1.8;'>{separator.join(items)}</div>"
    st.markdown(progress_html, unsafe_allow_html=True)
    st.markdown("<hr style='margin-top: 0.2rem; margin-bottom: 1.5rem; border: none; border-top: 1px solid #e0e0e0;'/>", unsafe_allow_html=True)


# =============================================================================
# 3. STEP 1: WELCOME / STUDENT INFORMATION
# =============================================================================

if st.session_state.current_step == "student_info":
    render_progress_bar(0)
    st.markdown("## Let's Assess Your Career Readiness")
    st.markdown("Complete a short assessment to understand your placement readiness, technical strengths, career interests, and areas for improvement.")

    with st.container(border=True):
        full_name = st.text_input(
            "Full Name *",
            value=st.session_state.student_name,
            placeholder="e.g., Alex Morgan"
        )

        dept_options = [
            "Select Department",
            "Computer Science / IT",
            "Electronics & Communication",
            "Electrical / Electronics",
            "Mechanical",
            "Civil",
            "Other Engineering / Technology"
        ]
        curr_dept_idx = dept_options.index(st.session_state.student_dept) if st.session_state.student_dept in dept_options else 0
        department = st.selectbox(
            "Department / Branch *",
            options=dept_options,
            index=curr_dept_idx
        )

        other_dept_val = ""
        if department == "Other Engineering / Technology":
            other_dept_val = st.text_input(
                "Specify your department / field *",
                value=st.session_state.other_dept,
                placeholder="e.g., Biotechnology, Chemical Engineering, etc."
            )

        year_options = [
            "Select Year",
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year",
            "Graduated"
        ]
        curr_year_idx = year_options.index(st.session_state.student_year) if st.session_state.student_year in year_options else 0
        year_of_study = st.selectbox(
            "Year of Study *",
            options=year_options,
            index=curr_year_idx
        )

    if st.button("Continue to Academic Profile", type="primary", use_container_width=True):
        if not full_name.strip():
            st.error("Please enter your full name.")
        elif department == "Select Department":
            st.error("Please select your department.")
        elif department == "Other Engineering / Technology" and not other_dept_val.strip():
            st.error("Please specify your department / field.")
        elif year_of_study == "Select Year":
            st.error("Please select your year of study.")
        else:
            st.session_state.student_name = full_name.strip()
            st.session_state.student_dept = department
            st.session_state.other_dept = other_dept_val.strip() if department == "Other Engineering / Technology" else ""
            st.session_state.student_year = year_of_study
            st.session_state.current_step = "academic"
            st.rerun()


# =============================================================================
# 4. STEP 2: ACADEMIC PROFILE
# =============================================================================

elif st.session_state.current_step == "academic":
    render_progress_bar(1)
    st.markdown("## Your Academic Profile")
    st.markdown("Enter your academic details. These indicators provide the academic foundation for your placement estimate.")

    with st.container(border=True):
        cgpa_val = st.number_input(
            "College CGPA (out of 10) *",
            min_value=0.0,
            max_value=10.0,
            value=st.session_state.academic_cgpa,
            step=0.01,
            placeholder="e.g., 7.85"
        )
        st.caption("Training range: 6.5 – 9.1 (recorded for academic profile documentation)")

        apt_val = st.number_input(
            "Historical Aptitude Screening Score (0–100) *",
            min_value=0.0,
            max_value=100.0,
            value=st.session_state.academic_aptitude,
            step=1.0,
            placeholder="e.g., 75"
        )
        st.caption("Training range: 60 – 90")

        soft_val = st.number_input(
            "Soft Skills Rating (1.0 to 5.0) *",
            min_value=1.0,
            max_value=5.0,
            value=st.session_state.academic_soft_skills,
            step=0.1,
            placeholder="e.g., 4.0"
        )
        st.caption("Training range: 3.0 – 4.8")

        ssc_val = st.number_input(
            "10th Standard (SSC) Marks (%) *",
            min_value=0.0,
            max_value=100.0,
            value=st.session_state.academic_ssc,
            step=0.1,
            placeholder="e.g., 85.0"
        )
        st.caption("Training range: 55% – 90% (contributes 15% to final placement probability)")

        hsc_val = st.number_input(
            "12th Standard (HSC) Marks (%) *",
            min_value=0.0,
            max_value=100.0,
            value=st.session_state.academic_hsc,
            step=0.1,
            placeholder="e.g., 82.5"
        )
        st.caption("Training range: 57% – 88% (contributes 15% to final placement probability)")

    col_nav1, col_nav2 = st.columns([1, 2])
    with col_nav1:
        if st.button("Back"):
            st.session_state.current_step = "student_info"
            st.rerun()
    with col_nav2:
        if st.button("Continue to Aptitude Assessment", type="primary", use_container_width=True):
            if cgpa_val is None or apt_val is None or soft_val is None or ssc_val is None or hsc_val is None:
                st.error("Please fill in all 5 academic fields before continuing.")
            else:
                # Validate against model training distribution ranges
                range_warnings = []
                if not (6.5 <= cgpa_val <= 9.1):
                    range_warnings.append(f"CGPA ({cgpa_val}) is outside the model training range (6.5 – 9.1). Please enter a value between 6.5 and 9.1.")
                if not (60.0 <= apt_val <= 90.0):
                    range_warnings.append(f"Historical Aptitude Score ({apt_val}) is outside the model training range (60 – 90). Please enter a value between 60 and 90.")
                if not (3.0 <= soft_val <= 4.8):
                    range_warnings.append(f"Soft Skills Rating ({soft_val}) is outside the model training range (3.0 – 4.8). Please enter a value between 3.0 and 4.8.")
                if not (55.0 <= ssc_val <= 90.0):
                    range_warnings.append(f"SSC Marks ({ssc_val}%) is outside the model training range (55% – 90%). Please enter a value between 55% and 90%.")
                if not (57.0 <= hsc_val <= 88.0):
                    range_warnings.append(f"HSC Marks ({hsc_val}%) is outside the model training range (57% – 88%). Please enter a value between 57% and 88%.")

                if range_warnings:
                    for rw in range_warnings:
                        st.warning(rw)
                    st.error("Please enter valid values within the model training range to continue.")
                else:
                    # Save academic values
                    st.session_state.academic_cgpa = float(cgpa_val)
                    st.session_state.academic_aptitude = float(apt_val)
                    st.session_state.academic_soft_skills = float(soft_val)
                    st.session_state.academic_ssc = float(ssc_val)
                    st.session_state.academic_hsc = float(hsc_val)

                    # Compute historical ML prediction for research documentation (retained separately)
                    pipeline = load_reduced_model()
                    if pipeline is not None:
                        input_df = pd.DataFrame([{
                            'CGPA': float(cgpa_val),
                            'AptitudeTestScore': float(apt_val),
                            'SoftSkillsRating': float(soft_val),
                            'SSC_Marks': float(ssc_val),
                            'HSC_Marks': float(hsc_val)
                        }])[['CGPA', 'AptitudeTestScore', 'SoftSkillsRating', 'SSC_Marks', 'HSC_Marks']]
                        pred_proba = pipeline.predict_proba(input_df)[0]
                        st.session_state.historical_ml_prob = float(pred_proba[1]) * 100.0

                    st.session_state.current_step = "aptitude_intro"
                    st.rerun()


# =============================================================================
# 5. STEP 3: LIVE APTITUDE ASSESSMENT (INTRO)
# =============================================================================

elif st.session_state.current_step == "aptitude_intro":
    render_progress_bar(2)
    st.markdown("## Live Aptitude Assessment")
    st.markdown("Answer 15 randomized questions across Quantitative, Logical, Verbal, and Data Interpretation.")

    with st.container(border=True):
        st.markdown("**Categories Covered:**")
        st.markdown("""
        <span class='badge-tag'>Quantitative Aptitude (4)</span>
        <span class='badge-tag'>Logical Reasoning (4)</span>
        <span class='badge-tag'>Verbal Ability (4)</span>
        <span class='badge-tag'>Data Interpretation (3)</span>
        """, unsafe_allow_html=True)
        st.caption("15 Multiple-Choice Questions | 1 point per correct answer | No negative marking | Contributes 35% to final placement probability")

    col_nav1, col_nav2 = st.columns([1, 2])
    with col_nav1:
        if st.button("Back"):
            st.session_state.current_step = "academic"
            st.rerun()
    with col_nav2:
        if st.button("Start Aptitude Test", type="primary", use_container_width=True):
            if st.session_state.aptitude_questions is None:
                st.session_state.aptitude_questions = select_assessment_questions()
                st.session_state.aptitude_answers = {}
                st.session_state.aptitude_q_idx = 0
            st.session_state.current_step = "aptitude_test"
            st.rerun()


# =============================================================================
# 6. STEP 3: LIVE APTITUDE ASSESSMENT (QUESTIONS)
# =============================================================================

elif st.session_state.current_step == "aptitude_test":
    render_progress_bar(2)
    questions = st.session_state.aptitude_questions
    if questions is None:
        st.session_state.aptitude_questions = select_assessment_questions()
        questions = st.session_state.aptitude_questions

    q_idx = st.session_state.aptitude_q_idx
    q = questions[q_idx]

    answered_count = len([ans for ans in st.session_state.aptitude_answers.values() if ans is not None])
    st.markdown(f"**Question {q_idx + 1} of 15** `[{q['category']}]` — *Answered: {answered_count}/15*")

    with st.container(border=True):
        st.markdown(f"### {q['question']}")

        prev_answer = st.session_state.aptitude_answers.get(q["id"], None)
        selected_opt_idx = q["options"].index(prev_answer) if prev_answer in q["options"] else None

        chosen_ans = st.radio(
            "Select your answer:",
            options=q["options"],
            index=selected_opt_idx,
            key=f"apt_radio_{q['id']}",
            label_visibility="collapsed"
        )
        if chosen_ans is not None:
            st.session_state.aptitude_answers[q["id"]] = chosen_ans

    cols_nav = st.columns([1, 1, 2])
    with cols_nav[0]:
        if st.button("Previous", disabled=(q_idx == 0)):
            st.session_state.aptitude_q_idx = max(0, q_idx - 1)
            st.rerun()
    with cols_nav[1]:
        if q_idx < len(questions) - 1:
            if st.button("Next"):
                st.session_state.aptitude_q_idx = min(len(questions) - 1, q_idx + 1)
                st.rerun()
    with cols_nav[2]:
        if st.button("Submit Test", type="primary", use_container_width=True):
            user_answers = {qid: ans for qid, ans in st.session_state.aptitude_answers.items() if ans is not None}
            res = evaluate_assessment(questions, user_answers)
            st.session_state.aptitude_result = res
            st.session_state.current_step = "aptitude_result"
            st.rerun()


# =============================================================================
# 7. STEP 3: LIVE APTITUDE ASSESSMENT (RESULTS)
# =============================================================================

elif st.session_state.current_step == "aptitude_result":
    render_progress_bar(2)
    result = st.session_state.aptitude_result

    st.markdown("## Your Aptitude Results")

    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Score", f"{result['score']} / {result['total']}")
        with c2:
            st.metric("Percentage", f"{result['percentage']:.1f}%")

        st.markdown("---")
        strong = result.get("strong_topics", [])
        weak = result.get("weak_topics", [])

        if strong:
            st.markdown(f"**Strong Areas:** {', '.join(strong)}")
        else:
            st.markdown("**Strong Areas:** None above the 70% benchmark")

        if weak:
            st.markdown(f"**Weak Areas:** {', '.join(weak)}")
        else:
            st.markdown("**Weak Areas:** None. Excellent performance.")

        st.caption("Note: This live assessment score contributes 35% directly toward your final placement probability.")

    col_nav1, col_nav2 = st.columns([1, 2])
    with col_nav1:
        if st.button("Retake Assessment"):
            st.session_state.aptitude_questions = None
            st.session_state.aptitude_answers = {}
            st.session_state.aptitude_q_idx = 0
            st.session_state.aptitude_result = None
            st.session_state.current_step = "aptitude_intro"
            st.rerun()
    with col_nav2:
        if st.button("Continue to Technical Assessment", type="primary", use_container_width=True):
            st.session_state.current_step = "technical_intro"
            st.rerun()


# =============================================================================
# 8. STEP 4: LIVE TECHNICAL ASSESSMENT (INTRO)
# =============================================================================

elif st.session_state.current_step == "technical_intro":
    render_progress_bar(3)
    st.markdown("## Live Technical Assessment")
    st.markdown("Which technical area would you like to assess?")

    domain_choice = st.radio(
        "Choose an assessment track:",
        ["Both", "IT", "Core"],
        index=["Both", "IT", "Core"].index(st.session_state.technical_domain),
        horizontal=True
    )
    st.session_state.technical_domain = domain_choice

    display_dept = st.session_state.other_dept if st.session_state.student_dept == "Other Engineering / Technology" and st.session_state.other_dept else st.session_state.student_dept
    if "Electronics" in display_dept or "Electrical" in display_dept:
        st.info("Note: 'Core' or 'Both' is well-suited for your branch, but you can freely choose any track.")

    st.caption("15 Questions | IT covers programming, DSA, OOP, DBMS, SQL, OS, networks | Core covers digital/analog circuits, microprocessors, microcontrollers, embedded systems | Contributes 35% to final placement probability")

    col_nav1, col_nav2 = st.columns([1, 2])
    with col_nav1:
        if st.button("Back"):
            st.session_state.current_step = "aptitude_result"
            st.rerun()
    with col_nav2:
        if st.button("Start Technical Test", type="primary", use_container_width=True):
            st.session_state.technical_questions = select_technical_questions(domain=domain_choice)
            st.session_state.technical_answers = {}
            st.session_state.tech_q_idx = 0
            st.session_state.current_step = "technical_test"
            st.rerun()


# =============================================================================
# 9. STEP 4: LIVE TECHNICAL ASSESSMENT (QUESTIONS)
# =============================================================================

elif st.session_state.current_step == "technical_test":
    render_progress_bar(3)
    questions = st.session_state.technical_questions
    if questions is None:
        st.session_state.technical_questions = select_technical_questions(domain=st.session_state.technical_domain)
        questions = st.session_state.technical_questions

    q_idx = st.session_state.tech_q_idx
    q = questions[q_idx]

    answered_count = len([ans for ans in st.session_state.technical_answers.values() if ans is not None])
    st.markdown(f"**Question {q_idx + 1} of 15** `[{q['domain']} - {q['topic']}]` — *Answered: {answered_count}/15*")

    with st.container(border=True):
        st.markdown(f"### {q['question']}")

        prev_answer = st.session_state.technical_answers.get(q["id"], None)
        selected_opt_idx = q["options"].index(prev_answer) if prev_answer in q["options"] else None

        chosen_ans = st.radio(
            "Select your answer:",
            options=q["options"],
            index=selected_opt_idx,
            key=f"tech_radio_{q['id']}",
            label_visibility="collapsed"
        )
        if chosen_ans is not None:
            st.session_state.technical_answers[q["id"]] = chosen_ans

    cols_nav = st.columns([1, 1, 2])
    with cols_nav[0]:
        if st.button("Previous", disabled=(q_idx == 0)):
            st.session_state.tech_q_idx = max(0, q_idx - 1)
            st.rerun()
    with cols_nav[1]:
        if q_idx < len(questions) - 1:
            if st.button("Next"):
                st.session_state.tech_q_idx = min(len(questions) - 1, q_idx + 1)
                st.rerun()
    with cols_nav[2]:
        if st.button("Submit Test", type="primary", use_container_width=True):
            user_answers = {qid: ans for qid, ans in st.session_state.technical_answers.items() if ans is not None}
            res = evaluate_technical_assessment(questions, user_answers)
            st.session_state.technical_result = res
            st.session_state.current_step = "technical_result"
            st.rerun()


# =============================================================================
# 10. STEP 4: LIVE TECHNICAL ASSESSMENT (RESULTS)
# =============================================================================

elif st.session_state.current_step == "technical_result":
    render_progress_bar(3)
    result = st.session_state.technical_result

    st.markdown("## Your Technical Results")

    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Overall Score", f"{result['score']} / {result['total']}")
        with c2:
            st.metric("Percentage", f"{result['percentage']:.1f}%")

        if "Both" in result["domain"] or len(result.get("domain_scores", {})) > 1:
            st.markdown("---")
            dcols = st.columns(len(result["domain_scores"]))
            for idx, (dom, stats) in enumerate(result["domain_scores"].items()):
                with dcols[idx]:
                    st.markdown(f"**{dom} Track:** {stats['score']}/{stats['total']} ({stats['percentage']:.1f}%)")

        st.markdown("---")
        strong = result.get("strong_topics", [])
        weak = result.get("weak_topics", [])

        if strong:
            st.markdown(f"**Strong Skills:** {', '.join(strong)}")
        else:
            st.markdown("**Strong Skills:** None above the 70% benchmark")

        if weak:
            st.markdown(f"**Skills to Improve:** {', '.join(weak)}")
        else:
            st.markdown("**Skills to Improve:** None. Solid technical foundation.")

        st.caption("Note: This live assessment score contributes 35% directly toward your final placement probability.")

    col_nav1, col_nav2 = st.columns([1, 2])
    with col_nav1:
        if st.button("Retake Assessment"):
            st.session_state.technical_questions = None
            st.session_state.technical_answers = {}
            st.session_state.tech_q_idx = 0
            st.session_state.technical_result = None
            st.session_state.current_step = "technical_intro"
            st.rerun()
    with col_nav2:
        if st.button("Continue to Skill Assessment", type="primary", use_container_width=True):
            st.session_state.current_step = "skill_assessment"
            st.rerun()


# =============================================================================
# 11. STEP 5: SKILL ASSESSMENT (FAMILIARITY & SELF-REPORTED LEVEL)
# =============================================================================

elif st.session_state.current_step == "skill_assessment":
    render_progress_bar(4)
    st.markdown("## Skill Assessment")
    st.markdown("Select modern industry technologies you are familiar with and indicate your self-reported skill level.")

    with st.container(border=True):
        selected_skills = st.multiselect(
            "Select technologies and skill areas you have worked with or are pursuing:",
            options=SKILL_ASSESSMENT_AREAS,
            default=st.session_state.skill_assessment_selections,
            placeholder="Choose skill areas..."
        )

        st.caption("Selected skill areas indicate your interest and practical exposure.")

        if selected_skills:
            st.markdown("---")
            st.markdown("**Self-Reported Skill Level:**")
            for skill in selected_skills:
                c_lbl, c_sel = st.columns([2, 1])
                with c_lbl:
                    st.markdown(f"• **{skill}**")
                with c_sel:
                    curr_level = st.session_state.skill_levels.get(skill, "Intermediate")
                    lvl = st.selectbox(
                        f"Level for {skill}",
                        options=["Beginner", "Intermediate", "Advanced"],
                        index=["Beginner", "Intermediate", "Advanced"].index(curr_level),
                        key=f"skill_level_sel_{skill}",
                        label_visibility="collapsed"
                    )
                    st.session_state.skill_levels[skill] = lvl

        st.caption("Note: Self-reported skill levels reflect your current familiarity and interest in pursuing these areas. They are recorded for profile enrichment and do not alter your placement probability.")

    col_nav1, col_nav2 = st.columns([1, 2])
    with col_nav1:
        if st.button("Back"):
            st.session_state.current_step = "technical_result"
            st.rerun()
    with col_nav2:
        if st.button("Continue to Areas of Interest", type="primary", use_container_width=True):
            st.session_state.skill_assessment_selections = selected_skills
            st.session_state.current_step = "interests"
            st.rerun()


# =============================================================================
# 12. STEP 6: AREAS OF INTEREST
# =============================================================================

elif st.session_state.current_step == "interests":
    render_progress_bar(5)
    st.markdown("## Areas of Interest")
    st.markdown("Which areas are you interested in pursuing? Choose up to 4 areas.")

    with st.container(border=True):
        selected_interests = st.multiselect(
            "Select 1 to 4 career interest areas:",
            options=AREAS_OF_INTEREST,
            default=st.session_state.interests,
            max_selections=4,
            placeholder="Select career interest areas..."
        )

        st.caption(f"Selected: **{len(selected_interests)} of 4 (maximum 4)**")
        st.caption("Your selected interests directly guide the career recommendation engine and do not modify the placement probability.")

    col_nav1, col_nav2 = st.columns([1, 2])
    with col_nav1:
        if st.button("Back"):
            st.session_state.current_step = "skill_assessment"
            st.rerun()
    with col_nav2:
        if st.button("View My Results", type="primary", use_container_width=True):
            if len(selected_interests) == 0:
                st.error("Please select at least 1 area of interest (up to 4).")
            elif len(selected_interests) > 4:
                st.error("Please select at most 4 areas of interest.")
            else:
                st.session_state.interests = selected_interests
                st.session_state.current_step = "placement_probability"
                st.rerun()


# =============================================================================
# 13. STEP 7: WEIGHTED PLACEMENT PROBABILITY
# =============================================================================

elif st.session_state.current_step == "placement_probability":
    render_progress_bar(6)
    st.markdown("## Estimated Placement Probability")

    # Extract live test percentages and academic indicators
    apt_pct = float(st.session_state.aptitude_result.get("percentage", 0.0)) if st.session_state.aptitude_result else 0.0
    tech_pct = float(st.session_state.technical_result.get("percentage", 0.0)) if st.session_state.technical_result else 0.0
    ssc_pct = float(st.session_state.academic_ssc) if st.session_state.academic_ssc is not None else 0.0
    hsc_pct = float(st.session_state.academic_hsc) if st.session_state.academic_hsc is not None else 0.0

    # Deterministic 70/30 formula: 0.35*Apt + 0.35*Tech + 0.15*SSC + 0.15*HSC
    prob_val = calculate_weighted_placement_probability(
        aptitude_percentage=apt_pct,
        technical_percentage=tech_pct,
        ssc_percentage=ssc_pct,
        hsc_percentage=hsc_pct
    )
    st.session_state.placement_prob = prob_val

    with st.container(border=True):
        st.markdown(
            f"<div style='text-align: center; padding: 2rem 1rem;'>"
            f"<div style='font-size: 3.5rem; font-weight: 700; color: #1a73e8;'>{prob_val:.2f}%</div>"
            f"<p style='color: #3c4043; font-size: 1.05rem; margin-top: 0.75rem;'>"
            f"Your current placement estimate is primarily based on your live aptitude and technical performance, with academic performance contributing the remaining 30%.</p>"
            f"<p style='color: #70757a; font-size: 0.88rem; margin-top: 0.25rem;'>"
            f"This estimate is calculated from current assessment performance and academic indicators using the project's predefined weighting formula.</p>"
            f"</div>",
            unsafe_allow_html=True
        )

    st.markdown("### Performance Breakdown")
    with st.container(border=True):
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Aptitude Performance", f"{apt_pct:.1f}%")
            st.caption("Weight: 35%")
        with m2:
            st.metric("Technical Performance", f"{tech_pct:.1f}%")
            st.caption("Weight: 35%")
        with m3:
            st.metric("SSC Performance", f"{ssc_pct:.1f}%")
            st.caption("Weight: 15%")
        with m4:
            st.metric("HSC Performance", f"{hsc_pct:.1f}%")
            st.caption("Weight: 15%")

    col_nav1, col_nav2 = st.columns([1, 2])
    with col_nav1:
        if st.button("Back"):
            st.session_state.current_step = "interests"
            st.rerun()
    with col_nav2:
        if st.button("Continue to Career Recommendations", type="primary", use_container_width=True):
            st.session_state.current_step = "career"
            st.rerun()


# =============================================================================
# 14. STEP 8: CAREER RECOMMENDATIONS
# =============================================================================

elif st.session_state.current_step == "career":
    render_progress_bar(6)
    st.markdown("## Careers That Match You")
    st.markdown("Based on your technical skills, aptitude performance, placement probability, and areas of interest.")

    # Calculate recommendations using separate 40/20/20/20 ranking formula
    selected_domain = st.session_state.technical_domain
    career_data = recommend_careers(
        placement_probability=st.session_state.placement_prob,
        aptitude_result=st.session_state.aptitude_result,
        technical_result=st.session_state.technical_result,
        selected_domain=selected_domain,
        top_n=3,
        interests=st.session_state.interests
    )
    st.session_state.career_result = career_data
    recs = career_data["recommendations"]

    for rank, r in enumerate(recs, start=1):
        with st.container(border=True):
            col_t1, col_t2 = st.columns([3, 1])
            with col_t1:
                st.markdown(f"### Career #{rank}: {r['role']}")
                st.caption(f"Domain: {r['domain']}")
            with col_t2:
                st.markdown(f"**Match Score: {r['match_score']:.1f}%**")
                st.caption(f"[{r['match_level']}]")

            # 4 compact sub-metrics breakdown
            m1, m2, m3, m4 = st.columns(4)
            with m1:
                st.metric("Technical Match", f"{r['technical_match']:.1f}%")
            with m2:
                st.metric("Aptitude Match", f"{r['aptitude_match']:.1f}%")
            with m3:
                st.metric("Placement Probability", f"{r['placement_probability']:.1f}%")
            with m4:
                im_val = r.get('interest_match')
                im_str = f"{im_val:.1f}%" if im_val is not None else "0.0%"
                st.metric("Interest Match", im_str)

            # Concise matching rationale
            reasons = r.get("why_recommended", [])
            primary_reason = reasons[0] if reasons else "Strong alignment with your profile and interests."
            st.markdown(f"**Why this matches you:** {primary_reason}")

    col_nav1, col_nav2 = st.columns([1, 2])
    with col_nav1:
        if st.button("Back"):
            st.session_state.current_step = "placement_probability"
            st.rerun()
    with col_nav2:
        if st.button("Continue to Skill Gap Analysis", type="primary", use_container_width=True):
            st.session_state.current_step = "skill_gap"
            st.rerun()


# =============================================================================
# 15. STEP 9: SKILL GAP ANALYSIS
# =============================================================================

elif st.session_state.current_step == "skill_gap":
    render_progress_bar(6)
    st.markdown("## Your Skill Gaps")
    st.markdown("Identified areas for improvement against the 70% proficiency target:")

    apt_res = st.session_state.aptitude_result
    tech_res = st.session_state.technical_result
    recs = st.session_state.career_result["recommendations"] if st.session_state.career_result else []

    apt_weaks = apt_res.get("weak_topics", []) if apt_res else []
    tech_weaks = tech_res.get("weak_topics", []) if tech_res else []

    career_gaps = []
    if recs:
        for gap in recs[0].get("skill_gaps", []):
            if gap not in career_gaps:
                career_gaps.append(gap)

    total_gaps_count = len(apt_weaks) + len(tech_weaks) + len(career_gaps)

    if total_gaps_count == 0:
        st.success("No major skill gaps identified across your assessments.")
    else:
        # 1. Aptitude Areas to Improve
        if apt_weaks:
            st.markdown("#### Aptitude Areas to Improve")
            for cat in apt_weaks:
                score_pct = apt_res["category_scores"].get(cat, {}).get("percentage", 0.0)
                if cat == "Quantitative Aptitude":
                    act = "Practice 20 quantitative aptitude problems daily."
                elif cat == "Logical Reasoning":
                    act = "Practice timed logical deduction and pattern sets."
                elif cat == "Verbal Ability":
                    act = "Revise reading comprehension and grammar rules."
                elif cat == "Data Interpretation":
                    act = "Practice table and chart interpretation problems daily."
                else:
                    act = "Practice timed sets daily."

                with st.container(border=True):
                    c1, c2, c3 = st.columns([2, 1, 3])
                    with c1:
                        st.markdown(f"**{cat}**")
                    with c2:
                        st.markdown(f"Current: **{score_pct:.0f}%**  \nTarget: **70%**")
                    with c3:
                        st.markdown(f"Action: {act}")

        # 2. Technical Skills to Improve
        if tech_weaks:
            st.markdown("#### Technical Skills to Improve")
            for top in tech_weaks:
                score_pct = tech_res["topic_scores"].get(top, {}).get("percentage", 0.0)
                action_text = TOPIC_RECOMMENDATIONS.get(top, "Review fundamental concepts and solve practical problems.")
                with st.container(border=True):
                    c1, c2, c3 = st.columns([2, 1, 3])
                    with c1:
                        st.markdown(f"**{top}**")
                    with c2:
                        st.markdown(f"Current: **{score_pct:.0f}%**  \nTarget: **70%**")
                    with c3:
                        st.markdown(f"Action: {action_text}")

        # 3. Career-Specific Skills to Improve
        if career_gaps:
            st.markdown("#### Career-Specific Skills to Improve")
            with st.container(border=True):
                st.markdown(f"**Key skills for {recs[0]['role']}:**")
                for cg in career_gaps[:3]:
                    st.markdown(f"• {cg}")

    col_nav1, col_nav2 = st.columns([1, 2])
    with col_nav1:
        if st.button("Back"):
            st.session_state.current_step = "career"
            st.rerun()
    with col_nav2:
        if st.button("Continue to Improvement Plan", type="primary", use_container_width=True):
            st.session_state.current_step = "improvement"
            st.rerun()


# =============================================================================
# 16. STEP 10: PERSONALIZED IMPROVEMENT PLAN
# =============================================================================

elif st.session_state.current_step == "improvement":
    render_progress_bar(6)
    st.markdown("## Your Personalized Improvement Plan")
    st.markdown("Follow this step-by-step roadmap to boost your career readiness:")

    apt_weaks = st.session_state.aptitude_result.get("weak_topics", []) if st.session_state.aptitude_result else []
    tech_weaks = st.session_state.technical_result.get("weak_topics", []) if st.session_state.technical_result else []
    recs = st.session_state.career_result["recommendations"] if st.session_state.career_result else []

    roadmap_steps = []

    # Step 1: Aptitude
    if apt_weaks:
        roadmap_steps.append(f"Strengthen {apt_weaks[0]} with 20 minutes of daily question practice.")
    else:
        roadmap_steps.append("Maintain aptitude speed with weekly timed mock assessments.")

    # Step 2: Technical
    if tech_weaks:
        primary_tech = tech_weaks[0]
        advice = TOPIC_RECOMMENDATIONS.get(primary_tech, "Review core concepts and solve practical coding problems.")
        roadmap_steps.append(f"Improve {primary_tech}: {advice}")
    else:
        roadmap_steps.append("Deepen domain mastery by exploring advanced system architectures.")

    # Step 3: Modern Technologies
    if st.session_state.skill_assessment_selections:
        first_skill = st.session_state.skill_assessment_selections[0]
        roadmap_steps.append(f"Practice {first_skill} through hands-on tutorials and code implementations.")
    else:
        roadmap_steps.append("Practice modern industry tools and cloud foundations.")

    # Step 4: Portfolio Project
    if recs:
        top_role = recs[0]
        role_skills = top_role.get("recommended_skills", [])
        top_skill = role_skills[0] if role_skills else "target technologies"
        roadmap_steps.append(f"Build one portfolio project focusing on {top_role['role']} ({top_skill}).")
    else:
        roadmap_steps.append("Build one full-stack or domain-specific portfolio project.")

    # Step 5: Technical Interview Practice
    roadmap_steps.append("Practice technical interview questions, data structures, and behavioral responses.")

    # Step 6: Mock Readiness Reassessment
    roadmap_steps.append("Take a comprehensive mock assessment before campus recruitment drives.")

    with st.container(border=True):
        for idx, step in enumerate(roadmap_steps, start=1):
            st.markdown(f"**Step {idx}:** {step}")

    col_nav1, col_nav2 = st.columns([1, 2])
    with col_nav1:
        if st.button("Back"):
            st.session_state.current_step = "skill_gap"
            st.rerun()
    with col_nav2:
        if st.button("Finish Assessment", type="primary", use_container_width=True):
            st.session_state.current_step = "finish"
            st.rerun()


# =============================================================================
# 17. STEP 11: FINAL COMPLETION PAGE (STRICTLY NO RESTART BUTTON)
# =============================================================================

elif st.session_state.current_step == "finish":
    st.markdown("## Your Career Assessment is Complete")

    s_name = st.session_state.student_name or "Student"
    display_dept = st.session_state.other_dept if st.session_state.student_dept == "Other Engineering / Technology" and st.session_state.other_dept else st.session_state.student_dept
    s_dept = display_dept if display_dept != "Select Department" else "Engineering"
    s_year = st.session_state.student_year if st.session_state.student_year != "Select Year" else "Current Year"
    prob_val = st.session_state.placement_prob or 0.0

    recs = st.session_state.career_result["recommendations"] if st.session_state.career_result else []
    top_role_name = recs[0]["role"] if recs else "Software Developer"

    with st.container(border=True):
        st.markdown(f"### Assessment Summary for {s_name}")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**Student:** {s_name}")
            st.markdown(f"**Department:** {s_dept}")
            st.markdown(f"**Year of Study:** {s_year}")
        with c2:
            st.markdown(f"**Estimated Placement Probability:** **{prob_val:.2f}%**")
            st.markdown(f"**Top Career Recommendation:** **{top_role_name}**")

    st.markdown("""
    Your assessment has identified your current strengths, areas that need improvement, and career paths aligned with your skills and interests.

    Use these insights as a roadmap for your preparation and career development.

    **Keep learning. Keep practicing. Keep moving forward.**
    """)
