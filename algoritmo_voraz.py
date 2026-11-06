def resolver_asignacion_pupitres(n, amistad, trabajo):
    # 1. Generar todos los candidatos (parejas posibles i, j con i < j (debido a que añadimos una diagonal de 0's en la anterior función))
    # y calcular su beneficio potencial. En este caso n es el tamaño de las matrices de amistad y trabajo, con un valor maximo de 100.
    candidatos = []
    for i in range(n):
        for j in range(i + 1, n):
            # Beneficio de la pareja (i, j): (Amistad mutua) * (Trabajo mutuo)
            beneficio_amistad = amistad[i, j] + amistad[j, i]
            beneficio_trabajo = trabajo[i, j] + trabajo[j, i]
            beneficio_total_pareja = beneficio_amistad * beneficio_trabajo
            #Este doble bucle anidado tiene una complejidad de el orden de O(n²)
            candidatos.append((beneficio_total_pareja, i, j))   #Metemos el beneficio de cada pareja en la lista hasta quedarnos sin alumnos
            
    # 2. Ordenar los candidatos de mayor a menor beneficio (Criterio voraz)
    candidatos.sort(key=lambda x: x[0], reverse=True)
    #La lista contiene n(n-1)/2 elementos, que son todas las posibles parejas. Por tanto, al ordenar la lista tenemos una complejidad del orden de O(n²log n)
    
    # 3. Estructuras de estado
    alumnos_asignados = [False] * n #Esto nos servirá para comprobar si las parejas de alumnos estan ya o no sentadas en un pupitre. Esto tiene una complejidad del orden de O(n)
    solucion = []   #Esta lista nos servira para mostrar la salida de la solución del algoritmo
    beneficio_total = 0
    
    # 4. Proceso voraz de selección
    for beneficio, i, j in candidatos:
        # Función de viabilidad: ambos alumnos deben estar libres
        if alumnos_asignados[i]==False and alumnos_asignados[j]==False:
            # Seleccionar la pareja
            solucion.append((i, j))
            alumnos_asignados[i] = True #Aqui nos encargamos de modificar la lista para que no volvamos a seleccionar a las mismas personas i y j
            alumnos_asignados[j] = True
            beneficio_total += beneficio #Por último, se van sumando los beneficios a la variable que tenemos creada
            #En este bucle se recorreran O(n²) candidatos

           
                
    # 5. Identificar si algún alumno se ha quedado solo (en caso de N impar)
    if n % 2 != 0:
        for i in range(n):
            if alumnos_asignados[i] == False:
                alumno_solo = i
                solucion.append((alumno_solo, None))
                break
         #Este ultimo bucle tiene una complejidad lineal de orden de O(1)   
    return solucion, beneficio_total


#T(n) = O(n²) + O(n²log n) + O(n) + O(n²)
#La complejidad temporal total del ejercicio queda entonces del orden de O(n²log n).