import pygame
from scoring import apply_answer
from ui import (
    draw_card,
    draw_results,
    draw_hints,
    draw_intro,
    draw_paused,
    draw_buttons,
    draw_current_score,
)
from generator import generate_trial
from config import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    FPS,
    SCREEN_BG_COLOR,
    COUNTDOWN,
    CARD_RECT_COLOR_WRONG,
    CARD_RECT_BASE_COLOR,
    CARD_RECT_COLOR_CORRECT,
    FEEDBACK_DURATION,
    BUTTON_YES_X,
    BUTTON_NO_X,
    BUTTON_Y,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
)
from random import Random
from time import time
from state import State
from timer import draw_timer_bar, draw_timer_text

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brain Shift")
clock = pygame.time.Clock()

score = 0
correct_answers = 0
wrong_answers = 0
total_answers = 0
feedback_end_time = 0
pause_start_time = 0


def reset_game(
    score,
    correct_answers,
    wrong_answers,
    total_answers,
    start_time,
    state,
    active_color,
):
    start_time = time()
    score = 0
    correct_answers = 0
    wrong_answers = 0
    total_answers = 0
    state = State.PLAYING
    active_color = CARD_RECT_BASE_COLOR
    return (
        score,
        correct_answers,
        wrong_answers,
        total_answers,
        start_time,
        state,
        active_color,
    )


running = True
start_time = time()
state = State.INTRO
rng = Random()
trial = generate_trial(rng)
active_color = CARD_RECT_BASE_COLOR
remaining_time = COUNTDOWN

while running:
    current_time_ticks = pygame.time.get_ticks()

    if state == State.PLAYING:
        if current_time_ticks > feedback_end_time:
            active_color = CARD_RECT_BASE_COLOR

        elapsed_time = time() - start_time
        remaining_time = max(0, COUNTDOWN - elapsed_time)

        if remaining_time <= 0:
            state = State.RESULTS

    user_answer = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif state == State.INTRO:
                if event.key == pygame.K_SPACE:
                    start_time = time()
                    state = State.PLAYING

            elif state == State.PAUSED:
                if event.key == pygame.K_p:
                    pause_duration = time() - pause_start_time
                    start_time += pause_duration
                    state = State.PLAYING

            elif state == State.PLAYING:
                if event.key == pygame.K_p:
                    pause_start_time = time()
                    state = State.PAUSED

                elif event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                    user_answer = event.key == pygame.K_RIGHT

            elif state == State.RESULTS:
                if event.key == pygame.K_r and (event.mod & pygame.KMOD_SHIFT):
                    (
                        score,
                        correct_answers,
                        wrong_answers,
                        total_answers,
                        start_time,
                        state,
                        active_color,
                    ) = reset_game(
                        score,
                        correct_answers,
                        wrong_answers,
                        total_answers,
                        start_time,
                        state,
                        active_color,
                    )

        elif event.type == pygame.MOUSEBUTTONDOWN and state == State.PLAYING:
            if event.button == 1:
                mouse_pos = event.pos
                rect_no = pygame.Rect(
                    BUTTON_NO_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT
                )
                rect_si = pygame.Rect(
                    BUTTON_YES_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT
                )

                if rect_si.collidepoint(mouse_pos):
                    user_answer = True
                elif rect_no.collidepoint(mouse_pos):
                    user_answer = False

    if state == State.PLAYING and user_answer is not None:
        is_correct = user_answer == trial.expected_answer

        if is_correct:
            correct_answers += 1
            active_color = CARD_RECT_COLOR_CORRECT
        else:
            wrong_answers += 1
            active_color = CARD_RECT_COLOR_WRONG

        feedback_end_time = current_time_ticks + FEEDBACK_DURATION
        total_answers += 1
        score = apply_answer(score, is_correct)
        trial = generate_trial(rng)

    screen.fill(SCREEN_BG_COLOR)

    if state == State.INTRO:
        draw_intro(screen)

    elif state == State.PAUSED:
        draw_paused(screen, remaining_time)

    elif state == State.PLAYING:
        draw_card(screen, trial, active_color)
        draw_hints(screen, trial, correct_answers)
        draw_buttons(screen)
        draw_timer_bar(screen, remaining_time, COUNTDOWN)
        draw_timer_text(screen, remaining_time, remaining_time <= 0)
        draw_current_score(screen, score)

    elif state == State.RESULTS:
        draw_results(
            screen,
            score=score,
            correct_answers=correct_answers,
            wrong_answers=wrong_answers,
            total_answers=total_answers,
        )

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
