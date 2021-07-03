








"""                     ETAPA 7 MULTIJUGADORES

'Al inicio se deberá solicitar el nombre de los jugadores, controlando que no se
ingresen más de 5, y que los nombre no se repitan. Podrá considerar que el ingreso
de nombres finaliza, cuando se da enter y no se ingresa nada.
Ingresados los nombres de los participantes, se deberán ordenar al azar para
asignarle el turno de juego a cada uno de ellos; y se les debe informar antes del
comienzo de la partida.

A partir de la segunda partida, el orden de los jugadores, deberá generarse
nuevamente, pero el ganador de la última partida, siempre tendrá el primer turno de
la siguiente; el resto de los turnos debe otorgarse de forma aleatoria'

()DEFINICION DE TURNOS ALEJO



'Luego se preguntará cuál será la longitud de la palabra a adivinar, y se aplicará la
misma longitud para todos los jugadores, pero se les deberá otorgar distintas
palabras. Si no se ingresa nada como valor de longitud, se entenderá que participan
todas las palabras, pero en este caso también, al elegir aleatoriamente las palabras a
adivinar para cada jugador, se les debe otorgar a todos palabras de igual longitud.
En cada nueva partida, volver a solicitar la longitud de la palabra a adivinar'

()DEFINIR: LONGITUD->PALABRA A ADIVINAR (main?) ROCIO



'Comienza el primer jugador según su turno,si acierta la letra,
elige una nueva letra así hasta que comete un desacierto y el 
turno pasara al siguiente jugador
Cuando uno de los jugadores llega al máximo de desaciertos, la partida continúa con
el resto de los jugadores.
En cada turno, se debe mostrar el nombre de quien está participando, además de
toda la información que se mostraba en la Parte 1 (palabra enmascarada, aciertos,
desaciertos, lista de letras utilizadas, puntaje parcial). El programa debe mostrar los
mismos mensajes que mostraba en la Parte 1, tanto para los aciertos, desaciertos,
letras ya elegidas, e ingresos inválidos.'

()REDEFINIR ETAPA1 ---


'Al finalizar cada partida, se debe mostrar el resultado de la partida, indicando para
cada jugador la palabra que debía adivinar, cantidad de aciertos y desaciertos, el
puntaje obtenido en la partida, y si hubo ganador, debe estar indicado.
Si se ha jugado más de una partida, también se debe mostrar los Resultados
Generales, indicando la cantidad de partidas jugadas; mostrando por jugador, los
datos ordenados por Puntaje Total, junto con la cantidad de aciertos y desaciertos, y
la cantidad de palabras adivinadas ó las veces que ha ganado. 
A continuación se debe preguntar si se desea jugar una nueva partida.'

()DEFINIR RESULTADOS ABIGAIL






'Si acierta la letra, suma 2 puntos
Si comete un desacierto se le resta 1 punto
Quien acierte primero la palabra suma 10 puntos
Si ninguno acierta, gana el programa, y en este caso se le restarán 5 puntos a cada jugador'

#Tener en cuenta: recibira por cada turno un diccionario:
Diccionario[Jugador][0] = PalabraAdivinar # Esto para saber quien gano primero (para sumar 10 puntos) o para saber si perdieron
Diccionario[Jugador][5] = PalabraOculta   # todos (resta 5 a todos): (PalabaraOculta.count('?') == 0) Gana, pierden si
                                          # Desaciertos == CANTIDAD_MAX_VIDAS (siendo esta 8)

Diccionario[Jugador][2] = aciertos
Diccionario[Jugador][3] = desaciertos
Diccionario[Jugador][6] = Puntos #Aqui actualizar los puntos


()REDEFINIR ETAPA5: PUNTOS   ROCIO-AXEL


"""



"""                 ETAPA 8 ARCHIVOS DE TEXTO

'Ahora que sabemos procesar archivos de texto, en lugar de utilizar la función que
nos devolvía un texto, a partir del cual generamos nuestras palabras; debemos
reemplazar esa parte del proceso, por otra que tome el texto, desde 3 ó más
archivos.
te pediremos que los leas línea por línea y deberás adaptar las funciones que 
generaban el diccionario de palabras, a esta nueva modalidad. 
Evita leer los archivos más de una vez, al igual que debes optimizar el acceso a
cualquier estructura auxiliar que utilices. 
'


'
Como salida de la lectura de los archivos, deberán generar el archivo palabras.csv,
que contendrá, todas las palabras obtenidas, ordenadas alfabéticamente, y en cada
línea, debe estar la palabra, y la cantidad de veces que aparece en cada archivo.
Por ejemplo:

Palabra,CantArchivo1,CantArchivo2,CantArchivo3
nubes,18,4,0
pajaros,3,0,12
puerta,5,8,2
'
ABIGAIL




'También deberán agregar un archivo de configuración, que se llamará
configuracion.csv, del cual leerán los valores iniciales que tomarán en la partida, los
siguientes elementos:
MAX_USUARIOS,10
LONG_PALABRA_MIN,5
MAX_DESACIERTOS,7
PUNTOS_ACIERTOS,10
PUNTOS_DESACIERTOS,5
PUNTOS_ADIVINA_PALABRA,100
PUNTOS_RESTA_GANA_PROGRAMA,20


Si por algún motivo, uno o más valores no pueden ser recuperados del archivo de
configuración, deben ser establecidos con valores por defecto. Una vez establecidos
los valores, al inicio de la aplicación, mostrar por pantalla, el valor efectivamente
asignado a cada elemento y si fue dado por omisión ó por configuración.
A partir de ahora, estos serán los valores que rijan nuestra partida, y podrán ser
variados antes de iniciar una nueva partida de cero'

ALEJO




"""