import pygame
from time import time
from state import State
from config import BUTTON_NO_X, BUTTON_YES_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT


def handle_inputs(state, start_time, pause_start_time, reset_callback):
    running = True
    user_answer = None
    next_state = state
    next_start_time = start_time
    next_pause_start_time = pause_start_time
    reset_data = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif state == State.INTRO:
                if event.key == pygame.K_SPACE:
                    next_start_time = time()
                    next_state = State.PLAYING

            elif state == State.PAUSED:
                if event.key == pygame.K_p:
                    pause_duration = time() - pause_start_time
                    next_start_time = start_time + pause_duration
                    next_state = State.PLAYING

            elif state == State.PLAYING:
                if event.key == pygame.K_p:
                    next_pause_start_time = time()
                    next_state = State.PAUSED
                elif event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                    user_answer = event.key == pygame.K_RIGHT

            elif state == State.RESULTS:
                if event.key == pygame.K_r and (event.mod & pygame.KMOD_SHIFT):
                    reset_data = reset_callback()
                    next_state = State.PLAYING

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

    return {
        "running": running,
        "state": next_state,
        "start_time": next_start_time,
        "pause_start_time": next_pause_start_time,
        "user_answer": user_answer,
        "reset_data": reset_data,
    }
