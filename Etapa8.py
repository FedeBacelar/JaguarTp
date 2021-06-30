def get_line(archivo):
    """Recibe un archivo para leerlo linea por linea y devuelve una lista con las palabras
    filtradas
    Firma: Abigail"""
    line = archivo.readline()
    if line:
        line = line.lower()
        lista = line.rstrip("\n").split(" ")
        lista = filtro(lista)                                     #la lista pasa por un filtro
    else:
        lista=0                                                   #devulve 0 si ya llego al final del texto
    return lista

def lista_cuentos(archivo):
    """recibe un archivo.txt y devuelve una lista con TODAS las palabras de ese archivo
    Firma: Abigail"""
    lista_palabras = []
    lista = get_line(archivo)
    while lista!=0:
        for palabra in lista:
            lista_palabras.append(palabra)
        lista=get_line(archivo)
    return lista_palabras

def escribir(archivo, dic):
    """Recibe y escribe en un archivo.csv lo del diccionario.
    Firma:Abigail"""
    for clave in dic:
        archivo.write(clave + "," + str(dic[clave][0]) + "," + str(dic[clave][1]) + ","+ str(dic[clave][2]) + "\n")
 
def crear_diccionario():
    """crea un diccionario con las palabras de los archivos y la cantidad de veces que aparece"""
    lista1=lista_cuentos(archivo1)
    lista2=lista_cuentos(archivo2)
    lista3=lista_cuentos(archivo3)
    minimo_letras= 5
    diccionario={}
    for palabra in lista1:
        if len(palabra)>= minimo_letras and palabra not in diccionario and palabra.isalpha():
                diccionario[palabra]=[lista1.count(palabra),lista2.count(palabra),lista3.count(palabra)]
    for palabra in lista2:
        if len(palabra)>= minimo_letras and palabra not in diccionario and palabra.isalpha():
                diccionario[palabra]=[lista1.count(palabra),lista2.count(palabra),lista3.count(palabra)]
    for palabra in lista3:
        if len(palabra)>= minimo_letras and palabra not in diccionario and palabra.isalpha():
                diccionario[palabra]=[lista1.count(palabra),lista2.count(palabra),lista3.count(palabra)]
                
    return diccionario


"""FUNCIONES DE LA ETAPA 2"""

def filtro(lista):
    """Filtra los acentos y símbolos de puntuación, devuelve la lista sin símbolos y omitiendo acentos
    Firma: Rocío"""
    cadena=""
    for elemento in lista:
        cadena+= ","+ elemento
    filtrar = cadena.maketrans("áéíòóúü,?¿¡!;.\"()_--:«»[]#", "aeioouu                   ")
    cadena = cadena.translate(filtrar)
    lista_filtrada= (cadena.split())
    
    return lista_filtrada

def diccionario_ordenado(diccionario):
    """Convirte un diccionario a una lista ordenada, retorna el diccionario ordenado
    Firma: Abigail"""
    lista=list(diccionario.items())
    lista.sort()
    ordenado = dict(lista)
    
    return ordenado

def GenerarDiccionario():
    """Firma: Rocío y Abigail"""
    diccionario = diccionario_ordenado(crear_diccionario())
    escribir(palabras,diccionario)
    #print diccionario
    #print ("El total de palabras es:", total_palabras())
    return diccionario



archivo1=open("Cuentos.txt","r")
archivo2=open("La araña negra - tomo 1.txt","r")
archivo3=open("Las 1000 Noches y 1 Noche.txt","r")
palabras=open("palabras.csv","w")

GenerarDiccionario()

archivo1.close()
archivo2.close()
archivo3.close()
palabras.close()

