import pygame
from generales import *
class Boton():
    def __init__(self,coordenate,size,COLOR,fontSize,mensaje,borde = False,color_texto = BLACK,agrandado = True):
        if borde:
            self.image = pygame.surface.Surface((size[0] + 6, size[1] + 6))
            self.fondo = pygame.surface.Surface(size)
            self.rect = self.fondo.get_rect()
            self.rect.bottomleft = coordenate
            self.fondo.fill(COLOR)
            self.image.fill((0, 0, 0))
            self.image.blit(self.fondo, (3, 3))
            self.size_original = (size[0] + 6, size[1] + 6)
        else:
            self.image = pygame.surface.Surface(size)
            self.rect = self.image.get_rect()
            self.rect.bottomleft = coordenate
            self.image.fill(COLOR)
        font = pygame.font.Font("fuentes/HARLOWSI.TTF", fontSize)
        texto_renderizado = font.render(mensaje, True, color_texto)
        text_rect = texto_renderizado.get_rect()
        text_rect.center = (size[0] // 2, size[1] // 2)
        self.image.blit(texto_renderizado, text_rect)
        self.centro_original = self.rect.center
        
    def detectarPresionado(self,x,y,apretado):
        if apretado and self.rect.left < x and self.rect.right > x and self.rect.top < y and self.rect.bottom > y:
            return True
        return False