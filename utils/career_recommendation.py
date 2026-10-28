"""
Career Recommendation Engine
Provides transparent, rule-based career matching, skill-gap identification,
and personalized improvement guidance.
"""

from typing import List, Dict, Any, Optional

try:
    from data.career_roles import CAREER_ROLES
except ImportError:
    from ..data.career_roles import CAREER_ROLES

TOPIC_RECOMMENDATIONS = {
    "Programming": "Practice basic programming patterns, algorithmic problem-solving, and core language features.",
    "Data Structures & Algorithms": "Practice arrays, strings, sorting, searching, stacks, and queues on LeetCode or HackerRank.",
    "OOP": "Revise the 4 OOP pillars (Inheritance, Polymorphism, Encapsulation, Abstraction) and class design patterns.",
    "DBMS": "Revise normalization, candidate keys, indexing, transactions, and ACID properties.",
    "SQL": "Practice SELECT, JOIN, GROUP BY, HAVING, subqueries, and aggregate functions.",
    "Operating Systems": "Revise CPU scheduling, deadlocks, paging, virtual memory, and process synchronization.",
    "Computer Networks": "Review OSI layers, TCP/UDP protocols, IP subnetting, and HTTP/HTTPS architecture.",
    "Digital Electronics": "Revise logic gates, Boolean algebra, K-maps, combinational circuits (MUX), and sequential flip-flops.",
    "Analog Electronics": "Revise op-amp configurations, negative feedback, BJT biasing regions, and frequency response.",
    "Microprocessors": "Study 8085/8086 architectures, register organization, memory segmentation, and interrupt handling.",
    "Microcontrollers": "Review 8051/ARM architecture, timer modes, GPIO interfacing, and interrupt service routines.",
    "Communication Systems": "Revise sampling theorem, AM/FM modulation, Nyquist criteria, and digital BPSK/QAM schemes.",
    "Signals & Systems": "Practice convolution, Fourier transforms, Laplace transforms, and LTI stability conditions.",
    "Electronic Devices": "Revise semiconductor physics, PN junction characteristics, and MOSFET operation thresholds.",
    "Embedded Systems": "Study RTOS task scheduling, priority inversion, interrupt latency, and DMA operations."
}

def normalize_interest(interest: str) -> str:
    """Normalizes interest labels so both UI variations match canonical role interests."""
    if interest in {"Web Development", "Web / Frontend Development", "Frontend Development"}:
        return "Web / Frontend Development"
    if interest in {"Artificial Intelligence", "AI"}:
        return "Data Science & AI"
    return interest



ROLE_INTEREST_MAPPING = {
    "Software Developer": ["Software Development"],
    "Frontend Developer": ["Web / Frontend Development", "UI/UX"],
    "Backend Developer": ["Software Development", "Cloud Computing", "DevOps"],
    "Full Stack Developer": ["Software Development", "Web / Frontend Development"],
    "Data Analyst": ["Data Analytics", "Data Science & AI"],
    "Data Scientist": ["Data Science & AI", "Machine Learning"],
    "ML Engineer": ["Machine Learning", "Data Science & AI"],
    "DevOps Engineer": ["DevOps", "Cloud Computing"],
    "QA Engineer": ["Testing / QA", "Software Development"],
    "Cloud Engineer": ["Cloud Computing", "Networking", "DevOps"],
    "Cybersecurity Analyst": ["Cybersecurity", "Networking"],
    "Embedded Engineer": ["Embedded Systems", "Electronics & Communication", "VLSI / Semiconductor"]
}


def get_match_level(score: float) -> str:
    """
    Classifies match score into standard confidence levels:
    - 80.0 to 100.0: Strong Match
    - 65.0 to 79.99: Good Match
    - 50.0 to 64.99: Moderate Match
    - Below 50.0: Weak Match
    """
    if score >= 80.0:
        return "Strong Match"
    elif score >= 65.0:
        return "Good Match"
    elif score >= 50.0:
        return "Moderate Match"
    else:
        return "Weak Match"


