from Etapa1 import CorrerJuego, OcultarCadena
from Etapa2y8 import GenerarDiccionario
from Etapa3 import elegir_palabra_aleatoria, pedir_longitud
from Etapa5 import SeguirJuego
from Puntaje import tabla, datos
from AlejoTurnos import nombres, nueva_organizacion

# Desde Etapa1 se puede desactivar/Activar la Interfaz grafica que produce la funcion "Grafico"

# Si desea ACTIVAR la tabla de puntajes borre las # del main() 

def main():
    """
    Firma: FedeBacelar, Alejo, Rocio, Abigail, Axel
    """

    DiccionarioPalabras = GenerarDiccionario()
    Turnos = nombres()
    #Nombre = datos()
    seguir = True
    while seguir:
    
        LongitudPalabra = pedir_longitud() #Pedimos longitud
        for Jugador in Turnos:
            Turnos[Jugador][0] = elegir_palabra_aleatoria(DiccionarioPalabras, LongitudPalabra) #Otorgamos palabra a los jugadores
            Turnos[Jugador][5] = OcultarCadena(Turnos[Jugador][0]) #Ocultamos su palabra
        
        DicResultadosJugadores, Ganador = CorrerJuego(Turnos) #Borrar ganador etapa1
        Turnos = nueva_organizacion(Turnos, Ganador)
        seguir = SeguirJuego()


    #print(tabla(Nombre, Puntos))

main()

