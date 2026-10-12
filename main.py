# main()
# 705a.in
# Funciones
#from fixed_entrada import leer_fichero
import numpy as np
from entrada import leer_fichero
from algoritmo_voraz import resolver_asignacion_pupitres

ruta_fichero = input('¿Cuál es la ruta del fichero a analizar?: ')

num_veces_algoritmo, lista_num_alumnos, lista_matrices_amistad, lista_matrices_trabajo = leer_fichero(ruta_fichero)


solucion_clase = [] 
orden_alumnos = ''
beneficio_total_clase = 0

for i in range(num_veces_algoritmo):
    solucion_clase, beneficio_total_clase = resolver_asignacion_pupitres(lista_num_alumnos[i], lista_matrices_amistad[i], lista_matrices_trabajo[i])
    print(beneficio_total_clase, '\n')
    for j in solucion_clase:
        orden_alumnos += str(j) + ' '
    print(orden_alumnos, '\n')

