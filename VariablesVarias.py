import csv


def cambio_conf(default = {}):
    """
 Te pregunta si desea cambiar los valores por default de las configuraciones,
en caso de ser afirmativo este se apoyara de la funcion graf_conf() para
tener una referencia de lo que el usuario desea cambiar. Al final retornara

Firma: Alejo
"""
    sigue = True
    while sigue:
        cambio = input("Ingrese el parametro que desee cambiar: ")
        while cambio < "1" and cambio > "7" or not cambio.isnumeric():
            cambio = input("Ingrese un numero entre 0 y 7: ")
        cambio_valor = input("Ingrese el nuevo valor: ")
        parametros = graf_conf()
        default[parametros[int(cambio)]] = int(cambio_valor)
        eleccion = input("¿Desea cambiar otro valor?[s/n]: ")
        while not eleccion.isalpha() or eleccion.lower() != "n" and eleccion.lower() != "s":
            eleccion = input("Por favor ingrese 's' o 'n': ")
        sigue = True if eleccion.lower() == 's' else False
    return default
    

def graf_conf(parametros = {}):
    """
Te brinda un diccionario con los nombres de los parametros con un numero
de referencia a cada uno.

Firma: Alejo
"""
    with open("configuracion.csv", "r") as conf:
        lectura = csv.reader(conf, delimiter=',')
        for parametro in lectura:
            parametros[len(parametros)+1]= parametro[0] 
    return parametros

        
