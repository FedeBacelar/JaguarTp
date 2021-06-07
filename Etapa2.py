from texto import obtener_texto


def crear_diccionario():
    """"Recibe un texto y crea un diccionario con las palabras, retorna un diccionario con
    la palabra y la cantidad de veces que esta aparece en el texto
    Firma: Abigail"""
    texto= obtener_texto()
    texto= texto.lower()
    lista= texto.split()
    lista= filtro(lista)
    diccionario={}
    minimo_letras= 5
    for palabra in lista:
        if len(palabra)>= minimo_letras and palabra not in diccionario:
                diccionario[palabra]= lista.count(palabra)
    return diccionario


def diccionario_ordenado(diccionario):
    """Convirte un diccionario a una lista ordenada, retorna el diccionario ordenado
    Firma: Abigail"""
    lista=list(diccionario.items())
    lista.sort()
    ordenado = dict(lista)
    return ordenado


def total_palabras():
    """Retorna la cantidad de palabras que hay en el diccionario
    Firma:Rocío"""
    return (len(crear_diccionario().keys()))


def filtro(lista):
    """Filtra los acentos y símbolos de puntuación, devuelve la lista sin símbolos y omitiendo acentos
    Firma: Rocío"""
    cadena=""
    for elemento in lista:
        cadena+= ","+ elemento
    filtrar = cadena.maketrans("áéíòóúü,?¿¡!;.\"()_--:«»", "aeioouu                ")
    cadena = cadena.translate(filtrar)
    lista_filtrada= (cadena.split())
    return lista_filtrada


def GenerarDiccionario():
    """Firma: Rocío y Abigail"""
    diccionario = diccionario_ordenado(crear_diccionario())
    #print diccionario
    #print ("El total de palabras es:", total_palabras())
    return(diccionario)
