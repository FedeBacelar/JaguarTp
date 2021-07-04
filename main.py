from Etapa1 import CorrerJuego, OcultarCadena
from Etapa2y8 import GenerarDiccionario
from Etapa3 import elegir_palabra_aleatoria, pedir_longitud
from Etapa5 import SeguirJuego
from Puntaje import tabla, datos
from AlejoTurnos import nombres, nueva_organizacion
from Etapa7 import ImprimirResultadoParcial, ImprimirResultadosGenerales,ResultadosGenerales

# Desde Etapa1 se puede desactivar/Activar la Interfaz grafica que produce la funcion "Grafico"

# Si desea ACTIVAR la tabla de puntajes borre las # del main() 

def main():
    """
    Firma: FedeBacelar, Alejo, Rocio, Abigail, Axel
    """


    DiccionarioPalabras = GenerarDiccionario()
    Turnos = nombres()
    seguir = True
    CantidadDePartidas = 0
    while seguir:
    
        LongitudPalabra = pedir_longitud() #Pedimos longitud
        """Error de presionar enter y dar longitudes diferentes listo"""

        for Jugador in Turnos:
            Turnos[Jugador][0] = elegir_palabra_aleatoria(DiccionarioPalabras, LongitudPalabra) #Otorgamos palabra a los jugadores
            Turnos[Jugador][5] = OcultarCadena(Turnos[Jugador][0]) #Ocultamos su palabra
        
        DicResultadosJugadores, Ganador = CorrerJuego(Turnos)

        CantidadDePartidas += 1
        ImprimirResultadoParcial(DicResultadosJugadores,Ganador)
        if CantidadDePartidas > 1:
            print("")
            DiccionarioPuntos= ResultadosGenerales(DicResultadosJugadores,Ganador,Puntos = None)
            ImprimirResultadosGenerales(DiccionarioPuntos, CantidadDePartidas)

        Turnos = nueva_organizacion(Turnos, Ganador)
        seguir = SeguirJuego()


main()
