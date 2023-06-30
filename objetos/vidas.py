from generales import *

class Vidas():
    def __init__(self,coordenate,size,inicial):
        self.cantidad_vidas = inicial
        self.lista_vidas = crear_lista_imagenes("sprites\GENERALES\VIDAS\VIDAS_",6,size)
        self.image = self.lista_vidas[inicial]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = coordenate

    def actualizar_vidas(self,cantidad):
        self.cantidad_vidas = cantidad
        self.image = self.lista_vidas[cantidad]

    def aumentar_vidas(self):
        if self.cantidad_vidas < 5:
            self.cantidad_vidas += 1
            self.image = self.lista_vidas[self.cantidad_vidas]

    def reducir_vidas(self):
        if self.cantidad_vidas > 0:
            self.cantidad_vidas -= 1
            self.image = self.lista_vidas[self.cantidad_vidas]
        