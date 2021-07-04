import random

def pedir_nombres(max_nombres):
    """
Pide nombres con una longitud maxima de los mismos y retorna una lista
con los nombres al azar
"""
    n_lista = []
    nombre = "Aqui iran los nombres"
    while len(n_lista) < max_nombres and nombre != "":
        nombre = input("Ingrese un nombre {}: ".format(len(n_lista) + 1))
        if nombre == "" and len(n_lista) == 0:
            while len(n_lista) == 0:
                nombre = input("Ingrese al menos un nombre: ")
                n_lista.append(nombre) if nombre != "" else None
        elif nombre in n_lista:
            print("Ingrese un nombre distinto")
            pass
        elif nombre != "":
            n_lista.append(nombre)
    random.shuffle(n_lista)
    return n_lista


def dict_nombres(Lista_nombres, Ganador = None):
    """
Con una lista de nombres predefinida, devuelve un diccionario con los jugadores
"""
    DiccionarioJugadores = {}
    if Ganador != None:
        Lista_nombres.remove(Ganador)
        DiccionarioJugadores[Ganador] = ["","",0,0,"","",0]
    for Jugador in Lista_nombres:
        DiccionarioJugadores[Jugador] = ["","",0,0,"","",0]
    return DiccionarioJugadores


def nueva_organizacion(DiccionarioJugadores, Ganador = None):
    """
    Crea una nueva organizacion de turnos en base al ganador y a los jugadores
    en cuestion. Atencion: Solo acepta un jugador
    """
    turnos_nuevos = {}
    Jugadores = list(DiccionarioJugadores.keys())
    random.shuffle(Jugadores)
    if Ganador == None:
        turnos_nuevos = dict_nombres(Jugadores)
    else:
        turnos_nuevos = dict_nombres(Jugadores, Ganador)
    return turnos_nuevos
    
    
def puntaje(DiccionarioJugadores, Puntos = {}):
    """
    De acuerdo al puntaje de los jugadores (hayan jugado o no) se adjunta los
    puntos de cada jugador en un diccionario donde las llaves sera cada jugador
    con su respectivo puntaje

    firma: Alejo
    """
    nombres = list(DiccionarioJugadores.keys())
    if len(Puntos) == 0: 
        for Jugador in nombres:
            Puntos[Jugador] = DiccionarioJugadores[Jugador][6]
    else:
        for Jugador in nombres:
            Puntos[Jugador] += DiccionarioJugadores[Jugador][6]
    return Puntos