def recommend_careers(
    placement_probability: float,
    aptitude_result: Dict[str, Any],
    technical_result: Dict[str, Any],
    selected_domain: str = "Both",
    career_roles: Optional[List[Dict[str, Any]]] = None,
    top_n: int = 3,
    interests: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Generates transparent, rule-based career recommendations.

    Args:
        placement_probability: Probability from placement model (0.0 to 1.0 or 0 to 100)
        aptitude_result: Dict from aptitude assessment evaluation
        technical_result: Dict from technical assessment evaluation
        selected_domain: 'IT', 'Core', or 'Both'
        career_roles: Optional custom roles list (defaults to CAREER_ROLES)
        top_n: Number of recommendations to return (default 3)

    Returns:
        Structured dictionary containing ranked recommendations with match scores,
        why_recommended rationales, skill gaps, recommended skills, and actionable advice.
    """
    if career_roles is None:
        career_roles = CAREER_ROLES

    if selected_domain not in {"IT", "Core", "Both"}:
        raise ValueError(f"Invalid selected_domain '{selected_domain}'. Must be 'IT', 'Core', or 'Both'")

    # 1. Normalize Placement Readiness (0 to 100)
    if 0.0 <= placement_probability <= 1.0:
        placement_readiness = placement_probability * 100.0
    else:
        placement_readiness = float(placement_probability)
    placement_readiness = max(0.0, min(100.0, placement_readiness))

    # 2. Extract Aptitude Scores
    overall_aptitude = float(aptitude_result.get("percentage", 0.0))
    aptitude_cat_scores = aptitude_result.get("category_scores", {})

    # 3. Extract Technical Scores
    topic_scores = technical_result.get("topic_scores", {})
    domain_scores = technical_result.get("domain_scores", {})

    scored_roles = []

    for role in career_roles:
        role_domain = role["domain"]

        # Domain filtering: enforce strict separation if user specified IT or Core
        if selected_domain == "IT" and role_domain != "IT":
            continue
        if selected_domain == "Core" and role_domain != "Core":
            continue

        important_topics = role["important_topics"]
        preferred_aptitude = role["preferred_aptitude"]

        # --- A. Technical Match (50% weight) ---
        tested_topic_pcts = []
        tested_topic_map = {}
        for t in important_topics:
            if t in topic_scores:
                pct = topic_scores[t]["percentage"]
                tested_topic_pcts.append(pct)
                tested_topic_map[t] = pct

        if tested_topic_pcts:
            technical_match = sum(tested_topic_pcts) / len(tested_topic_pcts)
        else:
            # If none of the specific topics were tested, check domain level performance
            if role_domain in domain_scores:
                technical_match = float(domain_scores[role_domain].get("percentage", 0.0))
            else:
                technical_match = 0.0

        technical_match = max(0.0, min(100.0, technical_match))

        # --- B. Aptitude Match (25% weight) ---
        preferred_apt_pcts = []
        for cat in preferred_aptitude:
            if cat in aptitude_cat_scores:
                preferred_apt_pcts.append(aptitude_cat_scores[cat]["percentage"])

        if preferred_apt_pcts:
            preferred_avg = sum(preferred_apt_pcts) / len(preferred_apt_pcts)
            # Blend 70% domain-relevant aptitude + 30% overall aptitude
            aptitude_match = (0.70 * preferred_avg) + (0.30 * overall_aptitude)
        else:
            aptitude_match = overall_aptitude

        aptitude_match = max(0.0, min(100.0, aptitude_match))

        # --- C. Weighted Final Match Score (0 to 100) ---
        interest_match = None
        matched_interests = []
        if interests is not None:
            role_interests = ROLE_INTEREST_MAPPING.get(role["role"], [])
            matched_interests = [normalize_interest(i) for i in interests if normalize_interest(i) in role_interests]
            m_count = len(matched_interests)
            if m_count == 0 or len(role_interests) == 0:
                interest_match = 0.0
            else:
                interest_match = round((m_count / len(role_interests)) * 100.0, 2)
                interest_match = min(100.0, max(0.0, interest_match))

            # Transparent 40/20/20/20 weighting
            t_weight = 0.40
            a_weight = 0.20
            p_weight = 0.20
            i_weight = 0.20
            total_match = (
                (technical_match * t_weight) +
                (aptitude_match * a_weight) +
                (placement_readiness * p_weight) +
                (interest_match * i_weight)
            )
        else:
            # Fallback to standard 50/25/25 formula when interests is None
            t_weight = role.get("technical_weight", 0.50)
            a_weight = role.get("aptitude_weight", 0.25)
            p_weight = role.get("placement_weight", 0.25)
            total_match = (
                (technical_match * t_weight) +
                (aptitude_match * a_weight) +
                (placement_readiness * p_weight)
            )

        total_match = round(max(0.0, min(100.0, total_match)), 2)

        # --- D. Rationales (Why Recommended) ---
        why_recommended = []
        if matched_interests:
            why_recommended.append(f"Strong interest alignment ({', '.join(matched_interests)})")

        for t, pct in tested_topic_map.items():
            if pct >= 70.0:
                why_recommended.append(f"Strong performance in {t} ({pct:.1f}%)")

        if placement_readiness >= 75.0:
            why_recommended.append(f"Solid placement readiness ({placement_readiness:.1f}%)")
        if aptitude_match >= 75.0:
            why_recommended.append(f"Good aptitude alignment ({aptitude_match:.1f}%)")

        if not why_recommended:
            why_recommended.append("Baseline alignment with student curriculum profile")

        # --- E. Skill Gaps (< 70% in important topics) ---
        skill_gaps = []
        actionable_recommendations = []
        for t, pct in tested_topic_map.items():
            if pct < 70.0:
                skill_gaps.append(f"Improve {t} ({pct:.1f}%)")
                if t in TOPIC_RECOMMENDATIONS:
                    actionable_recommendations.append(TOPIC_RECOMMENDATIONS[t])

        # If a core important topic was completely untested, note it as an exploration gap
        untested_topics = [t for t in important_topics if t not in tested_topic_map]
        for ut in untested_topics:
            skill_gaps.append(f"Assess & verify knowledge in {ut}")
            if ut in TOPIC_RECOMMENDATIONS and TOPIC_RECOMMENDATIONS[ut] not in actionable_recommendations:
                actionable_recommendations.append(TOPIC_RECOMMENDATIONS[ut])

        scored_roles.append({
            "role": role["role"],
            "domain": role_domain,
            "match_score": total_match,
            "match_level": get_match_level(total_match),
            "technical_match": round(technical_match, 2),
            "aptitude_match": round(aptitude_match, 2),
            "placement_probability": round(placement_readiness, 2),
            "placement_readiness": round(placement_readiness, 2),
            "interest_match": round(interest_match, 2) if interest_match is not None else None,
            "matched_interests": matched_interests,
            "description": role["description"],
            "why_recommended": why_recommended,
            "skill_gaps": skill_gaps,
            "recommended_skills": role["skills"],
            "actionable_recommendations": actionable_recommendations
        })

    # Sort descending by match score
    scored_roles.sort(key=lambda r: r["match_score"], reverse=True)

    # Return top N recommendations
    final_recommendations = scored_roles[:top_n]

    return {
        "selected_domain": selected_domain,
        "recommendations": final_recommendations,
        "total_evaluated": len(scored_roles)
    }
