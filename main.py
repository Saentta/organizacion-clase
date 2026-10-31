# main()
# TRABAJO REALIZADO POR: SERGIO CANDEL YELO Y CÉSAR MARTÍNEZ-LOZANO PÉREZ
# Funciones

import time
import numpy as np

from entrada import leer_fichero
from algoritmo_voraz import resolver_asignacion_pupitres


# Programa principial

ruta_fichero = input('¿Cuál es la ruta del fichero a analizar?: ')


num_veces_algoritmo, lista_num_alumnos, lista_matrices_amistad, lista_matrices_trabajo = leer_fichero(ruta_fichero) 


solucion_clase = [] 
orden_alumnos = ''
beneficio_total_clase = 0

tiempo_ini = time.time()
tiempo_ini_cpu = time.process_time()

for i in range(num_veces_algoritmo): # Llamada al algoritmo voraz, y lo efectuamos tantas veces como clases (num_veces_algortimo) haya
    solucion_clase, beneficio_total_clase = resolver_asignacion_pupitres(lista_num_alumnos[i], lista_matrices_amistad[i], lista_matrices_trabajo[i])
    print(beneficio_total_clase, '\n')
    orden_alumnos = ''
    for i, j in solucion_clase:
        
        if i == None:
            i = ''
        elif j == None:
            j = ''

        orden_alumnos += str(i) + ' ' + str(j) + ' '
    print(orden_alumnos, '\n')

tiempo_fin = time.time()
tiempo_fin_cpu = time.process_time()

tiempo_tot = tiempo_fin - tiempo_ini
tiempo_tot_cpu = tiempo_fin_cpu - tiempo_ini_cpu

print(f'El tiempo total de ejecución es: {tiempo_tot}')
print(f'El tiempo de ejecución del procesador es: {tiempo_tot_cpu}\n')


'''
{{{los tiempos teóricos se han conseguido a través de aplicar la suma de
la función n²log n en cada uno de los tamaños de las matrices de cada fichero.
La media del estimado sobre los tiempos de ejecución.}}}

El algorimo voraz tiene un orden de complejidad perteneciente a O(n²log n)
705a.in
705b.in
705c.in
Tiempos:
    a)
    tiempo de ejecución: 0.1330571174621582, 0.10887360572814941, 0.13779568672180176, 0.14369559288024902, 0.2236313819885254 
    tiempo del procesador: 0.128227121, 0.10770671699999995,  0.134160987, 0.13596801500000005, 0.18216102199999995
    media del estimado: 0.164836 s
    tiempo teorico: 0.11701586 s
    b)
    tiempo de ejecución: 0.05843615531921387, 0.0558619499206543, 0.05261826515197754, 0.04905986785888672, 0.05064058303833008
    tiempo del procesador: 0.05616674700000002, 0.055117954999999996, 0.05196587800000002, 0.04850251, 0.04983665100000001
    media del estimado: 0.052317948200000006 s
    tiempo teorico: 0.07477 s
    c)
    tiempo de ejecución: 0.13597583770751953, 0.11869049072265625, 0.11525464057922363, 0.12622404098510742, 0.12553739547729492 
    tiempo del procesador: 0.134337221,  0.11629435599999999, 0.11525464057922363, 0.12224422000000001, 0.12331044600000002
    media del estimado: 0.12228817671584473 s
    tiempo teorico: 0.13460386 s

la media del error obtenido entre el tiempo teórico y real es el siguiente: 0.0275 s; suponemos que del propio 'ruido' del portátil
(otros procesos, acumulación en la caché, incluso los propios bucles que 'ignoramos' cuando suponemos que n tiende a infinito...).
Pese a ello, se ajusta con un error cuadrático medio de: 9.80*10⁽⁻⁴⁾

Tiempo conjunto dedicado 10 horas.

'''
