import random

def pedir_longitud():
    """
    Define si el parametro Longitud tendrá un valor o no, bajo condiciones definidas.
    Pregunta al usuario si quiere una longitud específica para la palabra candidata.
    En caso afirmativo, se la pide y devuelve esa longitud.
    Firma: Axel
    """
    Condicion = input("Presione la tecla S si desea establecer una longitud determinada para la palabra: ")
    if Condicion.lower() == "s":
        Condicion = input("Ingrese la longitud que desea (mínimo 5 y máximo 15, o será al azar): ")
        while Condicion.isalpha() or Condicion == "":
            Condicion = input("Por favor, ingrese un numero: ")
        Condicion = int(Condicion)
    else:
        Condicion = None
    return Condicion

def palabras_candidatas(Diccionario, Longitud = None):
    """
    Tiene como parámetros a Diccionario y Longitud, la cual no tiene valor a menos que lo 
    defina la función pedir_longitud, por lo que lo vuelve un parámetro que puede ser ignorado.
    Retorna una lista con palabras candidatas (si la longitud no se encuentra dentro del rango, será aleatoria).
    Firma: Axel
    """ 
    Lista = list(Diccionario)
    ListaLongitud = []
    LONGITUD_MAXIMA = 15
    LONGITUD_MINIMA = 5
    if Longitud:
        if Longitud < LONGITUD_MINIMA or Longitud > LONGITUD_MAXIMA:
            Longitud = random.choice(range(LONGITUD_MINIMA, LONGITUD_MAXIMA+1))
        for Palabra in Lista:
            if Longitud == len(Palabra):
                ListaLongitud += [Palabra]
        Lista = ListaLongitud
    return Lista


def elegir_palabra_aleatoria(Diccionario, longitud):
    """
    Recibe un Diccionario y una longitud, devuelve una clave aleatoria de la misma longitud.
    Firma: Abigail y Axel
    """
    palabra = random.choice(palabras_candidatas(Diccionario,longitud))
    return palabra

def palabra_a_adivinar(DiccionarioJugadores,DiccionarioPalabras):
    longitud= pedir_longitud()
    jugadores= list(DiccionarioJugadores.keys())
    lista_usadas=[]
    for jugador in jugadores:
        palabra = elegir_palabra_aleatoria(DiccionarioPalabras, longitud)
        while palabra in lista_usadas:
            palabra = elegir_palabra_aleatoria(DiccionarioPalabras, longitud)
        DiccionarioJugadores[jugador][0] = palabra
        lista_usadas+=[palabra]
    return DiccionarioJugadores  
