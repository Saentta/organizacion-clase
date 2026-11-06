import numpy as np      # Nos hará falta para las matrices de amistad y trabajo

def leer_fichero(fichero_txt: str)->(int, int, list, list):
    with open(fichero_txt, 'r') as f: # Abrimos el fichero.txt con apodo f


        num_veces_algoritmo = 0
        num_alumnos = 0
        lista_num_alumnos = []
        lista_matrices_amistad = []   # Inicializamos las variables que vamos a usar
        lista_matrices_trabajo = []
        
        todas_las_lineas = f.readlines() # Leer las lineas del fichero
        f.seek(0)                      # volvemos a indicar el señalador al principio para estudiar linea a linea
        linea = f.readline()
        
        num_linea = 0
        if num_linea == 0:
                num_veces_algoritmo = int(linea.strip())  # obtenemos el número de veces que se ejecutará el algoritmo
                                                           # puesto que siempre se encuentra en la primera línea
        num_linea = 1
        linea = f.readline()

        while num_linea < len(todas_las_lineas)-2:  # comenzamos el bucle para abarcar todo el fichero
            
            
            if len(linea.strip().split()) == 1: # Con esta condición nos aseguramos el num_alumnos por clase,
                num_alumnos = int(linea.strip())   # puesto que salvo la primera linea, las únicas con un solo caracter son estas
                matriz_amistad_clase = np.matrix([[0]*num_alumnos]*(num_alumnos)) 
                matriz_trabajo_clase = np.matrix([[0]*num_alumnos]*(num_alumnos)) # Ambas matrices tienen la misma dimension
                lista_num_alumnos.append(num_alumnos)
                linea = f.readline()
                
            
            else:
                num_0_diagonal = 0
                for y in range(num_alumnos):
                    for x in range(num_alumnos-1): # Hacemos -1 porque en una iteracion añadimos dos numeros de golpe
                        if linea != '': # Esta condición es necesaria para el final del fichero y que no caiga en un bucle infinito
                            if x==y:    # reconozco que es un 'parche' y no es lo más óptimo, pero llevo 6 horas con esto;
                                        # he comprobado que funciona reiteradas ocasiones con los distintos ficheros de entrada
                                        # evaluando las salidas con el resto de ficheros, asi como el propio debugger de Python
                                        # siguiendo como evolucionan las variables. Entonces mi lógica en este punto es que
                                        # 'si no está roto, no lo arregles'-gracias.
                                matriz_amistad_clase[y, x] = 0 # Nos aseguramos de tener la diagonal 0
                                num_0_diagonal += 1
                                if len(matriz_amistad_clase) > x+1:
                                    matriz_amistad_clase[y, x+1] = int((linea.strip().split())[x]) 
                            else:
                                if x+1 <= num_0_diagonal:
                                    matriz_amistad_clase[y, x] = int((linea.strip().split())[x])
                                elif x+1 > num_0_diagonal:
                                    matriz_amistad_clase[y, x+1] = int((linea.strip().split())[x])
                        else:
                            break
                    linea = f.readline()
                    num_linea += 1
                lista_matrices_amistad.append(matriz_amistad_clase) # añadimos la matriz a la lista
                
                            
                                            # Inmediatamente después, están los valores para la matriz trabajo
                                            # Entonces repetimos el mismo proceso ahora con la matriz trabajo
                
                num_0_diagonal = 0
                for y in range(num_alumnos):
                    for x in range(num_alumnos-1): 
                        if linea != '':
                            if x==y:
                                matriz_trabajo_clase[y, x] = 0 # Nos aseguramos de tener la diagonal 0
                                num_0_diagonal += 1
                                if len(matriz_trabajo_clase) > x+1:
                                    matriz_trabajo_clase[y, x+1] = int((linea.strip().split())[x])
                            else:
                                if x+1 <= num_0_diagonal:
                                    matriz_trabajo_clase[y, x] = int((linea.strip().split())[x])
                                elif x+1 > num_0_diagonal:
                                    matriz_trabajo_clase[y, x+1] = int((linea.strip().split())[x])
                        else:
                            break
                    linea = f.readline()
                    num_linea += 1
                lista_matrices_trabajo.append(matriz_trabajo_clase)
                
            
    
    return (num_veces_algoritmo, lista_num_alumnos, lista_matrices_amistad, lista_matrices_trabajo)

def valor_asignacion(i, j, amistad:matrix, trabajo:matrix):
  valor = (amistad[i, j]+amistad[j, i])*(trabajo[i, j]+trabajo[j, i])
  return valor

def crea_matriz_beneficio(n, amistad, trabajo):
    
    matriz_beneficio = np.matrix([[2]*n]*n)
    for i in range(n):
        for j in range(n):
            matriz_beneficio[i, j] = (amistad[i, j] + amistad[j, i])* (trabajo[i, j] + trabajo[j, i])
    
    return matriz_beneficio


def genera_matrices(n):
    
    with open(f'ejemplo{n}.txt', 'w') as f:
        f.write('1\n')
        f.write(f'{n}\n')
        linea = 0
        num_aleatorios = list()
        for i in range(2*(n*(n-1))):
            num_aleatorios.append(np.random.randint(9)) # generamos TODOS los números
        
        for numero in range(len(num_aleatorios)):
            if numero != 0 and numero%(n-1) == 0:
                f.write(f'\n')
            f.write(f'{num_aleatorios[numero]} ')
