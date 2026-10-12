import numpy as np      # Nos hará falta para las matrices de amistad y trabajo

def leer_fichero(fichero_txt: str)->(int, int, list, list):
    with open(fichero_txt, 'r') as f: # Abrimos el fichero.txt con apodo f


        num_veces_algoritmo = 0
        num_alumnos = 0
        lista_num_alumnos = []
        lista_matrices_amistad = []   # Inicializamos las variables que vamos a usar
        lista_matrices_trabajo = []
        
        todas_las_lineas = f.readlines()
        f.seek(0)                      # Leer las lineas del fichero
        linea = f.readline()
        
        num_linea = 0
        if num_linea == 0:
                num_veces_algoritmo = int(linea.strip()) 
        
        num_linea = 1

        while num_linea < len(todas_las_lineas):
            linea = f.readline()
            
            if len(linea.strip().split()) == 1: # Con esta condición nos aseguramos el num_alumnos por clase,
                num_alumnos = int(linea.strip())   # puesto que como el segundo caracter de las matrices va a ser siempre 
                matriz_amistad_clase = np.matrix([[0]*num_alumnos]*(num_alumnos))# un espacio vacio; nos apoyamos en esto.
                matriz_trabajo_clase = np.matrix([[0]*num_alumnos]*(num_alumnos)) # Ambas matrices tienen la misma dimension
                lista_num_alumnos.append(num_alumnos)
                
            
            else:
                num_0_diagonal = 0
                for y in range(num_alumnos-1):
                    for x in range(num_alumnos-1): # Tenemos que hacer +2 porque las matrices son num_alumnos-1 
                        if x==y:
                            matriz_amistad_clase[y, x] = 0 # Nos aseguramos de tener la diagonal 0
                            num_0_diagonal += 1
                            if len(matriz_amistad_clase) > x+1:
                                matriz_amistad_clase[y, x+1] = int((linea.strip().split())[x])
                        else:
                            if x+1 <= num_0_diagonal:
                                matriz_amistad_clase[y, x] = int((linea.strip().split())[x])
                            elif x+1 > num_0_diagonal:
                                matriz_amistad_clase[y, x+1] = int((linea.strip().split())[x])
                    linea = f.readline()
                    num_linea += 1
                lista_matrices_amistad.append(matriz_amistad_clase) # añadimos la matriz a la lista
                
                linea = f.readline()
                num_linea +=1               
                                            # Inmediatamente después, están los valores para la matriz trabajo
                                            # Entonces repetimos el mismo proceso ahora con la matriz trabajo
                
                num_0_diagonal = 0
                for y in range(num_alumnos-1):
                    for x in range(num_alumnos-1): # Tenemos que hacer +2 porque las matrices son num_alumnos-1 
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
                    linea = f.readline()
                    num_linea += 1
                lista_matrices_trabajo.append(matriz_trabajo_clase)
                
            num_linea += 1 
    
    return (num_veces_algoritmo, lista_num_alumnos, lista_matrices_amistad, lista_matrices_trabajo)