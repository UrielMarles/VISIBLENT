import pygame

class Llaves():
    def __init__(self, coordenate, personaje):
        self.size = (50, 50)
        self.image_original = pygame.transform.scale(pygame.image.load("sprites/GENERALES/LLAVES/LLAVE_AMARILLA.png").convert_alpha(), self.size)
        self.image = pygame.transform.scale(pygame.image.load("sprites/GENERALES/LLAVES/LLAVE_AMARILLA.png").convert_alpha(), self.size)
        self.rect = self.image.get_rect()
        self.coordenate = coordenate
        self.rect.center = coordenate
        self.rotacion = 0
        self.personaje = personaje

    def detectar_colision(self):
        if self.rect.colliderect(self.personaje.rect):
            return True
        else:
            return False

    def movimiento_normal(self, frame50):
        self.rotacion += 2  # Aumenta el valor de rotación en cada frame
        self.image = pygame.transform.rotate(self.image_original, self.rotacion)  
        self.rect = self.image.get_rect()
        self.rect.center = self.coordenate
        return self.detectar_colision()