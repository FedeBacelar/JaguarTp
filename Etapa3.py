import random
from config import parametros

def pedir_longitud():
    """
    Define si el parametro Longitud tendrá un valor o no, bajo condiciones definidas.
    Pregunta al usuario si quiere una longitud específica para la palabra candidata.
    En caso afirmativo, se la pide y devuelve esa longitud.
    Firma: Axel
    """
    LONGITUD_MAXIMA = 15
    LONGITUD_MINIMA = parametros["LONG_PALABRA_MIN"]

    Ingreso = input("Presione la tecla S si desea establecer una longitud determinada para la palabra: ")
    if Ingreso.lower() == "s":
        Longitud = input("Ingrese la longitud que desea (mínimo 5 y máximo 15, o será al azar): ")
        while Longitud.isalpha() or Longitud == "":
            Longitud = input("Por favor, ingrese un numero: ")
        Longitud = int(Longitud)
        if Longitud < LONGITUD_MINIMA or Longitud > LONGITUD_MAXIMA:
            Longitud = random.choice(range(LONGITUD_MINIMA, LONGITUD_MAXIMA+1))

    else:
        Longitud = random.choice(range(LONGITUD_MINIMA, LONGITUD_MAXIMA+1))
    return Longitud


def palabras_candidatas(Diccionario, Longitud):
    """
    Tiene como parámetros a Diccionario y Longitud, la cual no tiene valor a menos que lo 
    defina la función pedir_longitud, por lo que lo vuelve un parámetro que puede ser ignorado.
    Retorna una lista con palabras candidatas (si la longitud no se encuentra dentro del rango, será aleatoria).
    Firma: Axel
    """ 
    Lista = list(Diccionario)
    ListaLongitud = []

    for Palabra in Lista:
        if Longitud == len(Palabra):
            ListaLongitud += [Palabra]

    Lista = ListaLongitud

    return Lista

def elegir_palabra_aleatoria(Diccionario, longitud = None):
    """
    Recibe un Diccionario y una longitud, devuelve una clave aleatoria de la misma longitud.
    Firma: Abigail y Axel
    """
    palabra = random.choice(palabras_candidatas(Diccionario,longitud))
    return palabra

def palabra_a_adivinar(jugadores, DiccionarioPalabras, LongitudPalabra):
    """
    Toma como parámetros, los jugadores, las palabras a elegir y la longitud ingresada.
    Devuelve para cada jugador una palabra dentro de la longitud pedida asegurando que no
    se repitan las palabras entre ellos.
    Firma: Rocío y Axel
    """
    lista_usadas=[]
    for jugador in jugadores:
        palabra = elegir_palabra_aleatoria(DiccionarioPalabras, LongitudPalabra)
        while palabra in lista_usadas:
            palabra = elegir_palabra_aleatoria(DiccionarioPalabras, LongitudPalabra)
        lista_usadas+=[palabra]
    return palabra 