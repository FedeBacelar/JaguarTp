def config():
    """
    Retorna un diccionario, teniendo como keys las palabras claves de configuracion y
    como values, los valores de cada palabra clave

    Firma: Alejo
    """
    long_deseada = 7
    confi_dict = {}
    posicion = 0
    with open("Configuraciones.csv", "r+") as conf:
        for linea in conf:
            texto_limpiado = limpieza(linea)
            lista, posicion = busqueda_error(texto_limpiado, posicion)
            confi_dict[lista[0]] = lista[1]
            
        while posicion < 7:
            lista, posicion = busqueda_error([], posicion)
            confi_dict[lista[0]] = lista[1]
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

def busqueda_error(lista, posicion):
    """
    Busca errores en la lista extraida del archivo csv, de presentar errores se colocan los valores por defecto

    Firma: Alejo
    """
    n_def = ["MAX_USUARIOS","LONG_PALABRA_MIN","MAX_DESACIERTOS","PUNTOS_ACIERTOS","PUNTOS_DESACIERTOS","PUNTOS_ADIVINA_PALABRA","PUNTOS_RESTA_GANA_PROGRAMA"]
    v_def = [10, 5, 7, 10, 5, 100, 2]
    if len(lista) != 2:
        lista_aprobada = [n_def[posicion], v_def[posicion]]
    elif len(lista) == 2:
            lista[0] = n_def[posicion] if lista[0] != n_def[posicion] else lista[0]
            lista[1] = v_def[posicion] if type(lista[1]) is not int else lista[1]
            lista_aprobada = lista
    posicion += 1
    return lista_aprobada, posicion


 # Falta reparar unos bugs cuando se borra una linea de la configuracion.csv pero para cambios erroneos en una linea funciona perfecto. Los problemas
 # surgen cuando se borra una linea de la configuracion.csv pues ahi reescribira los datos y asignara valores de forma ordenada cuando la realidad es
 # que el archivo al estar desordenado, asignara valores ordenados lo cual es indeseado para el jugador

