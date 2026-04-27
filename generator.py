from models import Trial
from rules import compute_expected_answer


def generate_trial(rng) -> Trial:
    capital_vowels = ["A", "E", "I", "O", "U"]
    possible_positions = ["TOP", "BOTTOM"]
    position = rng.choice(possible_positions)
    letter = rng.choice(capital_vowels)
    number = rng.randint(1, 9)
    expected_answer = compute_expected_answer(position, letter, number)
    return Trial(
        position=position, letter=letter, number=number, expected_answer=expected_answer
    )
