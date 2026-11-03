#Backtracking_2
''' 
DUDAS:
    1. Sobre el beneficio total, me parece que se solapan sumas y se alcanza
    un beneficio muy disparado con respecto a el real.

    2. Sobre el analisis teorico y experimental, ¿gráfica? ¿nivel de exquisitez?

    3. ¿Cómo pudiera acotar? 

    4. ¿Qué hago si el número de alumnos es impar?

ayuda no me gusta nada el backtracking practimente lo único que he hecho ha sido memorizarme el esquema general, mas siento que donadofnoslnfolacñlsnckawpeocnjawñecjnawñecjkan€¶đ¢“”đŋæßðſæ@€ŋŧ¶ŧ↓←¶”ð##~½¬{[¬½½½7[[]¬|@#|@3]]}
 '''

def valor_asignacion(i, j, amistad:matrix, trabajo:matrix):
  valor = (amistad[i, j]+amistad[j, i])*(trabajo[i, j]+trabajo[j, i])
  return valor

def generar_asignacion(nivel:int, s:list, amistad:list, trabajo, usada:list, bact:float): 
    
    if (s[nivel] >= 0) and (usada[s[nivel]] != 0):
        usada[s[nivel]] -= 1
    
    
    s[nivel]= s[nivel] + 1
    usada[s[nivel]] += 1

    i = nivel
    j= s[nivel]

    if s[nivel]==0:
        bact= bact + valor_asignacion(i, j, amistad, trabajo)
    else:
        bact= bact + valor_asignacion(i, j, amistad, trabajo) - valor_asignacion(i, j-1, amistad, trabajo)
    return s, bact, usada

def criterio_asignacion(nivel:int, s:list, n:int, usada:list, amistad, trabajo):
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
    estimacion_minima = float('inf')
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
    nivel = tem2
    return (usada[s[nivel]]==1) and (nivel < (n-1)) and s[nivel] > estimacion_minima

def solucion_asignacion(nivel:int, s:list, n:int, usada:list):
    return (usada[s[nivel]]==1) and (nivel == (n-1))

def mas_hermanos_asignacion(nivel:int, s:list, n:int):
  return s[nivel] < (n-1)

def retroceder_asignacion(nivel:int, s:list, amistad, trabajo, usada:list, bact:float):

    i = nivel
    j= s[nivel]

    bact= bact - valor_asignacion(i, j, amistad, trabajo)
    usada[s[nivel]] -= 1
    s[nivel]= -1
    nivel= nivel - 1

    return nivel, s, bact, usada


def Backtracking_2(n, amistad, trabajo):
    
    nivel= 0
    voa= float('-inf')
    soa= None
    bact = 0
    s = [-1]*n
    usada = [0]*n
    while nivel != -1:
        s, bact, usada= generar_asignacion(nivel, s, amistad, trabajo, usada, bact)
        if solucion_asignacion(nivel, s, n, usada) and bact > voa:
            voa= bact
            soa= s.copy()
        if criterio_asignacion(nivel, s, n, usada, amistad, trabajo):
            nivel= nivel + 1
        else:
            while not mas_hermanos_asignacion(nivel, s, n) and nivel >= 0:
                nivel, s, bact, usada= retroceder_asignacion(nivel, s, amistad, trabajo, usada, bact)
    return voa, soa

