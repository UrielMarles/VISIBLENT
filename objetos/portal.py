import pygame

class Portal():
    def __init__(self,coordenate,personaje):
        self.tamaño = 90
        self.size = (90,90)
        self.image_original = pygame.image.load("sprites\GENERALES\AGUJERO_NEGRO.png").convert_alpha()
        self.image = pygame.transform.scale(self.image_original,self.size)
        self.rect = self.image.get_rect()
        self.coordenate = coordenate
        self.rect.center = coordenate
        self.rotacion = 0
        self.velocidad = 5
        self.cantidad_achicado = 1
        self.centro_real = self.rect.center
        self.personaje = personaje

    def __girado_achicado(self,frame50):
        if frame50:
            self.rotacion += self.velocidad 
            if self.rotacion > 200 or self.rotacion < -200:
                self.velocidad = -(self.velocidad)
            self.tamaño += self.cantidad_achicado
            if self.tamaño < 50 or self.tamaño > 90:
                self.cantidad_achicado = -(self.cantidad_achicado)
            self.size = (self.tamaño,self.tamaño)
            self.image = pygame.transform.scale(self.image_original, self.size)
            self.image = pygame.transform.rotate(self.image, self.rotacion)
            self.rect = self.image.get_rect()
            self.rect.center = self.coordenate
    
    def detectar_colision(self):
        if self.rect.colliderect(self.personaje.rect):
            self.personaje.ganando = True
            self.personaje.centro_real = self.centro_real

    def movimiento_normal(self,frame50):
        self.__girado_achicado(frame50)
        self.detectar_colision()

