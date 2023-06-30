import pygame
from generales import *

class Mocos():
    def __init__(self,coordenate,max,min,direccion,velocidad,personaje):
        self.size = (100,100)
        self.lista_idle = crear_lista_imagenes("sprites\MOCO\CAMINANDO\MOCO_",7,self.size)
        self.image_muerto = pygame.transform.scale(pygame.image.load("sprites\MOCO\MURIENDO\EXPLOTANDO.png").convert_alpha(),self.size)
        self.image = pygame.transform.scale(pygame.image.load("sprites\MOCO\CAMINANDO\MOCO_0000.png").convert_alpha(),self.size)
        self.rect = self.image.get_rect()
        self.dire_inicial = coordenate
        self.rect.midbottom = coordenate
        self.frame_idle = 0
        self.frame_muerte = 0
        self.yendo_derecha = direccion
        self.velocidad = velocidad
        self.hitbox_width = self.size[0] * 0.75
        self.hitbox_height = self.size[1]
        self.max = max
        self.min = min
        self.personaje = personaje
        self.hitbox_offset_x = (self.rect.width - self.hitbox_width) // 2
        self.hitbox_offset_y = (self.rect.height - self.hitbox_height) // 2
        self.siendo_aplastado = False
        self.__actualizar_hitbox()

    def __morir(self,frame50):
        if frame50 and self.frame_muerte < 20:
            self.frame_muerte += 1
            self.size = (self.size[0]*0.99,self.size[1]*0.99)
            self.image = pygame.transform.rotate(self.image,45)
            self.image = pygame.transform.scale(self.image,self.size)
            self.rect = self.image.get_rect()
            self.rect.center = self.hitbox.center
            return False
        if self.frame_muerte == 20:
            return True

    def __actualizar_hitbox(self):
        self.hitbox = pygame.Rect(self.rect.left + self.hitbox_offset_x, self.rect.top + self.hitbox_offset_y,self.hitbox_width, self.hitbox_height)


    def __avanzar_frame(self,frame50):
        self.image = self.lista_idle[self.frame_idle]
        if frame50:
            self.frame_idle = aumentar_numero_en_rango(self.frame_idle,6)

    def __dar_paso(self):
        if self.yendo_derecha:
            self.rect.x += self.velocidad
        else:
            self.rect.x -= self.velocidad

    def __detectar_colisiones(self):
        # se fija si esta en el espacio vertical y horizontal del personaje
        en_area_vertical = self.hitbox.top < self.personaje.abajo_real and  self.hitbox.bottom > self.personaje.arriba_real
        en_area_horizontal = self.hitbox.left < self.personaje.derecha_real and self.hitbox.right > self.personaje.izquierda_real

        # Detecta si toca el borde del piso
        if self.rect.left < self.min or self.rect.right > self.max:
            self.__ruido_esquina()
            self.yendo_derecha = not(self.yendo_derecha) # si lo toca invierte la direccion de avanze
        
        #Detecta si esta siendo pisado
        
        if abs(self.hitbox.top - self.personaje.abajo_real) < 15 and en_area_horizontal and self.personaje.velocidad_caida >= 0:
            self.__ruido_explosion()
            self.siendo_aplastado = True
            self.image = self.image_muerto
            self.personaje.velocidad_caida = -10
            self.personaje.tiene_salto = True

        #Detecta si esta golpeando al personaje
        if abs(self.hitbox.bottom - self.personaje.arriba_real) < 15 and en_area_horizontal and self.personaje.velocidad_caida <= 0:
            self.personaje.muriendo = True
        elif (abs(self.hitbox.right - self.personaje.izquierda_real) < 10 or abs(self.hitbox.left - self.personaje.derecha_real) < 10) and en_area_vertical:
            self.personaje.muriendo = True


    def __ruido_esquina(self):
        if self.yendo_derecha:
            self.personaje.rugido_slime()
        else:
            self.personaje.rugido_grave_slime()
         
         
    def __ruido_explosion(self):
        self.personaje.explosion_slime()
    
    def movimiento_normal(self,frame50):
        if self.siendo_aplastado:
            return self.__morir(frame50)
        elif not(self.personaje.muriendo):
            self.__avanzar_frame(frame50)
            self.__detectar_colisiones()
            self.__dar_paso()
            self.__actualizar_hitbox()
        return False
        

