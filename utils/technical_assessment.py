"""
Technical Assessment Utility Module
Provides question selection, scoring, domain and topic diagnostics, and data validation
for the live 15-question technical assessment across IT, Core, and Both modes.
"""

import random
from typing import List, Dict, Any, Optional

try:
    from data.technical_questions import TECHNICAL_QUESTIONS
except ImportError:
    from ..data.technical_questions import TECHNICAL_QUESTIONS

IT_TOPICS = [
    "Programming",
    "Data Structures & Algorithms",
    "OOP",
    "DBMS",
    "SQL",
    "Operating Systems",
    "Computer Networks"
]

CORE_TOPICS = [
    "Digital Electronics",
    "Analog Electronics",
    "Microprocessors",
    "Microcontrollers",
    "Communication Systems",
    "Signals & Systems",
    "Electronic Devices",
    "Embedded Systems"
]

VALID_DOMAINS = {"IT", "Core", "Both"}
VALID_TOPICS = set(IT_TOPICS + CORE_TOPICS)
DEFAULT_THRESHOLD = 70.0


def validate_technical_question(q: Dict[str, Any]) -> bool:
    """
    Validates structure, domain, topic, and options of a single technical question.
    Raises ValueError if invalid.
    """
    required_keys = {"id", "domain", "topic", "question", "options", "answer", "explanation"}
    missing = required_keys - set(q.keys())
    if missing:
        raise ValueError(f"Technical question missing keys: {missing}")

    if not isinstance(q["id"], int):
        raise ValueError(f"Question ID must be integer, got {type(q['id'])}")

    if q["domain"] not in {"IT", "Core"}:
        raise ValueError(f"Invalid domain '{q['domain']}' in Q{q['id']}. Must be 'IT' or 'Core'")

    if q["topic"] not in VALID_TOPICS:
        raise ValueError(f"Invalid topic '{q['topic']}' in Q{q['id']}")

    if q["domain"] == "IT" and q["topic"] not in IT_TOPICS:
        raise ValueError(f"Topic '{q['topic']}' does not belong to IT domain in Q{q['id']}")

    if q["domain"] == "Core" and q["topic"] not in CORE_TOPICS:
        raise ValueError(f"Topic '{q['topic']}' does not belong to Core domain in Q{q['id']}")

    if not isinstance(q["question"], str) or not q["question"].strip():
        raise ValueError(f"Question text cannot be empty in Q{q['id']}")

    options = q["options"]
    if not isinstance(options, list) or len(options) != 4:
        raise ValueError(f"Q{q['id']} must have exactly 4 options")

    if not all(isinstance(opt, str) and opt.strip() for opt in options):
        raise ValueError(f"All options must be non-empty strings in Q{q['id']}")

    if q["answer"] not in options:
        raise ValueError(f"Answer '{q['answer']}' not found in options for Q{q['id']}")

    if not isinstance(q["explanation"], str) or not q["explanation"].strip():
        raise ValueError(f"Explanation cannot be empty in Q{q['id']}")

    return True


def validate_technical_question_set(questions: List[Dict[str, Any]], expected_domain: Optional[str] = None) -> bool:
    """
    Validates a complete set of 15 selected technical questions.
    Checks count, uniqueness, schemas, and domain composition.
    """
    if not isinstance(questions, list):
        raise ValueError("Questions must be a list")

    if len(questions) != 15:
        raise ValueError(f"Technical assessment must contain exactly 15 questions, found {len(questions)}")

    seen_ids = set()
    it_count = 0
    core_count = 0

    for q in questions:
        validate_technical_question(q)
        qid = q["id"]
        if qid in seen_ids:
            raise ValueError(f"Duplicate question ID {qid} found in selected set")
        seen_ids.add(qid)

        if q["domain"] == "IT":
            it_count += 1
        elif q["domain"] == "Core":
            core_count += 1

    if expected_domain == "IT":
        if it_count != 15:
            raise ValueError(f"IT mode must contain 15 IT questions, found {it_count}")
    elif expected_domain == "Core":
        if core_count != 15:
            raise ValueError(f"Core mode must contain 15 Core questions, found {core_count}")
    elif expected_domain == "Both":
        if it_count != 8 or core_count != 7:
            raise ValueError(f"Both mode must contain exactly 8 IT and 7 Core questions, found {it_count} IT and {core_count} Core")

    return True


