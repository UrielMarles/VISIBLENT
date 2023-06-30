import pygame
from generales import *
class Puntuacion():
    def __init__(self,coordenate,numero,nombre,tiempo):
        self.image = pygame.surface.Surface((340,50))
        self.numero = str(numero)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = coordenate
        self.image.fill(YELLOW)
        font = pygame.font.Font("fuentes/HARLOWSI.TTF", 35)
        numero_renderizado = font.render(self.numero, True, (0, 0, 0))
        nombre_renderizado = font.render(nombre, True, (0, 0, 0))
        tiempo_renderizado = font.render(tiempo, True, (0, 0, 0))
        numero_rect = numero_renderizado.get_rect()
        nombre_rect = nombre_renderizado.get_rect()
        tiempo_rect = tiempo_renderizado.get_rect()
        numero_rect.center = (25,25)
        nombre_rect.center = (150,25)
        tiempo_rect.center = (300,25)
        self.image.blit(numero_renderizado,numero_rect)
        self.image.blit(tiempo_renderizado,tiempo_rect)
        self.image.blit(nombre_renderizado,nombre_rect)