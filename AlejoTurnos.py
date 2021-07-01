import random

"""
'Al inicio se deberá solicitar el nombre de los jugadores, controlando que no se
ingresen más de 5, y que los nombre no se repitan. Podrá considerar que el ingreso
de nombres finaliza, cuando se da enter y no se ingresa nada.
Ingresados los nombres de los participantes, se deberán ordenar al azar para
asignarle el turno de juego a cada uno de ellos; y se les debe informar antes del
comienzo de la partida.

A partir de la segunda partida, el orden de los jugadores, deberá generarse
nuevamente, pero el ganador de la última partida, siempre tendrá el primer turno de
la siguiente; el resto de los turnos debe otorgarse de forma aleatoria'

()DEFINICION DE TURNOS ALEJO
"""

def nombres():
    """
Crea un diccionario con los nombres de los jugadores y luego lo
retorna ordenado al azar. el valor de cada nombre sera 6 espacios
para los aciertos, desaciertos, etc.

firma: Alejo
"""
    numero = 1
    max_nombres = 5
    nombres = []
    DiccionarioJugadores = {}
    nombre = "Aqui iran los nombres"
    while nombre != (None or "") and len(nombres) < max_nombres:
        nombre = input("Ingrese el nombre del jugador {}: ".format(numero))
        if nombre == "" and len(DiccionarioJugadores) == 0:
            while len(nombres) == 0:
                nombre = input("Por favor, ingrese al menos un nombre: ")
        elif nombre in nombres:
            print("Ingrese otro nombre por favor")
        elif nombre == "":
            pass
        else:
            nombres.append(nombre)
            numero += 1
    random.shuffle(nombres)
    for Jugador in nombres:
        DiccionarioJugadores[Jugador] = ["","","","","",""]
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
            turnos_nuevos[Jugador] = ["","","","","",""]
    else:
        Jugadores.remove(Ganador)
        random.shuffle(Jugadores)
        turnos_nuevos[Ganador] = ["","","","","",""]
        for Jugador in Jugadores:
            turnos_nuevos[Jugador] = ["","","","","",""]
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
            Puntos[Jugador] = int(DiccionarioJugadores[Jugador][1])
    else:
        for Jugador in nombres:
            Puntos[Jugador] += DiccionarioJugadores[Jugador][1]
    return Puntos

print(nueva_organizacion({"Benedicto":"","Pepe":"","Juan":""}))
    