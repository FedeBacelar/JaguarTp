def ImprimirResultadoParcial(DiccionarioJugadores, NombreGanador):
    """Recibe un diccionario de jugadores y el nombre del ganador e imprime los resultados de la PARTIDA
    el dic es asi: {'Jugador':[PalabraAdivinar,caracter,aciertos,desaciertos,caracteresErrados,cadenaOculta,PuntosEnPartida]}
    Firma: Abigail  """
    
    for jugador in DiccionarioJugadores:
        
        PalabraAdivinar = DiccionarioJugadores[jugador][0]
        aciertos = DiccionarioJugadores[jugador][2]
        desaciertos = DiccionarioJugadores[jugador][3]
        PuntosEnPartida = DiccionarioJugadores[jugador][6]
        print("{} tu palabra era {}, tuviste {} aciertos y {} desaciertos. Sumaste {} puntos!".format(jugador,PalabraAdivinar,aciertos,desaciertos,PuntosEnPartida))
        
    print("\n El ganador en esta partida fue: ", NombreGanador)



def ResultadosGenerales(DiccionarioJugadores, NombreGanador, Puntos = None):
    """ De acuerdo al puntaje de los jugadores (hayan jugado o no) se adjunta los
    puntos de cada jugador en un diccionario donde las llaves sera cada jugador
    con su respectivo puntaje

    firma: Alejo
    """
    nombres = list(DiccionarioJugadores.keys())
    Puntos = {} if Puntos == None else Puntos
    if len(Puntos) == 0: 
        for Jugador in nombres:
            Puntos[Jugador] = [DiccionarioJugadores[Jugador][6],DiccionarioJugadores[Jugador][2],DiccionarioJugadores[Jugador][3]]
            if Jugador == NombreGanador:                      
                Puntos[Jugador]+=[1]
            else:
                Puntos[Jugador]+=[0]
    else:
        for Jugador in nombres:
            Puntos[Jugador][0] += DiccionarioJugadores[Jugador][6]         #Suma los PuntosGenerales
            Puntos[Jugador][1] += DiccionarioJugadores[Jugador][2]         #Suma los aciertos
            Puntos[Jugador][2] += DiccionarioJugadores[Jugador][3]         #Suma los desaciertos 
            if Jugador == NombreGanador:
                Puntos[Jugador][3]+=[1]                                    #Si el jugador ganó suma 1
    return Puntos                                                          #Devuelve un diccionario asi {'Jugador': [PuntosGenerales,aciertos,desaciertos,PartidasGanadas]}



def ImprimirResultadosGenerales(Puntos, CantidadPartidas):
    """Recibe el diccionario de puntos y la cantidad de partidas jugadas e imprime los resultados generales.
    Firma: Abigail """
    
    print("Partidas jugadas: ", CantidadPartidas)
    
    puntos= OrdenarPorPuntaje(Puntos)   #Devuelve una lista asi [[Jugador,PuntosGenerales,aciertos,desaciertos,PartidasGanadas]]
    for i in range(0,len(puntos)):
        jugador= puntos[i][0]
        PuntosGenerales = puntos[i][1]
        aciertos = puntos[i][2]
        desaciertos = puntos[i][3]
        PartidasGanadas = puntos[i][4]
        
        print("{} tu puntaje total es: {}, tuviste {} aciertos y {} desaciertos. Partidas ganadas: {}".format(jugador,PuntosGenerales,aciertos,desaciertos,PartidasGanadas))
        
    
def OrdenarPorPuntaje(dic):
    """Convirte un diccionario a una lista y la ordena segun el puntaje total
    Firma: Abigail"""
    lista=[]
    for clave in dic:
        lista.append([clave,dic[clave][0],dic[clave][1],dic[clave][2],dic[clave][3]])
    lista.sort(key= lambda x: x[1], reverse=True)
    return lista
