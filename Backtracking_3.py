#Backtracking_3
''' 
DUDAS:
    1. Sobre el beneficio total, me parece que se solapan sumas y se alcanza
    un beneficio muy disparado con respecto a el real.MEDIO SOLUCIONADO

    2. Sobre el analisis teorico y experimental, ¿gráfica? ¿nivel de exquisitez?:
        Teorico: conteo para llegar a una formula 
        Experimental: hacer programa que cree matrices n que aumenten de 10 en 10. Sacar gráficas comparacion teorico/real

    3. ¿Cómo pudiera acotar?:
        Tambien me permite adaptar leer_fichero para insertar valor asignacion y que nos quede una matriz simetrica
        (ADAPTAR CÓDIGO)
        max = 0 
        for i in range(n):
            for j in range(n):
                if not usada[i] and not usada[j]:
                    if valor_asigancion(i, j)> max:
                        max = valor

    4. ¿Qué hago si el número de alumnos es impar? O considerarlo para el final o añadir un alumno con afinidad(beneficio) 0

    5. No me queda claro como crear un árbol permutacional: es solo con la lista usada

    6. ¿Lo puedo hacer buscando una librería que permita crear arboles k-arios? Mejor no

   

ayuda no me gusta nada el backtracking practimente lo único que he hecho ha sido memorizarme el esquema general, mas siento que donadofnoslnfolacñlsnckawpeocnjawñecjnawñecjkan€¶đ¢“”đŋæßðſæ@€ŋŧ¶ŧ↓←¶”ð##~½¬{[¬½½½7[[]¬|@#|@3]]}
 '''



def generar_asignacion(nivel:int, s:list, matriz_beneficios, usada:list, bact:float): 
    
    if (s[nivel] >= 0) and (usada[s[nivel]] != 0):
        usada[s[nivel]] -= 1
    
    
    s[nivel]= s[nivel] + 1
    usada[s[nivel]] += 1

    i = nivel
    j= s[nivel]

    if s[nivel]==0:
        bact= bact + matriz_beneficios[i, j]
    else:
        bact= bact + matriz_beneficios[i, j] - matriz_beneficios[i, j-1]
    return s, bact, usada

def criterio_asignacion(nivel:int, s:list, n:int, usada:list, matriz_beneficios, bact, voa):
    '''estimacion_maxima = 0            
    s_copia = s
    tem = nivel
    for element in range(s.count(-1)):
        nivel = s_copia.index(-1)
        i = nivel
        j = s[nivel]
        if valor_asignacion(i, j, amistad, trabajo) > estimacion_maxima:
            estimacion_maxima = valor_asignacion(i, j, amistad, trabajo)
        s_copia.pop(-1)
    nivel = tem'''                  # INTENTO FALLIDO DE PODA (corta demasiado)
    '''estimacion_minima = float('inf')
    tem = s
    s_copia = s.copy()
    tem2 = nivel
    for element in range(s.count(-1)):
        nivel = s_copia.index(-1)
        i = nivel
        j = s[nivel]
        if valor_asignacion(i, j, amistad, trabajo) < estimacion_minima:
            estimacion_minima = valor_asignacion(i, j, amistad, trabajo)
        s_copia.pop(-1)
    s = tem
    nivel = tem2 ''' # INTENTO 2 FALLIDO (cota ramas correctas)  
    '''
    estimacion_cota = -1
    for i in range(nivel+1, n):
        for j in range(usada.count(0)+1):
            if valor_asignacion(i, s[j], matriz_beneficios) > estimacion_cota:
                estimacion_cota = valor_asignacion(i, s[j], matriz_beneficios)'''
    '''
    cota_max = 0
    
    for i in range(n):
        for j in range(n):
            if usada[i] == 0 and usada[j] == 0:
                if matriz_beneficios[i, j] > cota_max:
                    cota_max = matriz_beneficios[i, j]'''
    return (usada[s[nivel]] == 1) and (nivel < (n - 1))# and voa < cota_max

def solucion_asignacion(nivel:int, s:list, n:int, usada:list):
    if (nivel == (n-1)) and (s.count(0)==1) and (n%2==1):
        return True
    return (usada[s[nivel]]==1) and (nivel == (n-1))

def mas_hermanos_asignacion(nivel:int, s:list, n:int):
  return s[nivel] < (n-1)

def retroceder_asignacion(nivel:int, s:list, matriz_beneficios, usada:list, bact:float):

    i = nivel
    j= s[nivel]

    bact= bact - matriz_beneficios[i, j]
    usada[s[nivel]] -= 1
    s[nivel]= -1
    nivel= nivel - 1

    return nivel, s, bact, usada


def Backtracking_3(n, matriz_beneficios):
    
    nivel= 0
    voa= float('-inf')
    soa= 0
    bact = 0
    s = [-1]*n
    usada = [0]*n
    while nivel != -1:
        s, bact, usada= generar_asignacion(nivel, s, matriz_beneficios, usada, bact)
        if solucion_asignacion(nivel, s, n, usada) and bact > voa:
            voa= bact
            soa= s.copy()
        if criterio_asignacion(nivel, s, n, usada, matriz_beneficios, bact, voa):
            nivel= nivel + 1
        else:
            while not mas_hermanos_asignacion(nivel, s, n) and nivel >= 0:
                nivel, s, bact, usada= retroceder_asignacion(nivel, s, matriz_beneficios, usada, bact)
    return voa, soa

