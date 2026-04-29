import pygame
def draw_card(surface, trial):
	card_width = 260
	card_height = 140
	margin = 40
	screen_width, screen_height = surface.get_size()

	if getattr(trial, 'position', None) == 'TOP':
		y = margin
	else: 
		y = screen_height - card_height - margin


	x = (screen_width - card_width) // 2

	rect = pygame.Rect(x, y, card_width, card_height)
	border_radius = 24
	pygame.draw.rect(surface, (255, 255, 255), rect, border_radius=border_radius)
	pygame.draw.rect(surface, (0, 0, 0), rect, 3, border_radius=border_radius)


	font = pygame.font.SysFont(None, 72)
	letter = getattr(trial, 'letter', '?')
	number = str(getattr(trial, 'number', '?'))


	font_big = pygame.font.SysFont(None, 72)
	letter_surf = font_big.render(letter, True, (0, 0, 0))
	number_surf = font_big.render(number, True, (0, 0, 0))

	spacing = 16
	total_width = letter_surf.get_width() + spacing + number_surf.get_width()
	center_x = x + card_width // 2
	center_y = y + card_height // 2

	letter_x = center_x - total_width // 2
	number_x = letter_x + letter_surf.get_width() + spacing
	letter_rect = letter_surf.get_rect(midleft=(letter_x, center_y))
	number_rect = number_surf.get_rect(midleft=(number_x, center_y))

	surface.blit(letter_surf, letter_rect)
	surface.blit(number_surf, number_rect)
    