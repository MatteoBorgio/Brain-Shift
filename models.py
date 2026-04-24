from dataclasses import dataclass

@dataclass
class Trial:
    position: str
    letter: str
    number: int
    expected_answer: bool
    user_answer: bool | None = None
    is_correct: bool = False