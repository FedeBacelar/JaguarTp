import random


def nombres():
    """
    Crea un diccionario con los nombres de los jugadores y luego lo
    retorna ordenado al azar. el valor de cada nombre sera 6 espacios
    para los aciertos, desaciertos, etc.

    firma: Alejo
    """
    max_nombres = 5
    Jugadores = []
    DiccionarioJugadores = {}
    nombre = "Aqui iran los nombres"
    while nombre != "" and len(Jugadores) < max_nombres:
        nombre = input("Ingrese el nombre del jugador {}: ".format(len(Jugadores) + 1))
        if nombre == "" and len(Jugadores) == 0:
            while len(Jugadores) == 0:
                nombre = input("Por favor, ingrese al menos un nombre: ")
                Jugadores.append(nombre) if nombre != "" else None
        elif nombre in Jugadores:
            print("Ingrese otro nombre por favor")
        elif nombre == "":
            pass
        else:
            Jugadores.append(nombre)
    random.shuffle(Jugadores)
    for Jugador in Jugadores:
        DiccionarioJugadores[Jugador] = ["","",0,0,"","",0]
    return DiccionarioJugadores

def nueva_organizacion(DiccionarioJugadores, Ganador = None):
    """
    Crea una nueva organizacion de turnos en base al ganador y a los jugadores
    en cuestion. Atencion: Solo acepta un jugador
    """
    turnos_nuevos = {}
    Jugadores = list(DiccionarioJugadores.keys())
    if Ganador == None:
        random.shuffle(Jugadores)
        for Jugador in Jugadores:
            turnos_nuevos[Jugador] = ["","",0,0,"","",0]
    else:
        Jugadores.remove(Ganador)
        random.shuffle(Jugadores)
        turnos_nuevos[Ganador] = ["","",0,0,"","",0]
        for Jugador in Jugadores:
            turnos_nuevos[Jugador] = ["","",0,0,"","",0]
    return turnos_nuevos
    

def puntaje(DiccionarioJugadores, Puntos = None):
    """
    De acuerdo al puntaje de los jugadores (hayan jugado o no) se adjunta los
    puntos de cada jugador en un diccionario donde las llaves sera cada jugador
    con su respectivo puntaje

    firma: Alejo
    """
    nombres = list(DiccionarioJugadores.keys())
    Puntos = {} if Puntos == None else Puntos
    if len(Puntos) == 0: 
        for Jugador in nombres:
            Puntos[Jugador] = DiccionarioJugadores[Jugador][6]
    else:
        for Jugador in nombres:
            Puntos[Jugador] += DiccionarioJugadores[Jugador][6]
    return Puntos

