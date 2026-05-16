def apply_answer(score: int, is_correct: bool) -> int:
    if is_correct:
        score += 10
        return score
    return max(0, (score - 5))



def apply_multiplier(score: int, streak: int):
    if streak > 3:
        score += streak * 10
    elif streak > 6:
        score += streak * 20
    elif streak > 9:
        score += streak * 40

    return score