def select_technical_questions(
    domain: str = "Both",
    question_bank: Optional[List[Dict[str, Any]]] = None,
    random_seed: Optional[int] = None
) -> List[Dict[str, Any]]:
    """
    Selects 15 questions from the technical question bank according to selected domain:
    - 'IT': exactly 15 IT questions (distributed as evenly as possible across the 7 IT topics)
    - 'Core': exactly 15 Core questions (distributed as evenly as possible across the 8 Core topics)
    - 'Both': exactly 8 IT questions + 7 Core questions
    """
    if domain not in VALID_DOMAINS:
        raise ValueError(f"Invalid domain '{domain}'. Must be one of {VALID_DOMAINS}")

    if question_bank is None:
        question_bank = TECHNICAL_QUESTIONS

    if random_seed is not None:
        rng = random.Random(random_seed)
    else:
        rng = random.Random()

    # Index questions by (domain, topic)
    topic_pools: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
        "IT": {t: [] for t in IT_TOPICS},
        "Core": {t: [] for t in CORE_TOPICS}
    }

    for q in question_bank:
        d = q["domain"]
        t = q["topic"]
        if d in topic_pools and t in topic_pools[d]:
            topic_pools[d][t].append(q)

    selected: List[Dict[str, Any]] = []

    if domain == "IT":
        # 15 questions across 7 topics: 6 topics get 2, 1 topic gets 3 (6*2 + 1*3 = 15)
        topics_shuffled = list(IT_TOPICS)
        rng.shuffle(topics_shuffled)
        # First topic gets 3, remaining 6 get 2
        for idx, t in enumerate(topics_shuffled):
            count = 3 if idx == 0 else 2
            available = topic_pools["IT"][t]
            if len(available) < count:
                raise ValueError(f"Insufficient questions for IT topic '{t}': available {len(available)}, needed {count}")
            selected.extend(rng.sample(available, count))

    elif domain == "Core":
        # 15 questions across 8 topics: 7 topics get 2, 1 topic gets 1 (7*2 + 1*1 = 15)
        topics_shuffled = list(CORE_TOPICS)
        rng.shuffle(topics_shuffled)
        # First 7 topics get 2, last gets 1
        for idx, t in enumerate(topics_shuffled):
            count = 1 if idx == 7 else 2
            available = topic_pools["Core"][t]
            if len(available) < count:
                raise ValueError(f"Insufficient questions for Core topic '{t}': available {len(available)}, needed {count}")
            selected.extend(rng.sample(available, count))

    elif domain == "Both":
        # 8 IT questions across 7 IT topics: 1 topic gets 2, 6 topics get 1 (1*2 + 6*1 = 8)
        it_topics_shuffled = list(IT_TOPICS)
        rng.shuffle(it_topics_shuffled)
        for idx, t in enumerate(it_topics_shuffled):
            count = 2 if idx == 0 else 1
            available = topic_pools["IT"][t]
            if len(available) < count:
                raise ValueError(f"Insufficient questions for IT topic '{t}'")
            selected.extend(rng.sample(available, count))

        # 7 Core questions across 8 Core topics: pick 7 distinct topics, 1 question each (7*1 = 7)
        core_topics_shuffled = list(CORE_TOPICS)
        rng.shuffle(core_topics_shuffled)
        chosen_core_topics = core_topics_shuffled[:7]
        for t in chosen_core_topics:
            available = topic_pools["Core"][t]
            if len(available) < 1:
                raise ValueError(f"Insufficient questions for Core topic '{t}'")
            selected.extend(rng.sample(available, 1))

    # Shuffle the final 15 questions so topics and domains are randomized
    rng.shuffle(selected)

    # Validate output question set
    validate_technical_question_set(selected, expected_domain=domain)

    return selected


