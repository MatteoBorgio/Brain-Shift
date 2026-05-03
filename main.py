import pygame
from scoring import apply_answer
from ui import draw_card
from generator import generate_trial
from config import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, SCREEN_BG_COLOR
import random

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

running = True
rng = random.Random()
trial = generate_trial(rng)
while running:
    screen.fill(SCREEN_BG_COLOR)
    draw_card(screen, trial)

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

                print(is_correct)
                print(score)
                trial = generate_trial(rng)

    pygame.display.flip()
    clock.tick(FPS)
