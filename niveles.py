import pygame
from generales import *
from objetos.mocos import Mocos
from objetos.ladrillos import Ladrillos
from objetos.personaje import Personaje
from objetos.vidas import Vidas
from objetos.pinchos import Pinchos
from objetos.portal import Portal
from objetos.indicador import Indicador
from objetos.llaves import Llaves
from objetos.puertas import Puertas
from objetos.cronometro import Cronometro


class Nivel():
    def __init__(self,infoLevel,screen,juego):
        self.vidas = Vidas((100,100),(500,80),3)
        self.cronometro = Cronometro()
        self.screen = screen
        self.imagen_fondo = pygame.transform.scale(pygame.image.load("sprites\GENERALES\FONDO.jpg"),(1200,900))
        self.infoLevel = infoLevel
        self.invis = False
        self.juego = juego
        self.__reestablecerNivel()


    def __reestablecerNivel(self):
        self.personaje = Personaje(self.infoLevel["Personaje"],self)
        self.portal = Portal(self.infoLevel["Portal"],self.personaje)
        self.indicador_ciego = Indicador(True)
        self.indicador_vidente = Indicador(False)
        self.objetos_con_colision = []
        self.objetos_con_movimiento = []
        self.objetos_en_invisibilidad = [self.vidas,self.indicador_ciego]
        self.objetos_siempre_visibles = [self.portal, self.personaje,self.cronometro]
        for pincho in self.infoLevel["Pinchos"]:
            self.objetos_con_colision.append(Pinchos(*pincho))
        for ladrillo in self.infoLevel["Ladrillos"]:
            if len(ladrillo) == 8:
                if ladrillo[2]:
                    objeto = Ladrillos(ladrillo[0],ladrillo[1],ladrillo[2],ladrillo[3],ladrillo[4],ladrillo[5],ladrillo[6],ladrillo[7],self.personaje)
                    self.objetos_con_movimiento.append(objeto)
                else:
                    objeto = Ladrillos(*ladrillo)
            else:
                objeto = Ladrillos(*ladrillo)
            self.objetos_con_colision.append(objeto)
        for moco in self.infoLevel["Mocos"]:
            objeto = Mocos(moco[0],moco[1],moco[2],moco[3],moco[4],self.personaje)
            self.objetos_con_movimiento.append(objeto)
        self.puertas = []
        for puerta in self.infoLevel["Puertas"]:
            objeto = Puertas(*puerta)
            self.objetos_con_colision.append(objeto)
            self.puertas.append(objeto)
        self.objetos_invisibles =  self.objetos_con_movimiento + self.objetos_con_colision 
        self.objetos_invisibles.append(self.indicador_vidente)
        self.llave_esta = False
        if self.infoLevel["Llave"][0]:
            self.llave = Llaves(self.infoLevel["Llave"][1],self.personaje)
            self.objetos_invisibles.append(self.llave)
            self.llave_esta = True
    

    def __manejar_movimiento_objetos(self):
        for objeto in self.objetos_con_movimiento:
            if objeto.movimiento_normal(self.juego.frame50):
                self.objetos_con_movimiento.remove(objeto)
                self.objetos_invisibles.remove(objeto)
        if self.llave_esta:
            if self.llave.movimiento_normal(self.juego.frame50):
                self.objetos_invisibles.remove(self.llave)
                self.llave_esta = False
                for objeto in self.puertas:
                    self.objetos_con_colision.remove(objeto)
                    self.objetos_invisibles.remove(objeto)
        self.portal.movimiento_normal(self.juego.frame50)

    def __rellenado_pantalla(self):
        #aca comienza el pintado
        self.screen.blit(self.imagen_fondo,(0,0))

        ## esto se pinta si no es invis
        if not(self.invis):
            for objeto in self.objetos_invisibles:
                self.screen.blit(objeto.image,objeto.rect)
        else: #esto solo se pinta si es invis
            for objeto in self.objetos_en_invisibilidad:
                self.screen.blit(objeto.image,objeto.rect)

        ## esto se pinta siempre
        for objeto in self.objetos_siempre_visibles:
            self.screen.blit(objeto.image,objeto.rect)
        pygame.display.flip()   
    
    def __manejar_vidas_e_invisibilidad(self):
        if self.personaje.muerte:
            self.__reestablecerNivel()
            if self.invis:
                self.vidas.reducir_vidas()
                if self.vidas.cantidad_vidas == 0:
                    self.invis = False
                    self.vidas.actualizar_vidas(3)
        if self.personaje.victoria:
            if not(self.invis):
                self.invis = True
                self.__reestablecerNivel()
                self.vidas.actualizar_vidas(3)
            else:
                self.juego.ganar_nivel()

    def __avanzar_tiempo(self):
        if self.juego.frame1000:
            self.cronometro.segundos_totales += 1
            self.cronometro.escribir_segundos()

    def avanzarFrame(self):
        self.__avanzar_tiempo()
        teclas = pygame.key.get_pressed()
        self.__manejar_movimiento_objetos()
        self.personaje.moverPersonaje(self.objetos_con_colision,teclas,self.juego.frame50,self.juego.frame25)
        self.__manejar_vidas_e_invisibilidad()
        self.__rellenado_pantalla()

    def efectoSonido(self,tipo):
        match tipo:
            case "salto":
                self.juego.sonido_salto.play()
            case "rugido_slime":
                self.juego.rugido_slime.play()
            case "rugido_grave_slime":
                self.juego.rugido_slime_grave.play()
            case "explosion_slime":
                self.juego.explosion_slime.play()
            case "ruido_portal":
                self.juego.ruido_portal.play()
            case "ruido_muerte":
                self.juego.ruido_muerte.play()
