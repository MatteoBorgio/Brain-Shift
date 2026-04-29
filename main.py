import pygame 
from ui import draw_card
from generator import generate_trial
import random
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
FPS           = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brain Shift")
clock = pygame.time.Clock()

running = True
rng = random.Random()
trial = generate_trial(rng)
draw_card(screen, trial)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    
    pygame.display.flip()
    clock.tick(60)


