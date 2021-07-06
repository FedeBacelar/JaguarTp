from VariablesVarias import parametros

def Puntaje(Aciertos,Desaciertos,Puntos=0):
    """
    Toma como parametros: Aciertos(int), Desaciertos(int)
    Retorna los puntos del usuario
    Firma: FedeBacelar
    """
    PUNTOS_ACIERTOS = parametros["PUNTOS_ACIERTOS"]
    PUNTOS_DESACIERTOS = parametros["PUNTOS_DESACIERTOS"]
    Puntos += (Aciertos*PUNTOS_ACIERTOS - Desaciertos*PUNTOS_DESACIERTOS)
    return Puntos

def SeguirJuego():
    """
    Retorna la solicitud de "seguir jugando" del usuario en forma de: True o False
    FedeBacelar: FedeBacelar
    """
    seguir = str(input("Desea seguir jugando? (s/n)"))
    return seguir.lower() == "s"