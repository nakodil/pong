"""
    задержка сбрасывания мяча
    объект игрового поля
        границы для коллизий
"""
import pygame  # pip install pygame
from paddle import Paddle
from ball import Ball
from score import Score

# настройка
FPS = 60
is_fullscreen = True
screen_width = 800
screen_height = 600

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(1)
pygame.mixer.music.load("assets/ball_hit.mp3")

# экран
if is_fullscreen:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()
else:
    screen = pygame.display.set_mode((screen_width, screen_height))

# игровые объекты
clock = pygame.time.Clock()
player = Paddle(screen, position_x=screen_width * 0.1)
opponent = Paddle(screen, position_x=screen_width * 0.9, is_auto=True)
player_score = Score(screen, position_x=screen_width * 0.4, owner=player)
opponent_score = Score(screen, position_x=screen_width * 0.6, owner=opponent)
ball = Ball(screen)


def main_loop():
    while True:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
        if keys[pygame.K_ESCAPE]:
            return None

        screen.fill((0, 0, 0))
        player.draw()
        opponent.draw()
        ball.draw()
        player_score.draw()
        opponent_score.draw()

        player.controls(keys, ball)
        opponent.controls(keys, ball)
        ball.update(player, opponent)
        player_score.update()
        opponent_score.update()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main_loop()
    pygame.quit()