def evaluate_technical_assessment(
    selected_questions: List[Dict[str, Any]],
    user_answers: Dict[int, str],
    threshold: float = DEFAULT_THRESHOLD
) -> Dict[str, Any]:
    """
    Evaluates submitted answers for a technical assessment.

    Args:
        selected_questions: List of 15 question dictionaries
        user_answers: Dict mapping question_id -> user answer string
        threshold: Cutoff percentage for strong topics (default 70.0%)

    Returns:
        Structured result dictionary with domain, overall score, domain_scores,
        topic_scores, strong_topics, weak_topics, and question details.
    """
    # Detect assessment domain
    domains_present = {q["domain"] for q in selected_questions}
    if len(domains_present) == 1:
        assessment_domain = list(domains_present)[0]
    elif domains_present == {"IT", "Core"}:
        assessment_domain = "Both"
    else:
        assessment_domain = "Unknown"

    validate_technical_question_set(selected_questions, expected_domain=assessment_domain)

    total_score = 0
    total_questions = len(selected_questions)

    domain_stats: Dict[str, Dict[str, Any]] = {}
    topic_stats: Dict[str, Dict[str, Any]] = {}
    question_details = []

    for q in selected_questions:
        qid = q["id"]
        dom = q["domain"]
        top = q["topic"]
        correct_answer = q["answer"]
        user_answer = user_answers.get(qid, None)

        is_correct = (user_answer == correct_answer) if user_answer is not None else False
        points = 1 if is_correct else 0
        total_score += points

        # Accumulate domain stats
        if dom not in domain_stats:
            domain_stats[dom] = {"score": 0, "total": 0, "percentage": 0.0}
        domain_stats[dom]["total"] += 1
        domain_stats[dom]["score"] += points

        # Accumulate topic stats
        if top not in topic_stats:
            topic_stats[top] = {"score": 0, "total": 0, "percentage": 0.0}
        topic_stats[top]["total"] += 1
        topic_stats[top]["score"] += points

        question_details.append({
            "id": qid,
            "domain": dom,
            "topic": top,
            "question": q["question"],
            "options": q["options"],
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "explanation": q["explanation"]
        })

    # Validate that domain scores sum to total_score
    sum_domain_scores = sum(d["score"] for d in domain_stats.values())
    if sum_domain_scores != total_score:
        raise ValueError(f"Domain scores sum ({sum_domain_scores}) does not match total score ({total_score})")

    # Validate that topic scores sum to total_score
    sum_topic_scores = sum(t["score"] for t in topic_stats.values())
    if sum_topic_scores != total_score:
        raise ValueError(f"Topic scores sum ({sum_topic_scores}) does not match total score ({total_score})")

    # Compute percentages
    overall_percentage = round((total_score / total_questions) * 100, 2)

    for dom, stats in domain_stats.items():
        stats["percentage"] = round((stats["score"] / stats["total"]) * 100, 2) if stats["total"] > 0 else 0.0

    strong_topics = []
    weak_topics = []

    for top, stats in topic_stats.items():
        pct = round((stats["score"] / stats["total"]) * 100, 2) if stats["total"] > 0 else 0.0
        stats["percentage"] = pct
        if pct >= threshold:
            strong_topics.append(top)
        else:
            weak_topics.append(top)

    # Sort topics alphabetically for consistent presentation
    strong_topics.sort()
    weak_topics.sort()

    return {
        "domain": assessment_domain,
        "score": total_score,
        "total": total_questions,
        "percentage": overall_percentage,
        "domain_scores": domain_stats,
        "topic_scores": topic_stats,
        "strong_topics": strong_topics,
        "weak_topics": weak_topics,
        "details": question_details
    }
