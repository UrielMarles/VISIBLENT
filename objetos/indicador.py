import pygame

class Indicador():
    def __init__(self,ciego):
        self.size = (100,100)
        if ciego:
            self.image = pygame.transform.scale(pygame.image.load("sprites\MENUS\LOGO.png").convert_alpha(),self.size)
        else:
            self.image = pygame.transform.scale(pygame.image.load("sprites/MENUS/LOGO_SIN_TACHAR.png").convert_alpha(),self.size)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,100)