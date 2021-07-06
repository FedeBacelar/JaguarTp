import csv
import os
from config import*


def cambio_conf():
    """
 Te pregunta si desea cambiar los valores por default de las configuraciones,
en caso de ser afirmativo este se apoyara de la funcion graf_conf() para
tener una referencia de lo que el usuario desea cambiar. Al final retornara

Firma: Alejo
"""
    eleccion = input("Antes de iniciar el juego, ¿Desea cambiar algun valor de la configuracion?[s/n]: ")
    while not eleccion.isalpha() or eleccion.lower() != "n" and eleccion.lower() != "s":
            eleccion = input("Por favor ingrese 's' o 'n': ")
    sigue = True if eleccion.lower() == "s" else False
    while sigue:
        parametros = opc_conf()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(grafico_conf(parametros))
        cambio = input("Ingrese el parametro que desee cambiar: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        while not cambio.isnumeric() or int(cambio) < 1 or int(cambio) > 7:
            cambio = input("Ingrese un numero entre 0 y 7: ")
            os.system('cls' if os.name == 'nt' else 'clear')
        cambio_valor = input("Ingrese el nuevo valor: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        while not cambio_valor.isnumeric() or int(cambio_valor) <= 0:
            cambio_valor= input("Ingrese un valor numerico mayor a 0: ")
            os.system('cls' if os.name == 'nt' else 'clear')
        with open("configuracion.csv", "r") as leo_conf:
            lectura = csv.reader(leo_conf, delimiter=",")
            with open("configuracion_nueva.csv","w") as nueva_conf:
                escritura = csv.writer(nueva_conf, delimiter=",")
                for fila in lectura:
                    if parametros[int(cambio)] in fila:
                        fila[1] = int(cambio_valor)
                    escritura.writerow(fila)
        os.remove("configuracion.csv")
        os.rename("configuracion_nueva.csv", "configuracion.csv")
        eleccion = input("¿Desea cambiar otro valor?[s/n]: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        while not eleccion.isalpha() or eleccion.lower() != "n" and eleccion.lower() != "s":
            eleccion = input("Por favor ingrese 's' o 'n': ")
            os.system('cls' if os.name == 'nt' else 'clear')
        sigue = True if eleccion.lower() == 's' else False
    return "Cambio Hecho!!"
    

def opc_conf(parametros = {}):
    """
Te brinda un diccionario con los nombres de los parametros con un numero
de referencia a cada uno.

Firma: Alejo
"""
    with open("configuracion.csv", "r") as conf:
        lectura = list(csv.reader(conf, delimiter=','))
        for valor in range(len(lectura)):
            parametros[valor+1] = lectura[valor][0] 
    return parametros


def grafico_conf(parametros):
    """
Genra un grafico en el cual el usuario podra visualizar que parametros puede alterar
"""
    long = 40
    print("-"*long)
    with open("configuracion.csv", "r") as l_conf:
        lectura = list(csv.reader(l_conf))
        for variable in list(parametros.keys()):
            print("{} - {}: {}".format(variable, parametros[int(variable)], lectura[int(variable)-1][1]))
    return "-"*long

def config_final():
    cambio_conf()
    return config()

parametros = config_final()
