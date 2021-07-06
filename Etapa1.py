from EtapaGrafica import Grafico
from Etapa5 import Puntaje
from config import parametros

"""-----------------------------------ETAPA_1-------------------------------------------------------------------------------"""
def Ingreso(cadenaOculta, caracteresErrados):
    """
    Evalua los ingresos: 
    Mientras el ingreso sea un caracter alfanumerico y no se repita esta funcion retornara una letra
    Caso contrario entrar en un bucle hasta que se cumpla lo anterior nombrado
    Retornara el caracter en minuscula

    Firma: FedeBacelar
    """
    caracter = str(input("Ingrese Letra_ ")) 
    
    while not (caracter.isalpha() and len(caracter) == 1) and not(salidaAnticipada(caracter)) or Repetido(caracter, cadenaOculta, caracteresErrados): #Se evalua si 1)"No es una letra" 2)"No hubo salida anticipada" 3)"No hay un caracter repetido"
        
        if not (caracter.isalpha() and len(caracter) == 1): 
            print("Ingreso invalido: Solo se permite ingresar una letra")
        
        elif Repetido(caracter,cadenaOculta, caracteresErrados):
            print("Letra repetida, por favor vuelva a ingresar nueva letra")
        
        caracter = str(input("Ingrese Letra_ "))
    
    return caracter.lower()

def Repetido(caracter,cadenaOculta, errados): 
    """
    Toma como parametros: caracter, cadenaOculta, errados
    Mientras el caracter este repetido retornara TRUE, caso contrario FALSE
    NOTA: Si está repetido significa que el caracter está en la lista de "errados" o que este en "cadenaOculta", o sea ya fue usado
    NOTA2: Las variables son str. 
       Firma: Rocio
    """
    return (caracter in cadenaOculta or caracter in errados)

def salidaAnticipada(caracter):
    """
    Toma como parametro un caracter.
    Retorna TRUE si el caracter es una cadena igual a: "Fin" o "0"
       Firma: FedeBacelar
    """
    return (caracter.upper() == 'FIN' or caracter == '0')

def CaracterEnPalabra(caracter, PalabraAdivinar):
    """
    Toma como parametros: caracter(str), PalabraAdivinar(str)
    Retorna TRUE en caso de que el caracter este en PalabraAdivinar
    Firma: FedeBacelar
    """
    return(PalabraAdivinar.find(caracter) != -1 and caracter != "")

def Mensaje(caracter, PalabraAdivinar):
    """
    Toma como parametros: caracter(str), PalabraAdivinar(str)
    Retornara un mensaje para el usuario
        Firma: FedeBacelar
    """
    if not caracter: #Si el caracter esta vacio
        Mensaje = "Palabra a adivinar: "
    elif CaracterEnPalabra(caracter, PalabraAdivinar):
        Mensaje = "Muy Bien!!! "
    else:
        Mensaje = "Lo siento!!! "
    return(Mensaje)

def Contador(aciertos,desaciertos,caracteresErrados):
    """
    Toma como parametros: aciertos(int), desaciertos(int) caracteresErrados(str)
    Retorna un contador con aciertos, desaciertos y caracteres errados
        Firma: FedeBacelar
    """
    Puntos = " Aciertos: " + str(aciertos) + " Desaciertos: " + str(desaciertos) + caracteresErrados
    return(Puntos)

def OcultarCadena(PalabraAdivinar):
    """
    Toma como parametro la palabra a adivinar
    Retorna la palabra oculta por "?"
    Firma: Alejo
    """
    return "?"*len(PalabraAdivinar)
    
def RevelarCadena(caracter, PalabraAdivinar, cadenaOculta):
	"""
    Toma como parametros: caracter(str), PalabraAdivinar(str), CadenaOculta(str)
	Revela la cadena oculta conforme se ingresen letras
    Retorna la cadena semi-revelada
    Firma: Alejo
	"""
	longitud = len(list(PalabraAdivinar))
	cadenaOculta = list(cadenaOculta) 
	if CaracterEnPalabra(caracter, PalabraAdivinar):
		for posicion in range(longitud):
			if PalabraAdivinar[posicion] == caracter:
				cadenaOculta[posicion] = caracter
	return	CadenaPalabra(cadenaOculta)

def contarAciertos(caracter, PalabraAdivinar):
    """
    Toma como parametros: caracter(str) y PalabraAdivinar(str)
    Retorna 1 si el caracter esta en la palabra, sino retorna 0
    Firma: Rocio
    """ 
    devolver = 1 if CaracterEnPalabra(caracter, PalabraAdivinar) else 0
    return devolver

