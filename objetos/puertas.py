import pygame
from generales import *

class Puertas():
    def __init__(self,coordenate,size):
        self.image = pygame.surface.Surface(size)
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        primer_cuadrado = (size[0]-10,size[1]-10)
        #dibuja el bode
        pygame.draw.rect(self.image, BLACK, (self.rect.x,self.rect.y,size[0],size[1]), 3)
        #dibua el cuadrado de adentro
        pygame.draw.rect(self.image, BLACK, (self.rect.x+5, self.rect.y+5,primer_cuadrado[0],primer_cuadrado[1]), 3)
        self.rect.bottomleft = coordenate
        self.es_letal = False
        self.se_atravieza = False
        self.arriba_derecha = True

        