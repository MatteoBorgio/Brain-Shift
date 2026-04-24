def is_even(number: int) -> bool:
    return number % 2 == 0 

def is_vowel(letter: str) -> bool:
    return letter.lower() in ["a", "e", "i", "o", "u"]

def compute_expected_answer(position: str, letter: str, number: int) -> bool:
    if position.lower() == "top":
        return is_even(number)
    else:
        return is_vowel(letter)
    