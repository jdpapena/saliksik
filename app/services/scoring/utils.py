def calculate_stars(score: int, max_score: int) -> int:
    percentage = (score / max_score) * 100

    if percentage >= 90:
        return 5
    elif percentage >= 75:
        return 4
    elif percentage >= 60:
        return 3
    elif percentage >= 40:
        return 2
    return 1