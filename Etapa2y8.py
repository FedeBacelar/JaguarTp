def diccionario_ordenado(diccionario):
    """Convirte un diccionario a una lista ordenada, retorna el diccionario ordenado
    Firma: Abigail"""
    lista=list(diccionario.items())
    lista.sort()
    ordenado = dict(lista)
    return ordenado


def total_palabras():
    """Retorna la cantidad de palabras que hay en el diccionario
    Firma: Rocío"""
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


"""------------------------------------------------------ETAPA8------------------------------------------------------------------"""

def get_line(archivo):
    """Recibe un archivo para leerlo linea por linea y devuelve una lista con las palabras
    filtradas de ESA LINEA.
    Firma: Abigail """
    
    line = archivo.readline()
    if line:
        line = line.lower()
        lista = line.rstrip("\n").split(" ")
        lista = filtro(lista)                                     
    else:
        lista=0                                                  
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
    
    lista=crear_lista(lista_archivos)                 
    minimo_letras = 5
    diccionario = {}
    for lista_palabras in lista:
        
        NUM_ARCHIVO= lista.index(lista_palabras)       
        
        for palabra in lista_palabras:
            if len(palabra)>= minimo_letras and palabra.isalpha():                  
                if palabra not in diccionario:                                      
                    diccionario[palabra]=[0 for x in range(0,len(lista_archivos))]  
                diccionario[palabra][NUM_ARCHIVO]+=1                           
             
    return diccionario


def crear_lista(lista_archivos):
    """Recibe una lista de archivos y devuelve una lista de la lista de palabras de cada uno de los archivos
    Firma: Abigail """
    lista=[]
    for i in range(0,len(lista_archivos)):             
        lista_total=lista_de_palabras(lista_archivos[i])      
        lista.append(lista_total)                             
    return lista
    
def GenerarDiccionario():
    """Firma: Rocío y Abigail"""
    with open("ArchivoTexto\Cuentos.txt","r") as archivo1, open("ArchivoTexto\La araña negra - tomo 1.txt","r") as archivo2, open("ArchivoTexto\Las 1000 Noches y 1 Noche.txt","r") as archivo3, open("ArchivoTexto\palabras.csv","w") as palabras:
        lista_archivos = [archivo1,archivo2,archivo3]
        diccionario = diccionario_ordenado(crear_diccionario(lista_archivos))
        escribir(palabras,diccionario)

    return diccionario
