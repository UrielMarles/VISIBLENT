import pygame
from generales import *

class Ladrillos():
    def __init__(self,coordenate,size,movimiento = False, horizontal=True,velocidad = 2,max = None,min = None,atravezable = False,personaje = None):
        self.image = pygame.surface.Surface(size)
        self.rect = self.image.get_rect()
        if atravezable:
            self.image.fill(RED)
        else:
            self.image.fill(GRAY)
        primer_cuadrado = (size[0]-10,size[1]-10)
        #dibuja el bode
        pygame.draw.rect(self.image, BLACK, (self.rect.x,self.rect.y,size[0],size[1]), 3)
        #dibua el cuadrado de adentro
        pygame.draw.rect(self.image, BLACK, (self.rect.x+5, self.rect.y+5,primer_cuadrado[0],primer_cuadrado[1]), 3)
        self.rect.bottomleft = coordenate
        self.se_atravieza = atravezable
        self.es_letal = False
        self.se_mueve = movimiento
        self.horizontal = horizontal
        self.velocidad = velocidad
        self.arriba_derecha = True
        self.max = max
        self.min = min
        self.personaje = personaje
        self.inicio = coordenate
        self.tocando_personaje = False

    def movimiento_normal(self,frame50):
        self.__detectar_colisiones()
        self.__avanzar()
    
    def __avanzar(self):
        if self.horizontal:
            self.rect.x += self.velocidad
            if self.rect.right > self.max or self.rect.left < self.min:
                self.velocidad = -self.velocidad
            if self.tocando_personaje and not(self.personaje.moviendose_horizontalmente):
                self.personaje.rect.x += self.velocidad
        else:
            self.rect.y += self.velocidad
            if self.rect.top < self.min or self.rect.bottom > self.max:
                self.velocidad = -self.velocidad
            if self.tocando_personaje and not(self.personaje.moviendose_horizontalmente):
                self.personaje.rect.y += self.velocidad
        return False
    
    def __detectar_colisiones(self):
        # se fija si el personaje lo esta pisando
        self.tocando_personaje = False
        en_area_horizontal = self.rect.left < self.personaje.derecha_real and self.rect.right > self.personaje.izquierda_real
        if abs(self.rect.top - self.personaje.abajo_real) < 10 and en_area_horizontal and self.personaje.velocidad_caida >= 0:
            self.tocando_personaje = True
