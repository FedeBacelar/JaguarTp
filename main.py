from texto import obtener_texto
from Etapa1 import CorrerJuego
from Etapa2 import GenerarDiccionario
from Etapa3 import elegir_palabra_aleatoria, pedir_longitud
from Etapa5 import SeguirJuego
from Puntaje import tabla, datos

# Desde Etapa1 se puede desactivar/Activar la Interfaz grafica que produce la funcion "Grafico"

# Si desea ACTIVAR la tabla de puntajes borre las # del main() 


def main():
    """
    Firma: FedeBacelar, Alejo, Rocio, Abigail, Axel
    """
    Puntos= 0
    Diccionario = GenerarDiccionario()
    Nombre = datos()
    seguir = True
    while seguir:
        PalabraParaAdivinar = elegir_palabra_aleatoria(Diccionario, pedir_longitud())
        Puntos = CorrerJuego(PalabraParaAdivinar, Puntos)
        seguir = SeguirJuego()
    print(tabla(Nombre, Puntos))

main()

