import pygame
class Cronometro():
    def __init__(self) -> None:
        self.image = pygame.Surface((150, 50), pygame.SRCALPHA)
        self.font = pygame.font.Font("fuentes/HARLOWSI.TTF", 48)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (1000,75)
        self.segundos_totales = 0
        self.escribir_segundos()
        
    def escribir_segundos(self):
        self.image = pygame.Surface((150, 50), pygame.SRCALPHA)
        self.minutos = str(self.segundos_totales // 60).zfill(2)
        self.segundos_sobrantes = str(self.segundos_totales % 60).zfill(2)
        self.string_tiempo = self.minutos + ":" + self.segundos_sobrantes
        self.tiempo_renderizado = self.font.render(self.string_tiempo, True, (0, 0, 0))
        self.tiempo_renderizado_rect = self.tiempo_renderizado.get_rect()
        self.tiempo_renderizado_rect.center = (75,25)
        self.image.blit(self.tiempo_renderizado,self.tiempo_renderizado_rect)

