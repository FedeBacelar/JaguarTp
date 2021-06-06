import random

def pedir_longitud():
    """
    Le pide al usuario la longitud de la palabra candidata y devuelve esa longitud
    Firma: Abigail
    """
    Condicion = str(input("Desea condicionar la longitud de la palabra a adivinar? (s/n): "))
    if Condicion.lower() == "s":
        return int(input("Ingrese Longitud (Si el numero ingresado es menor a la longitud minima(5) se tomara el valor minima): "))


def palabras_candidatas(Diccionario,Longitud = None):
    """
    Recibe como parametros un diccionario y longitud(opcional)
    Retorna una lista con palabras candidatas (si no se especifica la longitud esta sera aleatoria)
    Firma: Abigail
    """ 
    LONGITUD_MINIMA = 5
    ListaKeys = list(Diccionario.keys())
    if Longitud:
        Longitud = LONGITUD_MINIMA if Longitud <= LONGITUD_MINIMA else Longitud
        Lista = [Palabra for Palabra in ListaKeys if len(Palabra) == Longitud]
    else:
        Lista = ListaKeys

    return Lista

def elegir_palabra_aleatoria(Diccionario, longitud):
    """
    Recibe un Diccionario y una longitud, devuelve una clave aleatoria de la misma longitud
    Firma: Abigail
    """
    palabra=random.choice(palabras_candidatas(Diccionario,longitud))
    return palabra