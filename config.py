def config():
    """
Retorna un diccionario, teniendo como keys las palabras claves de configuracion y
como values, los valores de cada palabra clave

Firma: Alejo
"""
    confi_dict = {"MAX_USUARIOS": 10,"LONG_PALABRA_MIN": 5,"MAX_DESACIERTOS": 7,"PUNTOS_ACIERTOS": 10,"PUNTOS_DESACIERTOS": 5,"PUNTOS_ADIVINA_PALABRA": 100,"PUNTOS_RESTA_GANA_PROGRAMA": 2}
    with open("configuracion.csv", "r+") as conf:
        for linea in conf:
            print(linea)
            texto_limpiado = limpieza(linea)
            confi_dict = cambio_valores(confi_dict, texto_limpiado)
    return confi_dict

def limpieza(texto):
    """
Brinda una lista el conforme el texto de la configuracion dado.
Dejandolo en optimas condiciones para su uso en config()

Firma: Alejo
"""
    texto = texto.split(",")
    if len(texto) > 1:
        texto[1] = int(texto[1])
    return texto

def cambio_valores(confi_dict, lista):
    """
Cambia valores de la lista default si cumple con ciertos requisitos, luego la devuelve

Firma: Alejo, FedeBacelar
"""
    
    if len(lista) == 2:
        for key in confi_dict:
            if key == lista[0] and type(lista[1]) == int:
                confi_dict[key] = lista[1]
    return confi_dict
