import pygame
from config import (
    SCREEN_WIDTH,
    TIMER_BAR_FG_COLOR,
    TIMER_BAR_MID_EXPIRING,
    TIMER_BAR_ABOUT_TO_EXPIRE,
    TIMER_BAR_X,
    TIMER_BAR_Y,
    TIMER_BAR_WIDTH,
    TIMER_BAR_HEIGHT,
    TIMER_BAR_BG_COLOR,
    TIMER_BORDER_RADIUS,
)


def draw_timer_bar(surface: pygame.Surface, remaining: float, duration: int):
    if remaining > duration * 0.6:
        color = TIMER_BAR_FG_COLOR
    elif remaining > duration * 0.3:
        color = TIMER_BAR_MID_EXPIRING
    else:
        color = TIMER_BAR_ABOUT_TO_EXPIRE

    pygame.draw.rect(
        surface,
        TIMER_BAR_BG_COLOR,
        pygame.Rect(TIMER_BAR_X, TIMER_BAR_Y, TIMER_BAR_WIDTH, TIMER_BAR_HEIGHT),
        border_radius=TIMER_BORDER_RADIUS,
    )
    pygame.draw.rect(
        surface,
        color,
        pygame.Rect(TIMER_BAR_X, TIMER_BAR_Y, TIMER_BAR_WIDTH, TIMER_BAR_HEIGHT),
        border_radius=TIMER_BORDER_RADIUS,
    )


def draw_timer_text(surface: pygame.Surface, remaining: float, expired: bool):
    font = pygame.font.Font(None, 36)
    y = TIMER_BAR_Y + TIMER_BAR_HEIGHT + 10
    remaining_seconds = int(remaining)

    if expired:
        text = "Tempo scaduto!"
        surf = font.render(text, True, (255, 0, 0))
    else:
        text = str(remaining_seconds)
        surf = font.render(text, True, (255, 255, 255))

    rect = surf.get_rect(centerx=SCREEN_WIDTH // 2, top=y)
    surface.blit(surf, rect)
