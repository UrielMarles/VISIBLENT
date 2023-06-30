import pygame
from generales import *
class Boton():
    def __init__(self,coordenate,size,COLOR,fontSize,mensaje,borde = False,color_texto = BLACK,agrandado = True):
        self.borde = borde
        self.agrandado = agrandado
        self.coordenate = coordenate
        self.size = size
        self.COLOR = COLOR
        self.fontSize = fontSize
        self.mensaje = mensaje
        self.color_texto = color_texto
        self.__reestablecer_image()

        self.centro_original = self.rect.center
        self.size_agrandado = (self.size_original[0]+5,self.size_original[1]+5)
        
    def detectarPresionado(self,x,y,apretado):
        if self.rect.left < x and self.rect.right > x and self.rect.top < y and self.rect.bottom > y:
            if self.agrandado:
                self.image = pygame.transform.scale(self.image,self.size_agrandado)
                self.rect.size = self.size_agrandado
            if apretado:
                return True
        else:
            if self.agrandado:
                self.__reestablecer_image()
        return False
    
    def __reestablecer_image(self):
        if self.borde:
            self.image = pygame.surface.Surface((self.size[0] + 6, self.size[1] + 6))
            self.fondo = pygame.surface.Surface(self.size)
            self.rect = self.fondo.get_rect()
            self.rect.bottomleft = self.coordenate
            self.fondo.fill(self.COLOR)
            self.image.fill((0, 0, 0))
            self.image.blit(self.fondo, (3, 3))
            self.size_original = (self.size[0] + 6, self.size[1] + 6)
        else:
            self.image = pygame.surface.Surface(self.size)
            self.rect = self.image.get_rect()
            self.rect.bottomleft = self.coordenate
            self.size_original = self.size
            self.image.fill(self.COLOR)
        
        font = pygame.font.Font("fuentes/HARLOWSI.TTF", self.fontSize)
        texto_renderizado = font.render(self.mensaje, True, self.color_texto)
        text_rect = texto_renderizado.get_rect()
        text_rect.center = (self.size[0] // 2, self.size[1] // 2)
        self.image.blit(texto_renderizado, text_rect)