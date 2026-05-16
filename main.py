import pygame
from scoring import apply_answer, apply_multiplier
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
)
from random import Random
from time import time
from state import State
from timer import draw_timer_bar, draw_timer_text
from input_handler import handle_inputs

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
    score=0,
    correct_answers=0,
    wrong_answers=0,
    total_answers=0,
    start_time=0,
    state=None,
    active_color=None,
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
streak = 0
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

    def trigger_reset():
        return reset_game(
            score,
            correct_answers,
            wrong_answers,
            total_answers,
            start_time,
            state,
            active_color,
        )

    inputs = handle_inputs(state, start_time, pause_start_time, trigger_reset)

    running = inputs["running"]
    state = inputs["state"]
    start_time = inputs["start_time"]
    pause_start_time = inputs["pause_start_time"]
    user_answer = inputs["user_answer"]

    if inputs["reset_data"] is not None:
        (
            score,
            correct_answers,
            wrong_answers,
            total_answers,
            start_time,
            state,
            active_color,
        ) = inputs["reset_data"]
        streak = 0

    if state == State.PLAYING and user_answer is not None:
        is_correct = user_answer == trial.expected_answer

        if is_correct:
            correct_answers += 1
            streak += 1
            active_color = CARD_RECT_COLOR_CORRECT
        else:
            wrong_answers += 1
            streak = 0
            active_color = CARD_RECT_COLOR_WRONG

        feedback_end_time = current_time_ticks + FEEDBACK_DURATION
        total_answers += 1
        score = apply_answer(score, is_correct)
        score = apply_multiplier(score, streak)
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
