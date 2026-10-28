"""
Aptitude Assessment Utility Module
Provides question selection, scoring, topic diagnostics, and data validation
for the live 15-question aptitude assessment.
"""

import random
from typing import List, Dict, Any, Optional

try:
    from data.aptitude_questions import APTITUDE_QUESTIONS
except ImportError:
    from ..data.aptitude_questions import APTITUDE_QUESTIONS

# Standard category quota for 15-question assessment
CATEGORY_QUOTA = {
    "Quantitative Aptitude": 4,
    "Logical Reasoning": 4,
    "Verbal Ability": 4,
    "Data Interpretation": 3
}

VALID_CATEGORIES = set(CATEGORY_QUOTA.keys())
STRONG_THRESHOLD = 70.0  # Percentage threshold for strong topics


def validate_question(question: Dict[str, Any]) -> bool:
    """
    Validates the structure and content of a single question dictionary.
    Raises ValueError with description if invalid.
    """
    required_keys = {"id", "category", "question", "options", "answer", "explanation"}
    missing = required_keys - set(question.keys())
    if missing:
        raise ValueError(f"Question missing required keys: {missing}")

    if not isinstance(question["id"], int):
        raise ValueError(f"Question ID must be integer, got {type(question['id'])}")

    if question["category"] not in VALID_CATEGORIES:
        raise ValueError(f"Invalid category '{question['category']}'. Must be one of {VALID_CATEGORIES}")

    if not isinstance(question["question"], str) or not question["question"].strip():
        raise ValueError(f"Question text cannot be empty for Q{question['id']}")

    options = question["options"]
    if not isinstance(options, list) or len(options) != 4:
        raise ValueError(f"Question {question['id']} must have exactly 4 options, found {len(options) if isinstance(options, list) else type(options)}")

    if not all(isinstance(opt, str) and opt.strip() for opt in options):
        raise ValueError(f"All options must be non-empty strings in Q{question['id']}")

    if question["answer"] not in options:
        raise ValueError(f"Answer '{question['answer']}' not found in options {options} for Q{question['id']}")

    if not isinstance(question["explanation"], str) or not question["explanation"].strip():
        raise ValueError(f"Explanation cannot be empty for Q{question['id']}")

    return True


def validate_question_set(questions: List[Dict[str, Any]]) -> bool:
    """
    Validates a set of 15 selected questions for an assessment attempt.
    """
    if not isinstance(questions, list):
        raise ValueError("Questions must be a list")

    if len(questions) != 15:
        raise ValueError(f"Assessment must contain exactly 15 questions, got {len(questions)}")

    seen_ids = set()
    category_counts = {cat: 0 for cat in VALID_CATEGORIES}

    for q in questions:
        validate_question(q)
        qid = q["id"]
        if qid in seen_ids:
            raise ValueError(f"Duplicate question ID {qid} found in selected set")
        seen_ids.add(qid)
        category_counts[q["category"]] += 1

    for cat, expected in CATEGORY_QUOTA.items():
        if category_counts[cat] != expected:
            raise ValueError(f"Category '{cat}' has {category_counts[cat]} questions, expected {expected}")

    return True


def select_assessment_questions(
    question_bank: Optional[List[Dict[str, Any]]] = None,
    random_seed: Optional[int] = None
) -> List[Dict[str, Any]]:
    """
    Selects 15 random questions from the question bank following the quota:
    - Quantitative Aptitude: 4 questions
    - Logical Reasoning: 4 questions
    - Verbal Ability: 4 questions
    - Data Interpretation: 3 questions

    Randomizes selection each time and validates the final set.
    """
    if question_bank is None:
        question_bank = APTITUDE_QUESTIONS

    if random_seed is not None:
        rng = random.Random(random_seed)
    else:
        rng = random.Random()

    # Partition question bank by category
    category_pools: Dict[str, List[Dict[str, Any]]] = {cat: [] for cat in VALID_CATEGORIES}
    for q in question_bank:
        if q["category"] in category_pools:
            category_pools[q["category"]].append(q)

    # Check sufficient questions in each category
    for cat, quota in CATEGORY_QUOTA.items():
        if len(category_pools[cat]) < quota:
            raise ValueError(
                f"Question bank has insufficient questions for '{cat}': "
                f"available {len(category_pools[cat])}, required {quota}"
            )

    selected: List[Dict[str, Any]] = []
    for cat, quota in CATEGORY_QUOTA.items():
        sampled = rng.sample(category_pools[cat], quota)
        selected.extend(sampled)

    # Shuffle selected questions so categories are intermixed
    rng.shuffle(selected)

    # Validate final 15-question set
    validate_question_set(selected)

    return selected


def evaluate_assessment(
    selected_questions: List[Dict[str, Any]],
    user_answers: Dict[int, str],
    strong_threshold: float = STRONG_THRESHOLD
) -> Dict[str, Any]:
    """
    Evaluates user answers against the selected assessment questions.

    Args:
        selected_questions: List of 15 question dictionaries
        user_answers: Dict mapping question_id -> user's selected answer string
        strong_threshold: Percentage cutoff for strong topics (default 70.0%)

    Returns:
        Structured result dictionary containing total score, percentage,
        category-wise scores, strong topics, weak topics, and detailed feedback.
    """
    validate_question_set(selected_questions)

    total_questions = len(selected_questions)
    total_score = 0

    category_stats = {
        cat: {"score": 0, "total": 0, "percentage": 0.0}
        for cat in CATEGORY_QUOTA.keys()
    }

    question_details = []

    for q in selected_questions:
        qid = q["id"]
        cat = q["category"]
        correct_answer = q["answer"]
        user_answer = user_answers.get(qid, None)

        is_correct = (user_answer == correct_answer) if user_answer is not None else False
        points = 1 if is_correct else 0

        total_score += points
        category_stats[cat]["total"] += 1
        category_stats[cat]["score"] += points

        question_details.append({
            "id": qid,
            "category": cat,
            "question": q["question"],
            "options": q["options"],
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "explanation": q["explanation"]
        })

    # Verify category scores add up exactly to total score
    sum_cat_scores = sum(stats["score"] for stats in category_stats.values())
    if sum_cat_scores != total_score:
        raise ValueError(f"Category scores sum ({sum_cat_scores}) does not match total score ({total_score})")

    # Calculate percentages and identify strong / weak topics
    overall_percentage = round((total_score / total_questions) * 100, 2)

    strong_topics = []
    weak_topics = []

    for cat, stats in category_stats.items():
        if stats["total"] > 0:
            stats["percentage"] = round((stats["score"] / stats["total"]) * 100, 2)
        else:
            stats["percentage"] = 0.0

        if stats["percentage"] >= strong_threshold:
            strong_topics.append(cat)
        else:
            weak_topics.append(cat)

    return {
        "score": total_score,
        "total": total_questions,
        "percentage": overall_percentage,
        "category_scores": category_stats,
        "strong_topics": strong_topics,
        "weak_topics": weak_topics,
        "details": question_details
    }
