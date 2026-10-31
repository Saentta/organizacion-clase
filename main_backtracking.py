# main backtracking
import numpy as np
from entrada import leer_fichero
from Backtracking import resolver_asignacion_pupitres_backtracking


# Programa principial

ruta_fichero = input('¿Cuál es la ruta del fichero a analizar?: ')


num_veces_algoritmo, lista_num_alumnos, lista_matrices_amistad, lista_matrices_trabajo = leer_fichero(ruta_fichero) 


solucion_clase = [] 
orden_alumnos = ''
beneficio_total_clase = 0

for i in range(num_veces_algoritmo): # Llamada al algoritmo voraz, y lo efectuamos tantas veces como clases (num_veces_algortimo) haya
    solucion_clase, beneficio_total_clase = resolver_asignacion_pupitres_backtracking(lista_num_alumnos[i], lista_matrices_amistad[i], lista_matrices_trabajo[i])
    print(beneficio_total_clase, '\n')
    orden_alumnos = ''
    for i in solucion_clase:
        tem = i
        if i == None:
            i = ''
        elif i == None:
            i = ''

        orden_alumnos += str(i) + ' ' 
    print(orden_alumnos, '\n')

# 705a.in
#ejemplo.txt
#ejemplo2.txt