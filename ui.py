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
        y = MARGIN
    else:
        y = SCREEN_HEIGHT - CARD_HEIGHT - MARGIN

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

