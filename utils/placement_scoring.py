"""
Placement Scoring Module
Provides the deterministic Weighted Placement Probability Model for the student-facing assessment.

Formula:
Placement Probability =
    0.35 * Live Aptitude Percentage +
    0.35 * Live Technical Percentage +
    0.15 * SSC Percentage +
    0.15 * HSC Percentage

Live Assessment Contribution: 70% (35% Aptitude + 35% Technical)
Academic Indicators Contribution: 30% (15% SSC + 15% HSC)
"""

def calculate_weighted_placement_probability(
    aptitude_percentage: float,
    technical_percentage: float,
    ssc_percentage: float,
    hsc_percentage: float
) -> float:
    """
    Calculates the deterministic weighted placement probability.

    Args:
        aptitude_percentage: Percentage scored on the live 15-question aptitude assessment (0.0 to 100.0)
        technical_percentage: Percentage scored on the live 15-question technical assessment (0.0 to 100.0)
        ssc_percentage: 10th standard board percentage (0.0 to 100.0)
        hsc_percentage: 12th standard board percentage (0.0 to 100.0)

    Returns:
        Weighted placement probability rounded to 2 decimal places, bounded between 0.0 and 100.0.
    """
    apt = float(aptitude_percentage)
    tech = float(technical_percentage)
    ssc = float(ssc_percentage)
    hsc = float(hsc_percentage)

    weighted_prob = (
        (0.35 * apt) +
        (0.35 * tech) +
        (0.15 * ssc) +
        (0.15 * hsc)
    )

    bounded_prob = max(0.0, min(100.0, weighted_prob))
    return round(bounded_prob, 2)
