"""
La idea es armar un diccionario con el nombre como key y los puntos como values
"""
import random

def IngresarNuevoJugador(ListaDeJugadores): #Funcion "Ingreso" retorna nombre del jugador
    Nombre = str(input("Ingrese nombre Jugador{}: ".format(len(ListaDeJugadores)+1)))
    while Nombre in ListaDeJugadores:
        Nombre = str(input("Error: Jugador ya ingresado\nIngrese nombre Jugador{}: ".format(len(ListaDeJugadores))))
    return Nombre #Si ingresa "enter" dara como resultado ""



def DefinirJugadores(): #Funcion que retorna una lista de jugadores #Si inicalmente no ingreso nada retorna lista vacia
    MAX_JUGADORES = 5
    ListaDeJugadores = []
    NuevoJugador = None #Variable sin nada (!= "")
    while NuevoJugador != "" and len(ListaDeJugadores) < MAX_JUGADORES: #Si la lista tiene longitud 5 termina el bucle
        NuevoJugador = IngresarNuevoJugador(ListaDeJugadores)
        if NuevoJugador != "": ListaDeJugadores.append(NuevoJugador) #Si ingresa "enter" no lo agrega
    return ListaDeJugadores

def SeleccionarTurnos(ListaDeJugadores,PrimerTurno): #Esta funcion retorna una lista ordenada segun los turnos
    if PrimerTurno: #Si el primer turno esta definido (por ejemplo: porque gano 'Jugador1')

        ListaDeJugadores.remove(PrimerTurno) #Remuevo de la lista el nombre del jugador
        random.shuffle(ListaDeJugadores) #Mezclo la lista de los jugadores
        TurnosDefinidos = [PrimerTurno] + ListaDeJugadores #Agrego primero al jugador y luego uno la lista mezclada
    
    else: #Si no hay un primer turno definido:
        
        random.shuffle(ListaDeJugadores) #Mezclo la lista de jugadores
        TurnosDefinidos = ListaDeJugadores
    
    return TurnosDefinidos


def DefinirDiccionarioDeTurnos(ListaDeJugadores, PrimerTurno = None): #Crea un diccionario con claves de la lista (ordenada por turnos) de jugadore #Parametro opcional: PrimerTurno(nombre del jugador que va primero)
    TurnosDefinidos = SeleccionarTurnos(ListaDeJugadores, PrimerTurno) #Ordeno a los jugadores (ingresados de antemano como lista)
    DiccionarioDeTurnos = {}
    for Jugador in TurnosDefinidos: 
        DiccionarioDeTurnos[Jugador] = ["","",0,0,"","",0] #Lista predeterminada VACIA de cada jugador
    
    return DiccionarioDeTurnos





#MAIN: Para definir turnos iniciales usamos:

def DefinirTurnosIniciales():
    ListaDeJugadores = DefinirJugadores() #retorna una lista de jugadores
    Turnos = DefinirDiccionarioDeTurnos(ListaDeJugadores) #Crea un diccionario con claves de la lista (ordenada por turnos)
    return Turnos #Retorno el diccionario

#MAIN: Para redefinirTurnos usamos:

def ReDefinirTurnos(ListaDeJugadores, Ganador = None): #Como ya tenemos la lista de jugadores y a un posible ganador(El que acerto primero)
    Turnos = DefinirDiccionarioDeTurnos(ListaDeJugadores, Ganador) #Solo definimos un diccionario con el ganador (si lo hay)
    return Turnos


#Ambas retornan un diccionario con Claves "NombreJugador" y una lisa como valor
#La lista contiene [PalabraParaAdivinar,Caracter,Acierto,Desacierto,CaracteresErrados,CadenaOculta, PUNTOS]




print(DefinirTurnosIniciales())

"""
#Nota: ListaDeJugadores = [x for x in ListaDeClaves] Donde ListDeClaves son las claves del diccionario de jugadores
#Ej: (suponiendo que ListaDeJugadores ya la definimos)
ListaDeJugadores= ["Laura","Paola","Fede","Alicia","Juan"]
print(ReDefinirTurnos(ListaDeJugadores, "Alicia"))
"""