def contarDesaciertos(desaciertos, caracter, PalabraAdivinar, caracteresErrados):
	"""
	Toma como parametros: desaciertos(int), caracter(str), PalabraAdivinar(str), caracteresErrados(str)
    Retorna los desaciertos junto a caracteres errados
    Firma: Alejo
	"""
	if not CaracterEnPalabra(caracter, PalabraAdivinar):
		desaciertos += 1
		caracteresErrados += "-" + caracter
	return [desaciertos, caracteresErrados]

def CadenaPalabra(Lista):
	"""
	Toma como parametros una lista
    Retorna la lista en forma de cadena
    Firma: Alejo
	"""
	return "".join(Lista)
"""----------------------------ACTUALIZACION:ETAPA-1-------------------------------------------------------------------------------"""
def SeguirJugando(DiccionarioJugadores):
    Seguir = False 
    CANTIDAD_MAX_VIDAS = 8
    for Jugador in DiccionarioJugadores:
        Gano = DiccionarioJugadores[Jugador][5].count("?") == 0
        Perdio = DiccionarioJugadores[Jugador][3] == CANTIDAD_MAX_VIDAS
        Seguir = not (Gano or Perdio)
    return Seguir

def CorrerJuego(DiccionarioJugadores):
    #{'Jugador1':[PalabraAdivinar,caracter,aciertos,desaciertos,caracteresErrados,cadenaOculta,PuntosEnPartida], 'Jugador2':etc}
    AbandonarJuego = False

    Ganador = False
    NombreGanador = None

    MAX_DESACIERTOS = parametros["MAX_DESACIERTOS"]
    PUNTOS_RESTA_GANA_PROGRAMA = parametros["PUNTOS_RESTA_GANA_PROGRAMA"]
    PUNTOS_ADIVINA_PALABRA = parametros["PUNTOS_ADIVINA_PALABRA"]

    while SeguirJugando(DiccionarioJugadores) and not AbandonarJuego and not Ganador:

        for Jugador in DiccionarioJugadores:

            PalabraAdivinar = DiccionarioJugadores[Jugador][0]
            caracter = DiccionarioJugadores[Jugador][1]
            aciertos = DiccionarioJugadores[Jugador][2]
            desaciertos = DiccionarioJugadores[Jugador][3]    
            caracteresErrados = DiccionarioJugadores[Jugador][4]
            Fallo = False
            PuntosEnPartida = DiccionarioJugadores[Jugador][6]
            cadenaOculta = DiccionarioJugadores[Jugador][5]
           
            while (desaciertos <= MAX_DESACIERTOS and not Fallo) and not AbandonarJuego and cadenaOculta.count("?") != 0 and not Ganador:
                   
                Grafico(desaciertos,Contador(aciertos, desaciertos, caracteresErrados),PuntosEnPartida,Mensaje(caracter, PalabraAdivinar), cadenaOculta, Jugador)
                #print(Jugador + " : " +Mensaje(caracter, PalabraAdivinar) + "--> "  + cadenaOculta + Contador(aciertos, desaciertos, caracteresErrados) + " Puntos:" + str(PuntosEnPartida))
                caracter = Ingreso(cadenaOculta, caracteresErrados)      
                cadenaOculta = RevelarCadena(caracter,PalabraAdivinar,cadenaOculta)

                aciertos += contarAciertos(caracter, PalabraAdivinar)   
                desaciertos = contarDesaciertos(desaciertos, caracter, PalabraAdivinar, caracteresErrados)[0] 
                caracteresErrados = contarDesaciertos(desaciertos, caracter, PalabraAdivinar, caracteresErrados)[1]

                Fallo = not CaracterEnPalabra(caracter, PalabraAdivinar)
                AbandonarJuego = salidaAnticipada(caracter)
                
                if cadenaOculta.count("?") == 0:
                    Ganador = True
                    NombreGanador = Jugador
                    print("Felicidaes {}, acertaste!! {}\n\n".format(Jugador, PalabraAdivinar)) 
                elif desaciertos == 8:
                    print("Lo siento {}, perdiste!!\n\n".format(Jugador, PalabraAdivinar))
        
                PuntosEnPartida = Puntaje(aciertos,desaciertos)


                DiccionarioJugadores[Jugador][1] = caracter 
                DiccionarioJugadores[Jugador][2] = aciertos
                DiccionarioJugadores[Jugador][3] = desaciertos    
                DiccionarioJugadores[Jugador][4] = caracteresErrados
                DiccionarioJugadores[Jugador][5] = cadenaOculta
                DiccionarioJugadores[Jugador][6] = PuntosEnPartida     
    
    if not Ganador:
        for Jugador in DiccionarioJugadores:
            DiccionarioJugadores[Jugador][6] -= PUNTOS_RESTA_GANA_PROGRAMA
    else:
        DiccionarioJugadores[NombreGanador][6] += PUNTOS_ADIVINA_PALABRA
    
    return DiccionarioJugadores, NombreGanador
