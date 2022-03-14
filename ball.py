import pygame


class Ball:
    def __init__(
        self,
        screen,
        width=10,
        height=10,
        color=(255, 255, 255),
        velocity_x=10,
        velocity_y=10
    ):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.go_to_center()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def go_to_center(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def controls(self, player, opponent):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        if self.rect.left < 0:
            opponent.score += 1
            self.go_to_center()
        if self.rect.right > self.screen_rect.width:
            player.score += 1
            self.go_to_center()
        if self.rect.top < 0 or self.rect.bottom > self.screen_rect.height:
            self.velocity_y *= -1
        if (
            # хардкод, что если > 2 ракеток?
            self.rect.colliderect(player.rect)
            or self.rect.colliderect(opponent.rect)
        ):
            self.velocity_x *= -1
            self.velocity_y *= -1
