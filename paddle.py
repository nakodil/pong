import pygame


class Paddle:
    def __init__(
        self,
        screen,
        width=10,
        height=100,
        color=(255, 255, 255),
        position_x=0,
        is_automatic=False,
        velocity=10,
        key_up=pygame.K_UP,
        key_down=pygame.K_DOWN,
        score=0
    ):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = position_x
        self.rect.centery = self.screen_rect.centery
        self.is_automatic = is_automatic
        self.velocity = velocity
        self.key_up = key_up
        self.key_down = key_down
        self.score = score

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def controls(self, events_keys, ball_centery):
        if self.is_automatic:
            if ball_centery > self.rect.centery:
                self.rect.y += self.velocity
            if ball_centery < self.rect.centery:
                self.rect.y -= self.velocity
        else:
            if (
                events_keys[self.key_up]
                and self.rect.top >= self.velocity
            ):
                self.rect.y -= self.velocity
            if (
                events_keys[self.key_down]
                and self.rect.bottom <= self.screen_rect.height
            ):
                self.rect.y += self.velocity
