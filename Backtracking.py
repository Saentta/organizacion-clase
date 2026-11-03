# Backtracking

def resolver_asignacion_pupitres_backtracking(n, amistad, trabajo):
    '''
    Sabemos que va a haber una solución siempre.
    Sé que lo más óptimo va a ser empleando un árbol permutacional, puesto que si 
    asignamos un alumno i con otro j, ambos ya los podemos descartar del resto del algoritmo.
    podemos usar una matriz a de asignaciones n*n donde -1 no sea estudiado, 0 no se asigna 
    y 1 sí se asigna.
    '''
    import numpy as np
    
    nivel = 0
    fin = False
    mejor_beneficio = float('-inf')
    mejor_solucion = None
    beneficio_actual = 0
    solucion_actual = [-1]*n
    usada = [0]*n
    
    
    while nivel >= 0:
        solucion_actual, beneficio_actual, usada = generar(nivel, solucion_actual, amistad, trabajo, beneficio_actual, usada)

        if solucion(nivel, solucion_actual, n, amistad, trabajo, usada) and beneficio_actual > mejor_beneficio:
            mejor_beneficio = beneficio_actual
            mejor_solucion = solucion_actual.copy()

        if criterio(nivel, solucion_actual, n, usada, amistad, trabajo, beneficio_actual, mejor_beneficio):
            nivel += 1
        else:
            while not masHermanos(nivel, solucion_actual, n) and nivel >= 0:
                solucion_actual, beneficio_actual, nivel, usada = retroceder(nivel, solucion_actual, beneficio_actual, amistad, trabajo, usada)
                

    return mejor_solucion, mejor_beneficio
    
def generar(nivel, solucion_actual, amistad, trabajo, beneficio_actual, usada): 
    solucion_actual[nivel] += 1
    usada[solucion_actual[nivel]] += 1
    beneficio_iteracion = 0
    if solucion_actual[nivel] == 0:
        beneficio_iteracion = (amistad[nivel, solucion_actual[nivel]]+amistad[solucion_actual[nivel], nivel])*(trabajo[nivel, solucion_actual[nivel]]+trabajo[solucion_actual[nivel], nivel])
        beneficio_actual += beneficio_iteracion
        return solucion_actual, beneficio_actual, usada
    else:
        beneficio_iteracion = (amistad[nivel, solucion_actual[nivel]]+amistad[solucion_actual[nivel], nivel])*(trabajo[nivel, solucion_actual[nivel]]+trabajo[solucion_actual[nivel], nivel]) - (amistad[nivel, solucion_actual[nivel]-1]+amistad[solucion_actual[nivel]-1, nivel])*(trabajo[nivel, solucion_actual[nivel]-1]+trabajo[solucion_actual[nivel]-1, nivel]) 
        beneficio_actual += beneficio_iteracion
        usada[solucion_actual[nivel]-1]-=1
        return solucion_actual, beneficio_actual, usada

def criterio(nivel, solucion_actual, n, usada, amistad, trabajo, beneficio_actual, mejor_beneficio):
    import numpy as np
    
    estimacion_maxima = 0 
    for i in range(nivel+1, len(amistad)-1):
        maximo_fila = (np.amax(amistad[i]), np.amax(trabajo[i]))
        estimacion_maxima+= maximo_fila[0]*maximo_fila[1]
    if (beneficio_actual+ estimacion_maxima) <= mejor_beneficio:
       return False
    return usada[solucion_actual[nivel]] == 1 and nivel < (n-1)

def solucion(nivel, solucion_actual, n, amistad, trabajo, usada):
    return usada[solucion_actual[nivel]] == 1 and nivel == (n-1)

def masHermanos(nivel, solucion_actual, n):
    return solucion_actual[nivel] < (n-1)

def retroceder(nivel, solucion_actual, beneficio_actual, amistad, trabajo, usada):
    beneficio_actual -= (amistad[nivel, solucion_actual[nivel]]+amistad[solucion_actual[nivel], nivel])*(trabajo[nivel, solucion_actual[nivel]]+trabajo[solucion_actual[nivel], nivel])
    usada[solucion_actual[nivel]] = usada[solucion_actual[nivel]] - 1 
    solucion_actual[nivel] = -1
    nivel = nivel - 1
    return solucion_actual, beneficio_actual, nivel, usada