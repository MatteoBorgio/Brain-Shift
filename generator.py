from models import Trial
from rules import compute_expected_answer
from random import choices


def generate_trial(rng) -> Trial:
    capital_vowels = ["A", "E", "I", "O", "U"]
    capital_consonant =  ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
              'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    possibile_consonant = choices(capital_consonant, k=5)
    possible_letter = capital_vowels + possibile_consonant
    possible_positions = ["TOP", "BOTTOM"]
    position = rng.choice(possible_positions)
    letter = rng.choice(possible_letter)
    number = rng.randint(1, 9)
    expected_answer = compute_expected_answer(position, letter, number)
    return Trial(
        position=position, letter=letter, number=number, expected_answer=expected_answer
    )
