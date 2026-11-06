# main backtracking
import numpy as np
from entrada import leer_fichero, crea_matriz_beneficio
from backtracking import backtracking_opt
# Programa principial

ruta_fichero = input('¿Cuál es la ruta del fichero a analizar?: ')


num_veces_algoritmo, lista_num_alumnos, lista_matrices_amistad, lista_matrices_trabajo = leer_fichero(ruta_fichero) 


solucion_clase = [] 
orden_alumnos = ''
beneficio_total_clase = 0

for i in range(num_veces_algoritmo): # Llamada al algoritmo voraz, y lo efectuamos tantas veces como clases (num_veces_algortimo) haya
    matriz_beneficio = crea_matriz_beneficio(lista_num_alumnos[i], lista_matrices_amistad[i], lista_matrices_trabajo[i])
    beneficio_total_clase, solucion_clase = backtracking_opt(lista_num_alumnos[i], matriz_beneficio)
    print(beneficio_total_clase, '\n')
    orden_alumnos = ''
    for alumno in solucion_clase:
        
        if alumno == None:
            alumno = ''
        elif alumno == None:
            alumno = ''

        orden_alumnos += str(alumno) + ' ' 
    print(orden_alumnos, '\n')

#905a.in
#905b.in
#905c.in
#ejemplo.txt