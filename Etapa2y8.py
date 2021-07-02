
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

"""------------------------------------------------------ETAPA8------------------------------------------------------------------"""

def get_line(archivo):
    """Recibe un archivo para leerlo linea por linea y devuelve una lista con las palabras
    filtradas de ESA LINEA.
    Firma: Abigail """
    
    line = archivo.readline()
    if line:
        line = line.lower()
        lista = line.rstrip("\n").split(" ")
        lista = filtro(lista)                                     #la lista pasa por un filtro
    else:
        lista=0                                                   #devuelve 0 si ya llego al final del texto
    return lista


def lista_de_palabras(archivo):
    """Recibe un archivo.txt y devuelve una lista con TODAS las palabras de ese archivo
    Firma: Abigail """
    
    lista_palabras = []
    lista = get_line(archivo)
    while lista!=0:
        for palabra in lista:
            lista_palabras.append(palabra)
        lista=get_line(archivo)
    return lista_palabras


def escribir(archivo,dic):
    """Recibe y escribe en un archivo.csv lo del diccionario.
    Firma:Abigail """
    
    for clave in dic:
        archivo.write(clave)
        for i in range(0,len(dic[clave])):
            archivo.write("," + str(dic[clave][i]))
        archivo.write("\n")
 
 
def crear_diccionario(lista_archivos):
    """Recibe una lista de archivos para crear un diccionario con las palabras de estos archivos y la cantidad de veces que aparece
     Firma:Abigail """
    
    lista=crear_lista(lista_archivos)                 #Lista de la lista de palabras de los archivos
    minimo_letras = 5
    diccionario = {}
    for lista_palabras in lista:
        
        NUM_ARCHIVO= lista.index(lista_palabras)       #indica que archivo estoy usando
        
        for palabra in lista_palabras:
            if len(palabra)>= minimo_letras and palabra.isalpha():                  #Condicion de que la palabra sean puras letras y que sea mayor al minimo de letras
                if palabra not in diccionario:                                      
                    diccionario[palabra]=[0 for x in range(0,len(lista_archivos))]  #Como valor pone una lista de 0, segun la cantidad de archivos
                diccionario[palabra][NUM_ARCHIVO]+=1                           
             
    return diccionario


def crear_lista(lista_archivos):
    """Recibe una lista de archivos y devuelve una lista de la lista de palabras de cada uno de los archivos
    Firma: Abigail """
    lista=[]
    for i in range(0,len(lista_archivos)):             
        lista_total=lista_de_palabras(lista_archivos[i])      #lista de todas las palabras de ese archivo
        lista.append(lista_total)                             
    return lista
    
def GenerarDiccionario():
    """Firma: Rocío y Abigail"""
    with open("Cuentos.txt","r") as archivo1, open("La araña negra - tomo 1.txt","r") as archivo2, open("Las 1000 Noches y 1 Noche.txt","r") as archivo3, open("palabras.csv","w") as palabras:
        lista_archivos = [archivo1,archivo2,archivo3]
        diccionario = diccionario_ordenado(crear_diccionario(lista_archivos))
        escribir(palabras,diccionario)

    return diccionario

