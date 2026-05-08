import pygame
from config import (
    CARD_SPACING,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    CARD_HEIGHT,
    CARD_WIDTH,
    MARGIN,
    CARD_BORDER_COLOR,
    CARD_RECT_COLOR,
    CARD_BORDER_RADIUS,
    CARD_TEXT_COLOR,
)


def draw_card(surface, trial):
    if getattr(trial, "position", None) == "TOP":
        y = (SCREEN_HEIGHT // 2) - CARD_HEIGHT - MARGIN
    else:
        y = (SCREEN_HEIGHT // 2) + MARGIN

    x = (SCREEN_WIDTH - CARD_WIDTH) // 2

    rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
    pygame.draw.rect(surface, CARD_RECT_COLOR, rect, border_radius=CARD_BORDER_RADIUS)
    pygame.draw.rect(
        surface, CARD_BORDER_COLOR, rect, 3, border_radius=CARD_BORDER_RADIUS
    )

    letter = getattr(trial, "letter", "?")
    number = str(getattr(trial, "number", "?"))

    font = pygame.font.SysFont(None, 72)
    letter_surf = font.render(letter, True, CARD_TEXT_COLOR)
    number_surf = font.render(number, True, CARD_TEXT_COLOR)

    total_width = letter_surf.get_width() + CARD_SPACING + number_surf.get_width()
    center_x = x + CARD_WIDTH // 2
    center_y = y + CARD_HEIGHT // 2

    letter_x = center_x - total_width // 2
    number_x = letter_x + letter_surf.get_width() + CARD_SPACING
    letter_rect = letter_surf.get_rect(midleft=(letter_x, center_y))
    number_rect = number_surf.get_rect(midleft=(number_x, center_y))

    surface.blit(letter_surf, letter_rect)
    surface.blit(number_surf, number_rect)


def draw_results(surface, score, correct_answers, wrong_answers, total_answers):
    accuracy = 0.0
    if total_answers > 0:
        accuracy = (correct_answers / total_answers) * 100

    title_font = pygame.font.SysFont(None, 64)
    text_font = pygame.font.SysFont(None, 42)
    lines = [
        f"Punteggio: {score}",
        f"Corrette: {correct_answers}",
        f"Sbagliate: {wrong_answers}",
        f"Accuratezza: {accuracy:.1f}%",
        "Premi R per rigiocare",
    ]

    total_height = sum(text_font.size(line)[1] + 12 for line in lines)
    y = (surface.get_height() - total_height) // 2

    for index, line in enumerate(lines):
        font = title_font if index == 0 else text_font
        text_surf = font.render(line, True, CARD_TEXT_COLOR)
        text_rect = text_surf.get_rect(center=(surface.get_width() // 2, y + text_surf.get_height() // 2))
        surface.blit(text_surf, text_rect)
        y += text_surf.get_height() + 12

