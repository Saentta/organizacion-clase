#Backtracking_4
#¿O€(n²!)?

def generar(nivel, s, n, usado, bact, matriz_beneficio):
    # Si existe, deshacemos el candidato anterior en este nivel 
    if s[nivel] != -1 and s[nivel] < n:
        usado[s[nivel]] -= 1
        if nivel % 2 == 1: # Comprobamos que no había una pareja ya formada
            bact -= matriz_beneficio[s[nivel-1], s[nivel]]
    
    # Avanzamos al siguiente candidato
    s[nivel] += 1
    
    # Aplicamos el nuevo candidato 
    if s[nivel] < n:
        usado[s[nivel]] += 1
        if nivel % 2 == 1:
            bact += matriz_beneficio[s[nivel-1], s[nivel]]
            
    return s, usado, bact

def solucion(nivel, s, n, usado):
    # Es solución cuando llegamos al último nivel y todos los alumnos están emparejados
    return (nivel == n - 1) and (s[nivel] < n) and (usado[s[nivel]] == 1)

def criterio(nivel, s, n, usado):
    
    if s[nivel] >= n: # Comprobamos de que no nos hayamos salido del rango
        return False
        
    # Como estamos trabajando con una matriz en esencia simetrica,
    # podemos podar y disminuir casi a la mitad las comprobaciones que hacemos
    # si nos quedamos con una parte triangular de la matriz_beneficio.
    # Para aprovechar esto obligamos que el numero del alumno sea mayor.
    
    if nivel % 2 == 1:
        if s[nivel] < s[nivel-1]:
            return False
            
    return (usado[s[nivel]] == 1) and nivel < n-1

def masHermanos(nivel, s, n):
    # Quedan hermanos si el numero del alumno actual no ha llegado al máximo
    return s[nivel] < n - 1

def retroceder(nivel, s, n, usado, bact, matriz_beneficio):
    # Deshacemos el beneficio del candidato actual antes de retroceder al nivel anterior
    if s[nivel] != -1 and s[nivel] < n:
        usado[s[nivel]] -= 1
        if nivel % 2 == 1:
            bact -= matriz_beneficio[s[nivel-1], s[nivel]]
            
    # Reseteamos el nivel actual y retrocedemos
    s[nivel] = -1
    nivel -= 1
    
    return nivel, s, usado, bact

def backtracking_opt(n, matriz_beneficio):
    nivel = 0
    s = [-1]*n
    usado = [0]*n
    voa = float('-inf')
    soa = []
    bact = 0
    
    while nivel >= 0:
        s, usado, bact = generar(nivel, s, n, usado, bact, matriz_beneficio)
        
        
        if solucion(nivel, s, n, usado) and bact > voa:
            voa = bact
            soa = s.copy()
            
        
        if criterio(nivel, s, n, usado):
            nivel = nivel + 1
        else:
            
            while nivel >= 0 and not masHermanos(nivel, s, n):
                nivel, s, usado, bact = retroceder(nivel, s, n, usado, bact, matriz_beneficio)
                
    return voa, soa