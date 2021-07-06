from Etapa1 import CorrerJuego, OcultarCadena
from Etapa2y8 import GenerarDiccionario
from Etapa3 import elegir_palabra_aleatoria, pedir_longitud, palabra_a_adivinar
from Etapa5 import SeguirJuego
from EtapaTurnos import pedir_nombres, nueva_organizacion, dict_nombres
from Etapa7 import ImprimirResultadoParcial, ImprimirResultadosGenerales,ResultadosGenerales
from config import config, limpieza, cambio_valores
from VariablesVarias import parametros

# Desde Etapa1 se puede desactivar/Activar la Interfaz grafica que produce la funcion "Grafico"

# Si desea ACTIVAR la tabla de puntajes borre las # del main() 


def main():
    """
    Firma: FedeBacelar, Alejo, Rocio, Abigail, Axel
    """
    max_jugadores= parametros["MAX_USUARIOS"]
    DiccionarioPalabras = GenerarDiccionario()
    Lista_nombres= pedir_nombres(max_jugadores)
    Turnos = dict_nombres(Lista_nombres, Ganador = None)
    seguir = True
    CantidadDePartidas = 0
    while seguir:
    
        LongitudPalabra = pedir_longitud()

        for Jugador in Turnos:
            Turnos[Jugador][0] = palabra_a_adivinar(Turnos, DiccionarioPalabras, LongitudPalabra )
            Turnos[Jugador][5] = OcultarCadena(Turnos[Jugador][0]) 
            
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