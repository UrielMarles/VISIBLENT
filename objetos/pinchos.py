import pygame

class Pinchos():
    def __init__(self,coordenate,size,direccion,cantidad):
        self.ancho = size[0] * cantidad
        self.alto = size[1]
        self.pincho = pygame.transform.scale(pygame.image.load("sprites\GENERALES\PINCHO.png").convert_alpha(),size)
        self.fondoPinchos = pygame.Surface((self.ancho,self.alto),pygame.SRCALPHA)
        self.fondoPinchos.fill((0,0,0,0))
        for i in range(0,cantidad):
            self.fondoPinchos.blit(self.pincho,(i*size[0],0))
        self.image = self.fondoPinchos
        match direccion:
            case "d":
                self.image = pygame.transform.rotate(self.image,180)
            case "l":
                self.image = pygame.transform.rotate(self.image,90)
            case "r":
                self.image = pygame.transform.rotate(self.image,270)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = coordenate
        self.es_letal = True
        self.se_atravieza = False