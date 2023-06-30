import pygame

class Imagen():
    def __init__(self,coordenate,size,ruta,agrandado = True):
        self.agrandado = agrandado
        self.image_original = pygame.image.load(ruta).convert_alpha()
        self.image = pygame.transform.scale(self.image_original,size)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = coordenate
        self.size_original = size
        self.centro_original = self.rect.center
        self.size_agrandado = (size[0]+5,size[1]+5)

    def detectarPresionado(self,x,y,apretado):
        if self.rect.left < x and self.rect.right > x and self.rect.top < y and self.rect.bottom > y:
            if self.agrandado:
                self.image = pygame.transform.scale(self.image_original,self.size_agrandado)
                self.rect.center = self.centro_original
            if apretado:
                return True
        else:
            if self.agrandado:
                self.image = pygame.transform.scale(self.image_original,self.size_original)
                self.rect.center = self.centro_original
        return False