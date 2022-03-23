import pygame
import random


class Ball:
    def __init__(
        self,
        screen,
        width=10,
        height=10,
        color=(255, 255, 255),
        velocity_x=5,
        velocity_y=5,
        player=None,
        opponent=None,
    ):
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def ball_to_center(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.velocity_x *= random.choice((-1, 1))
        self.velocity_y *= random.choice((-1, 1))

    def update(self, player, opponent):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # коллизии с верхом и низом экрана
        if self.rect.top <= self.screen_rect.top:
            self.velocity_y *= -1
            pygame.mixer.music.play()
        if self.rect.bottom >= self.screen_rect.bottom:
            self.velocity_y *= -1
            pygame.mixer.music.play()

        # коллизии с ракетками
        if (
            self.rect.colliderect(player.rect)
            or self.rect.colliderect(opponent.rect)
        ):
            self.velocity_x *= -1
            self.velocity_y *= -1
            pygame.mixer.music.play()

        # гол
        if self.rect.right >= self.screen_rect.right:
            player.score += 1
            self.ball_to_center()
        if self.rect.left <= self.screen_rect.left:
            opponent.score += 1
            self.ball_to_center()
