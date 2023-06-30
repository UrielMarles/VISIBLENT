import pygame
import json
import re
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255) 
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
LIME = (0, 255, 0)
TEAL = (0, 128, 128)
BROWN = (165, 42, 42)

def crear_lista_imagenes(ruta,cantidad,size):
    lista = []
    for numero in range(0,cantidad):
        numero_con_ceros = str(numero).zfill(4)
        imagen = pygame.image.load(ruta+numero_con_ceros+".png").convert_alpha()
        imagen = pygame.transform.scale(imagen,size)
        lista.append(imagen)
    return lista

def voltear_lista_imagenes_verticalmente(lista):
    listaNueva = []
    for imagen in lista:
        volteada = pygame.transform.flip(imagen, True, False)
        listaNueva.append(volteada)
    return listaNueva

def aumentar_numero_en_rango(numero,max):
    if numero < max:
        numero +=1
    else:
        numero = 0
    return numero

def abrirNiveldeJson(ruta,nivel):
    with open(ruta, 'r') as archivo:
        datos = json.load(archivo)
        nivel = datos[nivel] 
    return convertir_bool(nivel)
    
def convertir_csv_a_lista_dict(ruta:str)-> list[dict]:
    with open(ruta,"r",encoding='utf-8') as archivo:
        contenido = archivo.read()
    lineas = contenido.split('\n')
    lista = []
    primera = True
    for linea in lineas:
        listaValores = linea.split(',')
        if primera:
            llaves = listaValores
            cantidadLlaves = len(llaves)
            primera = False
        else:
            diccionario = {}
            for i in range(0,cantidadLlaves):
                diccionario[llaves[i]] = listaValores[i]
            lista.append(diccionario)
    return lista

def guardar_lista_dict_como_csv(listaDict:list[dict],ruta:str) -> None:
    encabezado = ""
    for llave in listaDict[0]:
        encabezado = encabezado + str(llave) + ","
    encabezado = encabezado[:-1] # saca la coma
    ultima = len(listaDict)
    with open(ruta,"w",encoding='utf-8') as archivo:
        archivo.write(encabezado + '\n')
        iteracion = 0
        for dict in listaDict:
            iteracion += 1
            linea = ""
            for llave in dict:
                linea = linea + str(dict[llave]) + ","
            linea = linea[:-1]
            if iteracion != ultima:
                archivo.write(linea + '\n')
            else:
                archivo.write(linea)


#devuelve una lista de diccionarios que tienen el valor indicado en la llave indicada
def obtener_lista_diccionarios_con_valor_especifico_en_llave(lista_diccionarios:list[dict],categoria:str,valor:str) -> list[dict]:
    lista_diccionarios = list((filter(lambda diccionario: diccionario[categoria] == valor,lista_diccionarios)))
    return lista_diccionarios

def copia_profunda(lista:list[dict]) -> list[dict]:
    nuevaLista = []
    for iterable in lista:
        nuevoIterable = iterable.copy()
        nuevaLista.append(nuevoIterable)
    return nuevaLista

## Recibe una expresion Regular y una string y se fija si la string cumple la regex
def matchear_con_regex(condicion:str,string:str) -> bool:
    valido = False
    if re.match(condicion,string):
        valido = True
    return valido

# Devuelve True si recibe un string que contiene un entero mayor a cero
def validar_entero_mayor_a_cero(string:str)-> bool:
    condicion = r'^[1-9]\d*$'
    return matchear_con_regex(condicion,string)

## devuelve True si la string que recibe tiene unicamente letras o espacios
def validar_string_alfanumerica(string:str)-> bool:
    condicion = r'^[A-Za-z\s]+$'
    return matchear_con_regex(condicion,string)
    
## devuelve true si el string que recibe tiene unicamente numeros del 0 al 9 y un posible signo de menos
def validar_string_int(string:str) -> bool:
    condicion = r'^-?\d+$'
    return matchear_con_regex(condicion,string)

## devuelve true si el string que recibe tiene unicamente numeros, una coma, y un posible menos
def validar_string_float(string:str) -> bool:
    condicion = r'^-?\d*\.\d+$'
    return matchear_con_regex(condicion,string)

## devuelve true si el string que recibe tiene unicamente numeros, maximo una coma y maximo un menos
def validar_string_numerica(string:str) -> bool:
    condicion = r'^-?\d+(\.\d+)?$'
    return matchear_con_regex(condicion,string)

##Identifica si una string contiene un Int o un Float y en caso de ser asi devuelve la string convertida
def normalizar_numeros_en_strings(string:str)-> str|int|float:
    devuelve = string
    if validar_string_int(string):
        devuelve = int(string)
    if validar_string_float(string):
        devuelve = float(string)
    return devuelve

def convertir_bool(datos):
    if isinstance(datos, dict):
        for clave, valor in datos.items():
            if isinstance(valor, str) and valor.lower() == 'true':
                datos[clave] = True
            elif isinstance(valor, str) and valor.lower() == 'false':
                datos[clave] = False
            elif isinstance(valor, (dict, list)):
                datos[clave] = convertir_bool(valor)
    elif isinstance(datos, list):
        for i, valor in enumerate(datos):
            if isinstance(valor, str) and valor.lower() == 'true':
                datos[i] = True
            elif isinstance(valor, str) and valor.lower() == 'false':
                datos[i] = False
            elif isinstance(valor, (dict, list)):
                datos[i] = convertir_bool(valor)
    return datos