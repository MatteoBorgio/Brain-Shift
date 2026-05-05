import pygame
from config import TIMER_BAR_FG_COLOR, TIMER_BAR_MID_EXPIRING, TIMER_BAR_ABOUT_TO_EXPIRE, TIMER_BAR_X, TIMER_BAR_Y, TIMER_BAR_WIDTH, TIMER_BAR_HEIGHT, TIMER_BAR_BG_COLOR

def draw_timer_bar(surface: pygame.Surface, remaining: float, duration: int):
    if remaining > duration * 0.6:
        color = TIMER_BAR_FG_COLOR 
    elif remaining > duration * 0.3:
        color = TIMER_BAR_MID_EXPIRING
    else:
        color = TIMER_BAR_ABOUT_TO_EXPIRE
    
    pygame.draw.rect(surface, TIMER_BAR_BG_COLOR, pygame.Rect(TIMER_BAR_X, TIMER_BAR_Y, TIMER_BAR_WIDTH, TIMER_BAR_HEIGHT), border_radius=6)
    pygame.draw.rect(surface, color, pygame.Rect(TIMER_BAR_X, TIMER_BAR_Y, color, TIMER_BAR_HEIGHT), border_radius=6)