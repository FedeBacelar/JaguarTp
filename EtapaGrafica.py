
def Grafico(Desaciertos, StrContador, PuntosEnPartida, StrMensaje, cadenaOculta, NombreJugador):
    """
    Esta funcion proporciona al usuario una interfaz grafica con listas en forma de matriz
    En funcion de los desaciertos corresponde una matriz
    Firma: FedeBacelar
    """

    Dibujo = ()
    if Desaciertos == 0:
        Dibujo = ([" "," "," "," "," "],[" "," "," "," ",""],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," ",""],[""," "," "," "," "],[" ","","","",""])
    elif Desaciertos == 1:
        Dibujo = ([" "," "," "," "," "],[" "," "," "," ",""],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," ",""],[""," ","/"," ","\ "],[" ","","","",""])
    elif Desaciertos == 2:
        Dibujo = ([" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," ","  "],[" ",""," ","|",""],[""," ","/"," ","\ "],["","","","",""])
    elif Desaciertos == 3:
        Dibujo = ([" "," "," "," "," "],[" "," "," "," ",""],[" "," "," "," "," "],[" "," "," ","|"," "],[" "," "," ","|",""],[" "," ","/"," ","\ "],[" ","","","",""])
    elif Desaciertos == 4:
        Dibujo = ([" "," "," "," "," "],[" "," "," "," ",""],[" "," "," "," "," "],[" "," ","/","|","\ "],[" "," "," ","|",""],[" "," ","/"," ","\ "],[" ","","","",""])
    elif Desaciertos == 5:
        Dibujo = ([" "," "," "," "," "],[" "," "," "," ",""],[" "," "," ","O"," "],[" "," ","/","|","\ "],[" "," "," ","|",""],[" "," ","/"," ","\ "],[" ","","","",""])
    elif Desaciertos == 6:
        Dibujo = ([" "," "," "," "," "],["|"," "," "," ",""],["|"," "," ","O"," "],["|"," ","/","|","\ "],["|"," "," ","|",""],["|"," ","/"," ","\ "],[" ","","","",""])
    elif Desaciertos == 7:
        Dibujo = (["_","_","_","_","_"],["|"," "," "," ",""],["|"," "," ","O"," "],["|"," ","/","|","\ "],["|"," "," ","|",""],["|"," ","/"," ","\ "],[" ","","","",""])
    elif Desaciertos == 8:
        Dibujo = (["_","_","_","_","_"],["|"," "," ","|",""],["|"," "," ","O"," "],["|"," ","/","|","\ "],["|"," "," ","|",""],["|"," ","/"," ","\ "],["","","","",""])
    h = 7
    for Lista in Dibujo:
        for elemento in Lista:
            print(elemento, end="")
        if h == 7:
            print("    " + "Turno de: " + NombreJugador, end="")
        if h == 6:
            print("    " + StrContador +" Puntos:"+str(PuntosEnPartida), end="")
        elif h == 2:
            print("       " + StrMensaje + "--> " + cadenaOculta, end="")
        
        h -= 1

        print("")