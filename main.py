import pygame
from scoring import apply_answer
from ui import draw_card, draw_results
from generator import generate_trial
from config import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, SCREEN_BG_COLOR, COUNTDOWN
from random import Random
from time import time
from state import State
from timer import draw_timer_bar, draw_timer_text

# Inizializzazione di pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brain Shift")
clock = pygame.time.Clock()

# Contatori
score = 0
correct_answers = 0
wrong_answers = 0
total_answers = 0


# Funzioni utili
def reset_game(score, correct_answers, wrong_answers, total_answers, start_time, state):
    start_time = time()
    score = 0
    correct_answers = 0
    wrong_answers = 0
    total_answers = 0
    state = State.PLAYING
    return score, correct_answers, wrong_answers, total_answers, start_time, state


running = True
start_time = time()
state = State.PLAYING
rng = Random()
trial = generate_trial(rng)
while running:
    if state == State.PLAYING:
        screen.fill(SCREEN_BG_COLOR)
        draw_card(screen, trial)

        elapsed_time = time() - start_time
        remaining_time = COUNTDOWN - elapsed_time

        draw_timer_bar(screen, remaining_time, COUNTDOWN)
        draw_timer_text(screen, remaining_time, remaining_time <= 0)

        if elapsed_time >= COUNTDOWN:
            state = State.RESULTS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                    user_answer = event.key == pygame.K_RIGHT
                    is_correct = user_answer == trial.expected_answer
                    if is_correct:
                        correct_answers += 1
                    else:
                        wrong_answers += 1
                    total_answers += 1
                    score = apply_answer(score, is_correct)

                    trial = generate_trial(rng)
    else:
        screen.fill(SCREEN_BG_COLOR)
        draw_results(screen, score, correct_answers, wrong_answers, total_answers)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and event.mod & pygame.KMOD_SHIFT:
                    (
                        score,
                        correct_answers,
                        wrong_answers,
                        total_answers,
                        start_time,
                        state,
                    ) = reset_game(
                        score,
                        correct_answers,
                        wrong_answers,
                        total_answers,
                        start_time,
                        state,
                    )

    pygame.display.flip()
    clock.tick(FPS)
