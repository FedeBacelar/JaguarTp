from Etapa1 import CorrerJuego, OcultarCadena
from Etapa2y8 import GenerarDiccionario
from Etapa3 import elegir_palabra_aleatoria, pedir_longitud, palabra_a_adivinar
from Etapa5 import SeguirJuego
from EtapaTurnos import pedir_nombres, nueva_organizacion, dict_nombres
from Etapa7 import ImprimirResultadoParcial, ImprimirResultadosGenerales,ResultadosGenerales
from config import config, limpieza, cambio_valores
from VariablesVarias import parametros

# Desde Etapa1 se puede desactivar/Activar la Interfaz grafica que produce la funcion "Grafico"



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
    DiccionarioPuntos={}
    while seguir:
    
        LongitudPalabra = pedir_longitud()

        for Jugador in Turnos:
            Turnos[Jugador][0] = palabra_a_adivinar(Turnos, DiccionarioPalabras, LongitudPalabra )
            Turnos[Jugador][5] = OcultarCadena(Turnos[Jugador][0]) 
            
        DicResultadosJugadores, Ganador = CorrerJuego(Turnos)
        ImprimirResultadoParcial(DicResultadosJugadores,Ganador)
        
        if CantidadDePartidas == 0:
            DiccionarioPuntos= ResultadosGenerales(DicResultadosJugadores,Ganador,DiccionarioPuntos)
        else:
            print("")
            DiccionarioPuntos= ResultadosGenerales(DicResultadosJugadores,Ganador,DiccionarioPuntos)
            ImprimirResultadosGenerales(DiccionarioPuntos, CantidadDePartidas)
        CantidadDePartidas += 1
        
        Turnos = nueva_organizacion(Turnos, Ganador)
        seguir = SeguirJuego()

main()