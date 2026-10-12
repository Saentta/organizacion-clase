def resolver_asignacion_pupitres(n, amistad, trabajo):
    # 1. Generar todos los candidatos (parejas posibles i, j con i < j)
    # y calcular su beneficio potencial.
    candidatos = []
    for i in range(n):
        for j in range(i + 1, n):
            # Beneficio de la pareja (i, j): (Amistad mutua) * (Trabajo mutuo)
            beneficio_amistad = amistad[i, j] + amistad[j, i]
            beneficio_trabajo = trabajo[i, j] + trabajo[j, i]
            beneficio_total_pareja = beneficio_amistad * beneficio_trabajo
            
            candidatos.append((beneficio_total_pareja, i, j))   #Metemos el beneficio de cada pareja en la lista hasta quedarnos sin alumnos
            
    # 2. Ordenar los candidatos de mayor a menor beneficio (Criterio voraz)
    candidatos.sort(key=lambda x: x[0], reverse=True)
    
    # 3. Estructuras de estado
    alumnos_asignados = [False] * n #Esto nos servirá para comprobar si las parejas de alumnos estan ya o no sentadas en un pupitre
    solucion = []   #Esta lista nos servira para mostrar la salida de la solución del algoritmo
    beneficio_total = 0
    
    # 4. Proceso voraz de selección
    for beneficio, i, j in candidatos:
        # Función de viabilidad: ambos alumnos deben estar libres
        if not alumnos_asignados[i] and not alumnos_asignados[j]:
            # Seleccionar la pareja
            solucion.append((i, j))
            alumnos_asignados[i] = True #Aqui nos encargamos de modificar la lista para que no volvamos a seleccionar a las mismas personas i y j
            alumnos_asignados[j] = True
            beneficio_total += beneficio #Por último, se van sumando los beneficios a la variable que tenemos creada
            
            # Si ya hemos emparejado a todos (o solo queda 1 libre), podemos parar
            if sum(1 for asignado in alumnos_asignados if not asignado) <= 1:
                break
                
    # 5. Identificar si algún alumno se ha quedado solo (en caso de N impar)
    if n % 2 != 0:
        for i in range(n):
            if not alumnos_asignados[i]:
                alumno_solo = i
                print(alumno_solo)
                break
            
    return solucion, beneficio_total