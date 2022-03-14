"""
    TODO:
        класс главного окна!
        включить полноэкранный режим в процессе игры
"""

import pygame  # pip install pygame
from paddle import Paddle
from ball import Ball
from score import Score

# настройка
FPS = 60
is_fullscreen = False
screen_width = 800
screen_height = 600

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND = BLACK

# инициализация и создание объектов
pygame.init()
if is_fullscreen:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()
else:
    screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

player = Paddle(
    screen,
    position_x=screen_width * 0.1,
)

opponent = Paddle(
    screen,
    position_x=screen_width * 0.9,
    is_automatic=True,
)

ball = Ball(screen)

player_score = Score(
    screen,
    position_x=screen_width * 0.4,
    owner=player
)

opponent_score = Score(
    screen,
    position_x=screen_width * 0.6,
    owner=opponent
)

# главный цикл игры
game = True
while game:
    events_all = pygame.event.get()
    events_keys = pygame.key.get_pressed()

    for event in events_all:
        if event.type == pygame.QUIT:
            game = False
    if events_keys[pygame.K_ESCAPE]:
        game = False

    screen.fill(BACKGROUND)
    ball.draw()
    ball.controls(player, opponent)
    player.draw()
    player.controls(events_keys, ball.rect.centery)
    opponent.draw()
    opponent.controls(events_keys, ball.rect.centery)
    player_score.update()
    opponent_score.update()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
