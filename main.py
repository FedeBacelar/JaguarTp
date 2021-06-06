from texto import obtener_texto
from Etapa1 import CorrerJuego
from Etapa2 import GenerarDiccionario
from Etapa3 import elegir_palabra_aleatoria, pedir_longitud
from Etapa5 import Puntaje, SeguirJuego

#Desde Etapa1 se puede desactivar/Activar la Interfaz grafica que produce la funcion "Grafico"

def main():
    """
    Firma: FedeBacelar, Alejo, Rocio, Abigail
    """
    Puntos= 0
    Diccionario = GenerarDiccionario()
    seguir = True
    while seguir:
        PalabraParaAdivinar = elegir_palabra_aleatoria(Diccionario,pedir_longitud())
        Puntuacion = CorrerJuego(PalabraParaAdivinar,Puntos)
        Puntos = Puntuacion[2]
        seguir = SeguirJuego()

main()

