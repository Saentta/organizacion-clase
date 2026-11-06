# Experimetacion

# Funciones
import numpy as np
import time 
import matplotlib.pyplot as plt
from entrada import leer_fichero, crea_matriz_beneficio, genera_matrices
from backtracking import backtracking_opt
from algoritmo_voraz import resolver_asignacion_pupitres

# Programa principial
# Genera n ficheros aleatorios y compara tanto los tiempos como los beneficios de 
# sendos algoritmos creados.

n = int(input('¿Número de experimentos?: '))
rutas_ficheros = []
for i in range(3, n):
    genera_matrices(i) # Generamos matrices aleatorias de tamaño hasta n
    rutas_ficheros.append(str(f'ejemplo{i}.txt')) 



for i in range(len(rutas_ficheros)):
    num_veces_algoritmo, lista_num_alumnos, lista_matrices_amistad, lista_matrices_trabajo = leer_fichero(rutas_ficheros[i]) 

    lista_beneficio_total_clase_ar = [0]*len(rutas_ficheros)
    lista_beneficio_total_clase_backtracking = [0]*len(rutas_ficheros)
    lista_tiempos_ar = [0]*len(rutas_ficheros)
    lista_tiempos_backtracking = [0]*len(rutas_ficheros)

    # Leemos los datos aleatorios e inicializamos las listas que despues usaremos para mostrar
    # gráficas con la que podamos diferenciar los algoritmos

    for j in range(num_veces_algoritmo): 
        # Calculamos para con el algoritmo backtracking, almacenando el benfecio y tiempo
        matriz_beneficio = crea_matriz_beneficio(lista_num_alumnos[j], lista_matrices_amistad[j], lista_matrices_trabajo[j])
        tiempo_inicio = time.process_time()
        beneficio_total_clase_backtracking, solucion_clase = backtracking_opt(lista_num_alumnos[j], matriz_beneficio)
        tiempo_fin = time.process_time()
        tiempo_total_backtracking = tiempo_fin- tiempo_inicio
        lista_beneficio_total_clase_backtracking[j] = beneficio_total_clase_backtracking
        lista_tiempos_backtracking[j] = tiempo_total_backtracking


        # Calculamos para con el algoritmo voraz, almacenando el benfecio y tiempo
        tiempo_inicio = time.process_time()
        beneficio_total_clase_ar, solucion_clase_ar = resolver_asignacion_pupitres(lista_num_alumnos[j], lista_matrices_amistad[j], lista_matrices_trabajo[j])
        tiempo_fin = time.process_time()
        tiempo_total_ar = tiempo_fin - tiempo_inicio
        lista_beneficio_total_clase_ar[j] = beneficio_total_clase_ar
        lista_tiempos_ar[j] = tiempo_total_ar
    
    # Generamos las matrices comparativas
    x = np.arange(3, n)
    plt.figure()
    plt.subplot(211)
    plt.plot(x, lista_tiempos_ar, lista_tiempos_backtracking)

    plt.subplot(212)
    plt.plot(x, lista_beneficio_total_clase_ar, lista_beneficio_total_clase_backtracking)
    plt.show()
    
    
