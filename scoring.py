def apply_answer(score: int, is_correct: bool) -> int:
    if is_correct:
        score += 10
        return score
    return max(0, (score - 5))


def apply_multiplier(score: int, streak: int):
    if streak >= 3:
        score *= 2
    elif streak >= 6:
        score *= 3
    elif streak > 9:
        score *= 4

    return score
