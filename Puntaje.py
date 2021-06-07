def tabla(nombre, puntos):
	"""
	Genera una caja con puntajes
	Firma: Alejo
	"""
	tabla = NombresYPuntos(nombre, puntos)
	constructor = []
	long_mayor = palabra_grande(tabla)
	longitud_tabla = len(tabla)
	espaciado = 10
	print("\nTABLA DE PUNTAJES:")
	for salto in range(0, longitud_tabla, 2):
		constructor += "\n"+"-"*(long_mayor + espaciado ) + "\n¬ {} --> {}".format(tabla[salto], tabla[salto+1]) 
	constructor = "".join(constructor)
	return constructor
	

def palabra_grande(nombres):
	"""
	Retorna la posicion de la palabra mas grande
	Firma: Alejo
	"""
	acumulador = []
	for nombre in nombres:
		acumulador += [len(str(nombre))]
	return max(acumulador)
	
	
def NombresYPuntos(nombre, puntos):
	"""
	Brinda una lista con nombres y puntajes
	Firma: Alejo
	"""
	archivo = open("tabla_puntajes.txt", "r+")
	tabla = archivo.readline()
	tabla = separador(tabla)
	if nombre in tabla:
		pos = tabla.index(nombre)
		tabla[pos+1] = str(puntos)
		archivo.close()
	else:
		archivo.write("{}-{}-".format(nombre, puntos))
		archivo.close()
		archivo = open("tabla_puntajes.txt", "r+")
		tabla = archivo.readline()
		tabla = separador(tabla)
		archivo.close()
	return tabla


def separador(tabla):
	"""
	Quita los << - >> de la lista 
	Firma: Alejo
	"""
	tabla = tabla.split("-")
	tabla = " ".join(tabla)
	tabla = tabla.split()
	return tabla


def datos():
	nombre = input("¿Cual es su nombre?: ")
	while nombre == "":
		nombre = input("Debe colocar al menos un caracter: ")
	return nombre

