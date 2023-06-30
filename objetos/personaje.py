import pygame
from generales import *
class Personaje():

    def __init__(self,coordenate,nivel) -> None:
        self.size_inicial = (45,60)
        self.lista_moveR = crear_lista_imagenes("sprites\PERSONAJE\CAMINAR\caminarDos_",10,self.size_inicial)
        self.lista_moveL = voltear_lista_imagenes_verticalmente(self.lista_moveR)
        self.lista_idleR = crear_lista_imagenes("sprites\PERSONAJE\IDLER\idleR_",6,self.size_inicial)
        self.lista_idleL = voltear_lista_imagenes_verticalmente(self.lista_idleR)
        self.lista_IsaltoR = crear_lista_imagenes("sprites\PERSONAJE\SALTAR\INICIOSALTO\inicio_",13,self.size_inicial)
        self.lista_IsaltoL = voltear_lista_imagenes_verticalmente(self.lista_IsaltoR)
        self.lista_FsaltoR = crear_lista_imagenes(r"sprites\PERSONAJE\SALTAR\FINALSALTO\final_",5,self.size_inicial)
        self.lista_FsaltoL = voltear_lista_imagenes_verticalmente(self.lista_FsaltoR)
        self.lista_caidaR = crear_lista_imagenes("sprites\PERSONAJE\SALTAR\CAIDA\caida_",8,self.size_inicial)
        self.lista_caidaL = voltear_lista_imagenes_verticalmente(self.lista_caidaR)
        self.image_inicial = pygame.transform.scale(pygame.image.load("sprites\PERSONAJE\INICIAL.png").convert_alpha(),self.size_inicial)
        self.image = self.image_inicial
        self.rect = self.image.get_rect()
        self.coordenada_inicial = coordenate
        self.rect.bottomleft = self.coordenada_inicial
        self.rect_inicial = self.rect
        self.dist_pasos= 5
        self.achicadoHorizontal = 14
        self.achicadoVertical = 2
        self.nivel = nivel
        self.__reestablecer_variables()

    def __actualizarHitbox(self):
        self.abajo_real = self.rect.bottom - self.achicadoVertical
        self.derecha_real = self.rect.right - self.achicadoHorizontal
        self.izquierda_real = self.rect.left + self.achicadoHorizontal
        self.arriba_real = self.rect.top + self.achicadoVertical
        self.centro_real = self.rect.center

    def __reestablecer_variables(self):
        self.ultimo_lado = "right"
        self.velocidad_caida = 0
        self.frameMov = 0
        self.frameIdle = 0
        self.frameIsalto = 0
        self.frameDesaparicion = 0
        self.frameFsalto = 0
        self.frameCaida = 0
        self.size = self.size_inicial
        self.image = self.image_inicial
        self.rect = self.rect_inicial
        self.rect.bottomleft = self.coordenada_inicial
        self.tiene_salto = True
        self.saltando = False
        self.muriendo = False
        self.muerte = False
        self.ganando = False
        self.victoria = False
        self.__actualizarHitbox()

    def __aplicarGravedad(self,frame50):
        if not(self.tocandoPiso):
            self.rect.y += self.velocidad_caida
            if frame50 and self.velocidad_caida < 15:
                self.velocidad_caida +=1
            if self.ultimo_lado == "right":
                if self.velocidad_caida < 0:
                    self.image = self.lista_IsaltoR[self.frameIsalto]
                    self.frameIsalto = aumentar_numero_en_rango(self.frameIsalto,12)
                    self.frameFsalto = 0
                if self.velocidad_caida >=0 and self.velocidad_caida < 4:
                    self.image = self.lista_FsaltoR[self.frameFsalto]
                    if frame50:
                        self.frameFsalto = aumentar_numero_en_rango(self.frameFsalto,4)
                    self.frameCaida = 0
                if self.velocidad_caida > 3:
                    self.image = self.lista_caidaR[self.frameCaida]
                    self.frameCaida = aumentar_numero_en_rango(self.frameCaida,7)
            if self.ultimo_lado == "left":
                if self.velocidad_caida < 0:
                    self.image = self.lista_IsaltoL[self.frameIsalto]
                    self.frameIsalto = aumentar_numero_en_rango(self.frameIsalto,12)
                    self.frameFsalto = 0
                if self.velocidad_caida >=0 and self.velocidad_caida < 4:
                    self.image = self.lista_FsaltoL[self.frameFsalto]
                    if frame50:
                        self.frameFsalto = aumentar_numero_en_rango(self.frameFsalto,4)
                    self.frameCaida = 0
                if self.velocidad_caida > 3:
                    self.image = self.lista_caidaL[self.frameCaida]
                    self.frameCaida = aumentar_numero_en_rango(self.frameCaida,7)

    def __saltar(self,teclas):
        if teclas[pygame.K_SPACE] and (self.tocandoPiso or self.tiene_salto) and not(self.saltando):
            if not(self.tocandoPiso):
                self.tiene_salto = False
            self.nivel.efectoSonido("salto")
            self.saltando = True
            self.velocidad_caida = -10
            self.rect.y += self.velocidad_caida
        if not(teclas[pygame.K_SPACE]):
            if self.velocidad_caida < 0 and self.saltando:
                self.velocidad_caida = self.velocidad_caida/2
            self.saltando = False

    def __movimientoHorizontal(self,teclas,frame25):
        self.moviendose_horizontalmente = False
        if not(teclas[pygame.K_LEFT] and teclas[pygame.K_RIGHT]): #esto verifica que solo se mueva si no estan presionadas ambas teclas
            
            if teclas[pygame.K_LEFT]:
                self.__moveL(frame25)
            if teclas[pygame.K_RIGHT]:
                self.__moveR(frame25)

    def __moveL(self,frame25):
        self.moviendose_horizontalmente = True
        if self.tocandoPiso:
            self.image = self.lista_moveL[self.frameMov]
            if frame25:
                    self.frameMov = aumentar_numero_en_rango(self.frameMov,9)
        self.rect.x -= self.dist_pasos
        self.ultimo_lado = "left"
    
    def __moveR(self,frame25):
        self.moviendose_horizontalmente = True
        if self.tocandoPiso:
            self.image = self.lista_moveR[self.frameMov]
            if frame25:
                    self.frameMov = aumentar_numero_en_rango(self.frameMov,9)
        self.rect.x += self.dist_pasos
        self.ultimo_lado = "right"

    def __girar_reseteo(self,frame50,evento):
        if frame50:
            self.frameDesaparicion += 1
            if self.frameDesaparicion == 1:
                if evento == "victoria":
                    self.ruido_portal()
                else:
                    self.ruido_muerte()
            if self.frameDesaparicion > 10 or evento == "muerte":
                self.size = (self.size[0]*0.99,self.size[1]*0.99)
                self.image = pygame.transform.rotate(self.image,45)
                self.image = pygame.transform.scale(self.image,self.size)
            else:
                self.frameFsalto = aumentar_numero_en_rango(self.frameFsalto,4)
                self.image = self.lista_FsaltoR[self.frameFsalto]
            self.rect = self.image.get_rect()
            self.rect.center = self.centro_real
            if self.frameDesaparicion == 30:
                if evento == "muerte":
                    self.muerte = True
                else:
                    self.victoria = True

    def ruido_portal(self):
        self.nivel.efectoSonido("ruido_portal")
    def ruido_muerte(self):
        self.nivel.efectoSonido("ruido_muerte")
    def rugido_slime(self):
        self.nivel.efectoSonido("rugido_slime")
    def rugido_grave_slime(self):
        self.nivel.efectoSonido("rugido_grave_slime")
    def explosion_slime(self):
        self.nivel.efectoSonido("explosion_slime")
    
    def __idle(self,teclas,frame50): #esta idle cuando ambas teclas estan apretadas o ninguna en el piso
        if teclas[pygame.K_LEFT] == teclas[pygame.K_RIGHT] and self.tocandoPiso: 
            if frame50:
                self.frameIdle = aumentar_numero_en_rango(self.frameIdle,5)
            if self.ultimo_lado == "left":  
                self.image = self.lista_idleL[self.frameIdle]
            else:
                self.image = self.lista_idleR[self.frameIdle]
    
    def __detectarColisiones(self,lista_objetos):
        self.__actualizarHitbox()
        self.tocandoPiso = False
        for objeto in lista_objetos:
            colision = False
            en_area_horizontal = objeto.rect.left < self.derecha_real and objeto.rect.right > self.izquierda_real
            en_area_vertical = objeto.rect.top < self.abajo_real and  objeto.rect.bottom > self.arriba_real

            #se fija si toca el piso
            if abs(objeto.rect.top - self.abajo_real) < 10 and en_area_horizontal and self.velocidad_caida >= 0:
                self.tocandoPiso = True
                self.tiene_salto = True
                self.velocidad_caida = 0
                self.rect.bottom = objeto.rect.top + self.achicadoVertical
                colision = True

            #si no es atravezable verifica el resto de las colisiones
            if not(objeto.se_atravieza):
                if abs(objeto.rect.left - self.derecha_real) < 10 and en_area_vertical:
                    self.rect.right = objeto.rect.left + self.achicadoVertical
                    colision = True
                if abs(objeto.rect.right - self.izquierda_real) < 10 and en_area_vertical:
                    self.rect.left = objeto.rect.right - self.achicadoVertical
                    colision = True
                if abs(objeto.rect.bottom - self.arriba_real) < 11 and en_area_horizontal and self.velocidad_caida < 0:
                    self.velocidad_caida = 0
                    self.rect.top = objeto.rect.bottom - self.achicadoVertical
                    colision = True
            if colision and objeto.es_letal:
                self.muriendo = True
            

    def moverPersonaje(self,lista_objetos,teclas,frame50,frame25):
        if self.muriendo or self.ganando:
            if self.muriendo:
                self.__girar_reseteo(frame50,"muerte")
            else:
                self.__girar_reseteo(frame50,"victoria")
        else:
            self.__detectarColisiones(lista_objetos)
            self.__aplicarGravedad(frame50)
            self.__saltar(teclas)
            self.__idle(teclas,frame50)
            self.__movimientoHorizontal(teclas,frame25)
        
            