import pygame
from config import (
    CARD_SPACING,
    COLOR_BUTTON_TEXT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    CARD_HEIGHT,
    CARD_WIDTH,
    MARGIN,
    CARD_BORDER_COLOR,
    CARD_BORDER_RADIUS,
    CARD_TEXT_COLOR,
    HINT_COLOR,
    PADDING,
    OFFSET_X,
    BUTTON_HEIGHT,
    BUTTON_NO_X,
    BUTTON_Y,
    BUTTON_YES_X,
    BUTTON_RADIUS,
    BUTTON_WIDTH,
    COLOR_NO,
    COLOR_YES,
)

FONT_FAMILY = "segoeui,arial,helvetica"


def draw_card(surface, trial, color):
    if getattr(trial, "position", None) == "TOP":
        y = (SCREEN_HEIGHT // 2) - CARD_HEIGHT - MARGIN
    else:
        y = (SCREEN_HEIGHT // 2) + MARGIN

    x = (SCREEN_WIDTH - CARD_WIDTH) // 2

    shadow_surf = pygame.Surface((CARD_WIDTH, CARD_HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(
        shadow_surf,
        (0, 0, 0, 40),
        shadow_surf.get_rect(),
        border_radius=CARD_BORDER_RADIUS,
    )
    surface.blit(shadow_surf, (x + 6, y + 8))

    rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
    pygame.draw.rect(surface, color, rect, border_radius=CARD_BORDER_RADIUS)
    pygame.draw.rect(
        surface, CARD_BORDER_COLOR, rect, 3, border_radius=CARD_BORDER_RADIUS
    )

    letter = getattr(trial, "letter", "?")
    number = str(getattr(trial, "number", "?"))

    font = pygame.font.SysFont(FONT_FAMILY, 80, bold=True)
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


def draw_hints(surface, trial, correct_answers, max_threshold=10):
    alpha = max(0, 255 - (correct_answers * (255 // max_threshold)))
    if alpha <= 0:
        return

    font_hint = pygame.font.SysFont(FONT_FAMILY, 28, bold=True)

    card_x = (SCREEN_WIDTH - CARD_WIDTH) // 2
    hint_x = card_x + OFFSET_X + CARD_WIDTH

    if trial.position == "TOP":
        text = "NUMERO PARI?"
        card_y = (SCREEN_HEIGHT // 2) - CARD_HEIGHT - MARGIN
    else:
        text = "VOCALE?"
        card_y = (SCREEN_HEIGHT // 2) + MARGIN

    text_surface = font_hint.render(text, True, HINT_COLOR)
    text_surface.set_alpha(alpha)

    box_width = text_surface.get_width() + PADDING * 2
    box_height = text_surface.get_height() + PADDING * 2

    hint_y = card_y + (CARD_HEIGHT // 2) - (box_height // 2)

    shadow_alpha = min(alpha, 40)
    shadow_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
    pygame.draw.rect(
        shadow_surface,
        (0, 0, 0, shadow_alpha),
        shadow_surface.get_rect(),
        border_radius=8,
    )
    surface.blit(shadow_surface, (hint_x + 3, hint_y + 4))

    box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
    pygame.draw.rect(
        box_surface, (255, 255, 255, alpha), box_surface.get_rect(), border_radius=8
    )

    surface.blit(box_surface, (hint_x, hint_y))
    surface.blit(text_surface, (hint_x + PADDING, hint_y + PADDING))


def draw_results(surface, score, correct_answers, wrong_answers, total_answers):
    accuracy = 0.0
    if total_answers > 0:
        accuracy = (correct_answers / total_answers) * 100

    title_font = pygame.font.SysFont(FONT_FAMILY, 64, bold=True)
    text_font = pygame.font.SysFont(FONT_FAMILY, 38)
    small_font = pygame.font.SysFont(FONT_FAMILY, 28, italic=True)

    lines = [
        f"Punteggio: {score}",
        f"Corrette: {correct_answers}",
        f"Sbagliate: {wrong_answers}",
        f"Accuratezza: {accuracy:.1f}%",
    ]

    INT_PADDING_X = 50
    INT_PADDING_Y = 50

    content_height = sum(text_font.size(line)[1] + 15 for line in lines) + 40
    panel_width = 450 + (INT_PADDING_X * 2)
    panel_height = content_height + (INT_PADDING_Y * 2)

    panel_rect = pygame.Rect(0, 0, panel_width, panel_height)
    panel_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    shadow_surf = pygame.Surface((panel_width, panel_height), pygame.SRCALPHA)
    pygame.draw.rect(
        shadow_surf, (0, 0, 0, 50), shadow_surf.get_rect(), border_radius=20
    )
    surface.blit(shadow_surf, (panel_rect.x + 8, panel_rect.y + 10))

    pygame.draw.rect(surface, (250, 250, 250), panel_rect, border_radius=20)
    pygame.draw.rect(surface, CARD_BORDER_COLOR, panel_rect, 3, border_radius=20)

    y = panel_rect.y + INT_PADDING_Y
    for index, line in enumerate(lines):
        font = title_font if index == 0 else text_font
        text_surf = font.render(line, True, CARD_TEXT_COLOR)
        text_rect = text_surf.get_rect(
            center=(surface.get_width() // 2, y + text_surf.get_height() // 2)
        )
        surface.blit(text_surf, text_rect)
        y += text_surf.get_height() + (30 if index == 0 else 15)

    restart_surf = small_font.render(
        "Premi SHIFT + R per rigiocare", True, (100, 100, 100)
    )
    restart_rect = restart_surf.get_rect(
        center=(SCREEN_WIDTH // 2, panel_rect.bottom - INT_PADDING_Y)
    )
    surface.blit(restart_surf, restart_rect)


def draw_intro(surface):
    title_font = pygame.font.SysFont(FONT_FAMILY, 80, bold=True)
    text_font = pygame.font.SysFont(FONT_FAMILY, 34, bold=True)
    small_font = pygame.font.SysFont(FONT_FAMILY, 28)

    lines = [
        ("Brain Shift", title_font, CARD_TEXT_COLOR),
        ("", None, None),
        ("Rispondi velocemente:", text_font, (80, 80, 80)),
        ("TOP: il numero è pari?", small_font, CARD_TEXT_COLOR),
        ("BOTTOM: la lettera è una vocale?", small_font, CARD_TEXT_COLOR),
        ("", None, None),
        ("Controlli:", text_font, (80, 80, 80)),
        ("SINISTRA = NO", small_font, (200, 50, 50)),
        ("DESTRA = SI'", small_font, (50, 150, 50)),
        ("", None, None),
        ("Premi SPAZIO per iniziare", text_font, (50, 100, 200)),
    ]

    INT_PADDING_X = 60
    INT_PADDING_Y = 60

    panel_width = 600 + (INT_PADDING_X * 2)
    panel_height = 500 + (INT_PADDING_Y * 2)

    panel_rect = pygame.Rect(0, 0, panel_width, panel_height)
    panel_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    shadow_surf = pygame.Surface((panel_width, panel_height), pygame.SRCALPHA)
    pygame.draw.rect(
        shadow_surf, (0, 0, 0, 40), shadow_surf.get_rect(), border_radius=20
    )
    surface.blit(shadow_surf, (panel_rect.x + 8, panel_rect.y + 10))

    pygame.draw.rect(surface, (252, 252, 252), panel_rect, border_radius=20)
    pygame.draw.rect(surface, CARD_BORDER_COLOR, panel_rect, 3, border_radius=20)

    y = panel_rect.y + INT_PADDING_Y
    for line_text, font, color in lines:
        if line_text == "":
            y += 20
            continue
        text_surf = font.render(line_text, True, color)
        text_rect = text_surf.get_rect(
            center=(surface.get_width() // 2, y + text_surf.get_height() // 2)
        )
        surface.blit(text_surf, text_rect)
        y += text_surf.get_height() + 10


def draw_paused(surface, remaining_time):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    surface.blit(overlay, (0, 0))

    font_title = pygame.font.SysFont(FONT_FAMILY, 90, bold=True)
    font_text = pygame.font.SysFont(FONT_FAMILY, 46)
    font_small = pygame.font.SysFont(FONT_FAMILY, 32, italic=True)

    def draw_text_with_shadow(text, font, color, center_pos):
        shadow = font.render(text, True, (0, 0, 0))
        shadow_rect = shadow.get_rect(center=(center_pos[0] + 3, center_pos[1] + 3))
        surface.blit(shadow, shadow_rect)
        main_text = font.render(text, True, color)
        main_rect = main_text.get_rect(center=center_pos)
        surface.blit(main_text, main_rect)

    draw_text_with_shadow(
        "PAUSA",
        font_title,
        (255, 255, 255),
        (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100),
    )
    draw_text_with_shadow(
        f"Tempo rimanente: {remaining_time:.1f}s",
        font_text,
        (255, 200, 100),
        (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
    )
    draw_text_with_shadow(
        "Premi P per riprendere",
        font_small,
        (200, 200, 200),
        (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100),
    )


def draw_buttons(surface):
    font_btn = pygame.font.SysFont("segoeui,arial,helvetica", 28, bold=True)

    rect_no = pygame.Rect(BUTTON_NO_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    rect_si = pygame.Rect(BUTTON_YES_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

    for rect in (rect_no, rect_si):
        shadow = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.rect(
            shadow, (0, 0, 0, 40), shadow.get_rect(), border_radius=BUTTON_RADIUS
        )
        surface.blit(shadow, (rect.x + 3, rect.y + 4))

    pygame.draw.rect(surface, COLOR_NO, rect_no, border_radius=BUTTON_RADIUS)
    pygame.draw.rect(surface, COLOR_YES, rect_si, border_radius=BUTTON_RADIUS)

    surf_no = font_btn.render("NO", True, COLOR_BUTTON_TEXT)
    surf_si = font_btn.render("SÌ", True, COLOR_BUTTON_TEXT)

    surface.blit(surf_no, surf_no.get_rect(center=rect_no.center))
    surface.blit(surf_si, surf_si.get_rect(center=rect_si.center))
