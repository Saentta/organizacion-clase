# main()
# 705a.in
# Funciones
import time
import numpy as np
from entrada import leer_fichero
from algoritmo_voraz import resolver_asignacion_pupitres

ruta_fichero = input('¿Cuál es la ruta del fichero a analizar?: ')

tiempo_ini = time.time()
tiempo_ini_cpu = time.process_time()
num_veces_algoritmo, lista_num_alumnos, lista_matrices_amistad, lista_matrices_trabajo = leer_fichero(ruta_fichero)


solucion_clase = [] 
orden_alumnos = ''
beneficio_total_clase = 0

for i in range(num_veces_algoritmo):
    solucion_clase, beneficio_total_clase = resolver_asignacion_pupitres(lista_num_alumnos[i], lista_matrices_amistad[i], lista_matrices_trabajo[i])
    print(beneficio_total_clase, '\n')
    for i, j in solucion_clase:
        orden_alumnos += str(i) + ' ' + str(j) + ' '
    print(orden_alumnos, '\n')

tiempo_fin = time.time()
tiempo_fin_cpu = time.process_time()

tiempo_tot = tiempo_fin - tiempo_ini
tiempo_tot_cpu = tiempo_fin_cpu - tiempo_ini_cpu

print(f'El tiempo total de ejecución es: {tiempo_tot}')
print(f'El tiempo de ejecución del procesador es: {tiempo_tot_cpu}')
