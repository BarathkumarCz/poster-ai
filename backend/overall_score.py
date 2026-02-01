def compute_overall_score(scores: dict, ml_score, sections: dict) -> float:
    """
    Compute one final poster quality score (0–100)
    using:
    - Rule‑based scores
    - ML‑predicted score
    - Poster structure (title / subtitle / body)
    """

    # -------------------------
    # Rule‑based average score
    # -------------------------
    total = 0
    count = 0

    for value in scores.values():
        if isinstance(value, (int, float)):
            total += value
            count += 1

    rule_avg = total / count if count > 0 else 0

    # -------------------------
    # Structure bonus
    # -------------------------
    structure_bonus = 0

    if sections.get("title"):
        structure_bonus += 5
    if sections.get("subtitle"):
        structure_bonus += 3
    if sections.get("body"):
        structure_bonus += 2

    # -------------------------
    # ML contribution
    # -------------------------
    ml_component = ml_score if ml_score is not None else rule_avg

    # -------------------------
    # Final weighted score
    # -------------------------
    final_score = (
        0.6 * rule_avg +
        0.3 * ml_component +
        0.1 * structure_bonus * 10
    )

    return round(min(final_score, 100), 2)

