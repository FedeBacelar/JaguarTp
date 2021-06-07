def Puntaje(Aciertos, Desaciertos, Puntos=0):
    """
    Toma como parametros: Aciertos(int), Desaciertos(int), Puntos(int)
    Retorna los puntos del usuario
    Firma: FedeBacelar
    """
    Puntos += (Aciertos*10 - Desaciertos*5)
    return Puntos


def SeguirJuego():
    """
    Retorna la solicitud de "seguir jugando" del usuario en forma de: True o False
    FedeBacelar: FedeBacelar
    """
    seguir = str(input("Desea seguir jugando? (s/n)"))
    return seguir.lower() == "s"
    
