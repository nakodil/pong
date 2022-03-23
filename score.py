import pygame

pygame.font.init()
myfont = pygame.font.Font('assets/PressStart2P-Regular.ttf', 32)


class Score:
    def __init__(
        self,
        screen,
        position_x=0,
        position_y=30,
        color=(255, 255, 255),
        owner=None
    ):
        self.screen = screen
        self.owner = owner
        self.color = color
        self.image = myfont.render(str(self.owner.score), False, self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = position_x
        self.rect.centery = position_y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.image = myfont.render(str(self.owner.score), False, self.color)
