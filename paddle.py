import pygame


class Paddle:
    def __init__(
        self,
        screen,
        position_x=100,
        width=10,
        height=100,
        color=(255, 255, 255),
        is_auto=False,
        key_up=pygame.K_UP,
        key_down=pygame.K_DOWN,
        velocity=10,
        score=0
    ):
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.centerx = position_x
        self.rect.centery = self.screen_rect.centery
        self.key_up = key_up
        self.key_down = key_down
        self.velocity = velocity
        self.is_auto = is_auto
        self.score = score

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def controls(self, keys, ball):
        if self.is_auto:
            if (
                ball.rect.y < self.rect.y
                and self.rect.top > self.screen_rect.top
            ):
                self.rect.y -= self.velocity
            if (
                ball.rect.y > self.rect.y
                and self.rect.bottom < self.screen_rect.bottom
            ):
                self.rect.y += self.velocity
        else:
            if (
                keys[self.key_up]
                and self.rect.top > self.screen_rect.top
            ):
                self.rect.y -= self.velocity
            if (
                keys[self.key_down]
                and self.rect.bottom < self.screen_rect.bottom
            ):
                self.rect.y += self.velocity
