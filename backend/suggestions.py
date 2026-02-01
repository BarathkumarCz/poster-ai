def generate_design_feedback(overall_score, typography_suggestions):
    feedback = []

    if overall_score < 40:
        feedback.append("Overall hierarchy is weak — focus on clearer typography.")
    elif overall_score < 70:
        feedback.append("Design is decent but typography can be improved.")
    else:
        feedback.append("Strong visual design with good typography.")

    feedback.extend(typography_suggestions)
    return feedback
