import pygame

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


class Score:
    def __init__(
        self,
        screen,
        width=10,
        height=100,
        color=(255, 255, 255),
        # хардкод, нужно относительное от ширины экрана
        position_x=0,
        position_y=50,
        owner=None
    ):
        self.screen = screen
        self.owner = owner
        self.score = str(self.owner.score)
        self.textsurface = myfont.render(self.score, False, (255, 255, 255))
        self.rect = self.textsurface.get_rect()
        self.rect.centerx = position_x
        self.rect.centery = position_y

    def update(self):
        self.score = str(self.owner.score)
        self.textsurface = myfont.render(self.score, False, (255, 255, 255))
        self.screen.blit(self.textsurface, self.rect)
