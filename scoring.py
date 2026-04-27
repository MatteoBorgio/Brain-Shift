def apply_answer(score: int, is_correct: bool) -> int:
    if is_correct:
        score += 10
        return score
    return max(0, (score - 5))
