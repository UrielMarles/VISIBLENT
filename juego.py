import pygame
from generales import *
from objetos.imagen import Imagen
from niveles import *
from objetos.botones import Boton
from objetos.puntuacion import Puntuacion

class Juego():
    def __init__(self) -> None:
        self.__configurado_pygame()
        self.__inicializado_sonidos()
        self.__objetos_menu_inicio()
        self.__objetos_menu_pausa()
        self.__objetos_menu_niveles()
        self.__objetos_pantalla_nombre()

    def iniciar(self):
        self.__reestablecer_variables_iniciales()
        self.eligiendo_nombre = True
        self.inicio = False
        while self.running:
            self.__reestablecer_detecciones_eventos()
            if self.en_lvl:
                self.lvl.avanzarFrame()
            elif self.inicio:
                self.__menu_inicio()
            elif self.pausado:
                self.__menu_opciones()
            elif self.eligiendo_lvl:
                self.__menu_niveles()
            elif self.en_pantalla_victoria:
                self.__pantalla_victoria()
            elif self.eligiendo_nombre:
                self.__pantalla_nombre()
        pygame.quit()


    def __configurado_pygame(self):
        pygame.init()
        pygame.font.init()
        self.size = (1200, 900)
        self.milisegundos50 = pygame.USEREVENT+1
        self.milisegundos25 = pygame.USEREVENT+2
        self.milisegundos1000 = pygame.USEREVENT+3
        pygame.display.set_icon(pygame.image.load("sprites\MENUS\LOGO.png"))
        pygame.display.set_caption("VISIBLENT")
        pygame.time.set_timer(self.milisegundos50, 50)
        pygame.time.set_timer(self.milisegundos25, 25)
        pygame.time.set_timer(self.milisegundos1000, 1000)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        
    
    def __inicializado_sonidos(self):
        pygame.mixer.init()
        pygame.mixer.music.load("sonidos\musica_fondo.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        self.sonido_salto = pygame.mixer.Sound("sonidos\salto.mp3")
        self.rugido_slime = pygame.mixer.Sound(r"sonidos\rugido_slime.mp3")
        self.explosion_slime = pygame.mixer.Sound("sonidos\explosion_slime.mp3") 
        self.ruido_portal = pygame.mixer.Sound(r"sonidos\ruido_portal.mp3") 
        self.ruido_muerte = pygame.mixer.Sound(r"sonidos\ruido_muerte.mp3") 
        self.victoria_sonido = pygame.mixer.Sound(r"sonidos\victoria.mp3") 
        self.rugido_slime_grave = pygame.mixer.Sound(r"sonidos\rugido_slime_grave.mp3")
        self.__setear_volumen_general(0.5)
        
    def __setear_volumen_general(self,valor):
        pygame.mixer.music.set_volume(valor)
        self.sonido_salto.set_volume(valor*2)
        self.rugido_slime.set_volume(valor*0.5)
        self.explosion_slime.set_volume(valor*0.75)
        self.ruido_portal.set_volume(valor*1.5)
        self.ruido_muerte.set_volume(valor*1.5)
        self.victoria_sonido.set_volume(valor)
        self.rugido_slime_grave.set_volume(valor*0.5)

    def __objetos_menu_inicio(self):
        self.titulo = Imagen((125,400),(1000,400),"sprites\MENUS\TITULO.png",False)
        self.boton_jugar = Boton((450,450),(300,100),WHITE,72,"Jugar",True)
        self.boton_opciones = Boton((450,600),(300,100),WHITE,72,"Opciones",True)
        self.boton_salir = Boton((450,750),(300,100),WHITE,72,"Salir",True)
        self.total_blit_inicio = [self.titulo,self.boton_jugar,self.boton_opciones,self.boton_salir]
        self.frameFondoInicio = 0
        self.imagenesFondo = crear_lista_imagenes("sprites\MENUS\FONDO\FONDO_",4,self.size)
        self.rect_imagenes = self.imagenesFondo[0].get_rect()
        self.pantalla_carga = Imagen((0,900),(1200,900),"sprites\MENUS\CARGANDO.png")

    def __objetos_menu_pausa(self):
        self.pausa_fondo = Boton((350,800),(500,700),GRAY,10," ",True)
        self.titulo_pausa = Boton((360,225),(480,100),GRAY,85,"Pausado",False)
        self.boton_continuar = Boton((450,450),(300,80),WHITE,72,"Continuar",True)
        self.boton_volver_inicio = Boton((450,550),(300,80),WHITE,48,"Volver a inicio",True)
        self.boton_cerrar_juego = Boton((450,650),(300,80),WHITE,48,"Cerrar el juego",True)
        self.icono_sonido = Imagen((575,355),(80,80),"sprites\MENUS\SONIDO.png",False)
        self.barrita_sonido = Boton((450,325),(300,25),WHITE,10," ",True)
        # self.boton_silenciar = Boton((450,650),(300,80),WHITE,41,"Desactivar sonido",True)
        # self.boton_desilenciar = Boton((450,650),(300,80),WHITE,48,"Activar sonido",True)
        self.boton_cambiar_nombre = Boton((450,750),(300,80),WHITE,45,"Cambiar nombre",True)
        self.siguiendo_mouse = False
        self.total_blit_pausa = [self.pausa_fondo,self.barrita_sonido,self.titulo_pausa,self.boton_volver_inicio,self.boton_continuar,self.boton_cerrar_juego,self.boton_cambiar_nombre,self.icono_sonido]

    def __objetos_menu_niveles(self):
        self.titulo_menu = Boton((350,225),(500,200),WHITE,148,"Niveles",True)
        self.flecha_atras = Imagen((20,120),(100,100),"sprites\GENERALES\FLECHA_ATRAS.png")
        self.boton_lvl1 = Boton((120,400),(150,150),WHITE,72,"1",True)
        self.boton_lvl2 = Boton((390,400),(150,150),WHITE,72,"2",True)
        self.boton_lvl3 = Boton((660,400),(150,150),WHITE,72,"3",True)
        self.boton_lvl4 = Boton((930,400),(150,150),WHITE,72,"4",True)
        self.boton_lvl5 = Boton((120,600),(150,150),WHITE,72,"5",True)
        self.boton_lvl6 = Boton((390,600),(150,150),WHITE,72,"6",True)
        self.boton_lvl7 = Boton((660,600),(150,150),WHITE,72,"7",True)
        # self.boton_lvl8 = Boton((930,600),(150,150),WHITE,72,"8",True)
        # self.boton_lvl9 = Boton((120,800),(150,150),WHITE,72,"9",True)
        # self.boton_lvl10 = Boton((390,800),(150,150),WHITE,72,"10",True)
        # self.boton_lvl11 = Boton((660,800),(150,150),WHITE,72,"11",True)
        # self.boton_lvl12 = Boton((930,800),(150,150),WHITE,72,"12",True)
        self.total_blit_menu_niveles = [self.titulo_menu,self.boton_lvl1,self.boton_lvl2,self.boton_lvl3,self.boton_lvl4,self.flecha_atras,self.boton_lvl5,self.boton_lvl6,self.boton_lvl7]

    def __objetos_pantalla_nombre(self):
        self.nombre_fondo = Boton((200,675),(800,450),PURPLE,10," ",True)
        self.titulo_nombre = Boton((275,350),(650,75),WHITE,48,"Ingrese su nombre (max 14)",True)
        self.boton_aceptar_nombre = Imagen((375,660),(125,125),"sprites\MENUS\ACEPTAR.png")
        self.boton_borrar_nombre = Imagen((700,660),(125,125),"sprites\MENUS\CANCELAR.png")
        self.borrando = False
        self.nombre_string = ""
        self.total_blit_nombre = [self.nombre_fondo,self.titulo_nombre,self.boton_aceptar_nombre,self.boton_borrar_nombre]
    
    def __manejar_volumen(self):
        if self.icono_sonido.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.siguiendo_mouse = True
        if self.siguiendo_mouse:
            if self.mouse_x > 710:
                self.icono_sonido.rect.right = 755
            elif self.mouse_x < 490:
                self.icono_sonido.rect.left = 450
            else:
                self.icono_sonido.rect.left = self.mouse_x - 40
        if self.mouseSoltado:
            self.siguiendo_mouse = False
        self.fraccion_volumen =  (self.icono_sonido.rect.left -450) / 265
        self.__setear_volumen_general(self.fraccion_volumen)

    def __reestablecer_detecciones_eventos(self):
        self.clock.tick(60)
        self.frame50 = False
        self.frame25 = False
        self.frame1000 = False
        self.mouseApretado = False
        self.mouseSoltado = False
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.texto_escrito_en_frame = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == self.milisegundos50:
                self.frame50 = True
            elif event.type == self.milisegundos25:
                self.frame25 = True
            elif event.type == self.milisegundos1000:
                self.frame1000 = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouseApretado = True
                print(f"Coordenadas del clic: ({self.mouse_x}, {self.mouse_y})")
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.mouseSoltado = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__pausar_o_despausar()
                elif event.key == pygame.K_BACKSPACE:
                    self.borrando = True
                elif event.unicode.isalpha():
                    tecla = event.unicode.lower()
                    self.texto_escrito_en_frame += tecla
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    self.borrando = False

    def __reestablecer_variables_iniciales(self):
        self.running = True
        self.inicio = True
        self.pausado = False
        self.en_lvl = False
        self.eligiendo_lvl = False
        self.en_pantalla_victoria = False
        self.ultimo = "inicio"

    def __pausar_o_despausar(self):
        if self.en_lvl or self.eligiendo_lvl or self.inicio or self.pausado:
            if self.pausado:
                self.pausado = False
                match self.ultimo:
                    case "inicio":
                        self.inicio = True
                    case "lvl":
                        self.en_lvl = True
                    case "menu_lvl":
                        self.eligiendo_lvl = True
            else:
                self.pausado = True
                if self.inicio:
                    self.inicio = False
                    self.ultimo = "inicio"
                if self.eligiendo_lvl:
                    self.eligiendo_lvl = False
                    self.ultimo = "menu_lvl"
                elif self.en_lvl:
                    self.en_lvl = False
                    self.ultimo = "lvl"
    
    # para boton silenciar
    # def __silenciar_o_desilenciar(self):
    #     if self.silenciado:
    #         self.silenciado = False
    #         self.total_blit_pausa.remove(self.boton_desilenciar)
    #         self.total_blit_pausa.append(self.boton_silenciar)
    #         pygame.mixer.music.set_volume(0.5)
    #     else:
    #         self.silenciado = True
    #         self.total_blit_pausa.remove(self.boton_silenciar)
    #         self.total_blit_pausa.append(self.boton_desilenciar)
    #         pygame.mixer.music.set_volume(0.0)

    def __fondo_con_movimiento(self):
        if self.frame50 :
            self.frameFondoInicio = aumentar_numero_en_rango(self.frameFondoInicio,3)
        self.screen.blit(self.imagenesFondo[self.frameFondoInicio],self.rect_imagenes)

    def __blitear_lista_objetos(self,lista_objetos):
        for objeto in lista_objetos:
            self.screen.blit(objeto.image,objeto.rect)

    def __verificar_y_cargar_si_se_apreto(self,boton,indice):
        if boton.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.__cargar_nivel_segun_indice(indice)

    def __cargar_nivel_segun_indice(self,indice):
        if (indice < 7):
            self.screen.blit(self.pantalla_carga.image,self.pantalla_carga.rect)
            pygame.display.flip()
            self.en_lvl = True
            self.eligiendo_lvl = False
            self.en_pantalla_victoria = False
            self.ultimo = "lvl"
            infoLevel = abrirNiveldeJson("data\lista_niveles.json",indice)
            self.indice = indice
            self.numero_nivel = indice + 1
            self.lvl = Nivel(infoLevel,self.screen,self)
        else:
            self.eligiendo_lvl = True
            self.en_pantalla_victoria = False
            self.ultimo = "menu_lvl"

    def __actualizar_puntuaciones_nivel(self):
        numeroSegundos = self.lvl.cronometro.segundos_totales
        tiempoFormateado = self.lvl.cronometro.string_tiempo
        puntuacionesAnteriores = convertir_csv_a_lista_dict("data\puntuaciones.csv")
        numero_dict = -1
        reemplazandoPoisicion = 6
        seguir = True
        cantidadDicts = len(puntuacionesAnteriores) - 1
        while numero_dict < cantidadDicts and seguir:
            numero_dict +=1
            dict = puntuacionesAnteriores[numero_dict]

            if int(dict["numeroLvl"]) == self.numero_nivel and int(dict["numeroSegundos"]) > numeroSegundos:
                reemplazandoPoisicion = int(dict["posicion"])
                seguir = False
        dictQueReemplaza = {"numeroLvl":str(self.numero_nivel),"posicion":reemplazandoPoisicion,"numeroSegundos":numeroSegundos,"tiempoFormateado":tiempoFormateado,"nombre":self.nombre_string}
        while reemplazandoPoisicion <= 5:
            dictViejo = (puntuacionesAnteriores[numero_dict]).copy()
            puntuacionesAnteriores[numero_dict] = dictQueReemplaza
            dictQueReemplaza = dictViejo.copy()
            numero_dict +=1
            reemplazandoPoisicion +=1
            dictQueReemplaza["posicion"] = reemplazandoPoisicion
        self.lista_dict_puntuaciones_actualizadas = puntuacionesAnteriores
        guardar_lista_dict_como_csv(puntuacionesAnteriores,"data\puntuaciones.csv")
    
    def __actualizar_objetos_victoria(self):
        dicts_lvl = obtener_lista_diccionarios_con_valor_especifico_en_llave(self.lista_dict_puntuaciones_actualizadas,"numeroLvl",str(self.numero_nivel))
        self.victoria_fondo = Boton((150,850),(900,800),GRAY,10," ",True)
        self.titulo_victoria = Boton((350,200),(500,100),GRAY,90,"¡¡ Victoria !!",False)
        self.titulo_tiempos = Boton((650,300),(350,50),GREEN,50,"Top 5 tiempos",True)
        self.fondo_puntuaciones = Boton((650,700),(350,400),YELLOW,10," ",True)
        self.puntuacion1 = Puntuacion((654,375),1,dicts_lvl[0]["nombre"],dicts_lvl[0]["tiempoFormateado"])
        self.puntuacion2 = Puntuacion((654,450),2,dicts_lvl[1]["nombre"],dicts_lvl[1]["tiempoFormateado"])
        self.puntuacion3 = Puntuacion((654,525),3,dicts_lvl[2]["nombre"],dicts_lvl[2]["tiempoFormateado"])
        self.puntuacion4 = Puntuacion((654,600),4,dicts_lvl[3]["nombre"],dicts_lvl[3]["tiempoFormateado"])
        self.puntuacion5 = Puntuacion((654,675),5,dicts_lvl[4]["nombre"],dicts_lvl[4]["tiempoFormateado"])
        self.boton_siguiente_nivel = Boton((212,325),(350,75),WHITE,48,"Siguiente Nivel",True)
        self.boton_reintentar = Boton((212,450),(350,75),WHITE,56,"Reintentar",True)
        self.boton_menu_niveles = Boton((212,575),(350,75),WHITE,48,"Menu de niveles",True)
        self.boton_inicio_victoria = Boton((212,700),(350,75),WHITE,48,"Volver inicio",True)
        self.total_blit_victoria = [self.victoria_fondo,self.titulo_victoria,self.fondo_puntuaciones,self.boton_siguiente_nivel,self.boton_reintentar,self.boton_menu_niveles,self.boton_inicio_victoria,self.titulo_tiempos,self.puntuacion1,self.puntuacion2,self.puntuacion3,self.puntuacion4,self.puntuacion5]


    def ganar_nivel(self):
        self.__actualizar_puntuaciones_nivel()
        self.__actualizar_objetos_victoria()
        self.en_lvl = False
        self.pausado = False
        self.en_pantalla_victoria = True
        self.victoria_sonido.play()


    def __menu_niveles(self):
        ##pintado
        self.__fondo_con_movimiento()
        self.__blitear_lista_objetos(self.total_blit_menu_niveles)
        pygame.display.flip()
        ##logica
        if self.flecha_atras.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.__reestablecer_variables_iniciales()
        self.__verificar_y_cargar_si_se_apreto(self.boton_lvl1,0)
        self.__verificar_y_cargar_si_se_apreto(self.boton_lvl2,1)
        self.__verificar_y_cargar_si_se_apreto(self.boton_lvl3,2)
        self.__verificar_y_cargar_si_se_apreto(self.boton_lvl4,3)
        self.__verificar_y_cargar_si_se_apreto(self.boton_lvl5,4)
        self.__verificar_y_cargar_si_se_apreto(self.boton_lvl6,5)
        self.__verificar_y_cargar_si_se_apreto(self.boton_lvl7,6)
        # self.__verificar_y_cargar_si_se_apreto(self.boton_lvl8,7)
        # self.__verificar_y_cargar_si_se_apreto(self.boton_lvl9,8)
        # self.__verificar_y_cargar_si_se_apreto(self.boton_lvl10,9)
        # self.__verificar_y_cargar_si_se_apreto(self.boton_lvl11,10)
        # self.__verificar_y_cargar_si_se_apreto(self.boton_lvl12,11)

    def __menu_inicio(self):
        ## logica del menu
        if self.boton_salir.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.running = False
        elif self.boton_opciones.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.__pausar_o_despausar() 
        elif self.boton_jugar.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.eligiendo_lvl = True
            self.inicio = False
            self.ultimo = "menu_lvl"
        ##pintado del menu
        self.__fondo_con_movimiento()
        self.__blitear_lista_objetos(self.total_blit_inicio)
        pygame.display.flip() 

    def __menu_opciones(self):
        self.__manejar_volumen()
        if self.boton_continuar.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.__pausar_o_despausar()
        elif self.boton_volver_inicio.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.__reestablecer_variables_iniciales()
        elif self.boton_cerrar_juego.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.running = False
        # elif self.boton_silenciar.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
        #     self.__silenciar_o_desilenciar()
        elif self.boton_cambiar_nombre.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.pausado = False
            self.eligiendo_nombre = True
        ##pintado menu
        self.__blitear_lista_objetos(self.total_blit_pausa)
        pygame.display.flip()

    def __pantalla_victoria(self):
        if self.boton_siguiente_nivel.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.__cargar_nivel_segun_indice(self.numero_nivel)
        elif self.boton_reintentar.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.__cargar_nivel_segun_indice(self.indice)
        elif self.boton_menu_niveles.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.en_pantalla_victoria = False
            self.eligiendo_lvl = True
            self.ultimo = "menu_lvl"
        elif self.boton_inicio_victoria.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.__reestablecer_variables_iniciales()
        ## pintado menu
        self.__blitear_lista_objetos(self.total_blit_victoria)
        pygame.display.flip()

    def __pantalla_nombre(self):
        ##logica pantalla nombre
        for letra in self.texto_escrito_en_frame:
            if len(self.nombre_string) < 14:
                self.nombre_string += letra
        if self.borrando and self.frame50:
            self.nombre_string = self.nombre_string[:-1]
        self.cuadrado_ingresar_nombre = Boton((250,525),(700,150),BLACK,90,self.nombre_string,False,WHITE)
        if self.boton_borrar_nombre.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.nombre_string = ""
        if self.boton_aceptar_nombre.detectarPresionado(self.mouse_x,self.mouse_y,self.mouseApretado):
            self.eligiendo_nombre = False
            if self.pausado:
                self.pausado = False
            match self.ultimo:
                    case "inicio":
                        self.inicio = True
                    case "lvl":
                        self.en_lvl = True
                    case "menu_lvl":
                        self.eligiendo_lvl = True
        #pintado pantalla
        self.__fondo_con_movimiento()
        self.__blitear_lista_objetos(self.total_blit_nombre)
        self.screen.blit(self.cuadrado_ingresar_nombre.image,self.cuadrado_ingresar_nombre.rect)
        pygame.display.flip()


    