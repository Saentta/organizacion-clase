#Backtracking_2

def valor_asignacion(i, j, amistad:matrix, trabajo:matrix):
  valor = (amistad[i, j]+amistad[j, i])*(trabajo[i, j]+trabajo[j, i])
  return valor

def generar_asignacion(nivel:int, s:list, amistad:list, trabajo, usada:list, bact:float): #Probar primero 1, luego 2, ..., ​
    if s[nivel] == len(amistad)-1:
        return s, bact, usada
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

def criterio_asignacion(nivel:int, s:list, n:int, usada:list):
  return (usada[s[nivel]]==1) and (nivel < (n-1))

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
        if criterio_asignacion(nivel, s, n, usada):
            nivel= nivel + 1
        else:
            while not mas_hermanos_asignacion(nivel, s, n) and nivel >0:
                nivel, s, bact, usada= retroceder_asignacion(nivel, s, amistad, trabajo, usada, bact)
    return voa,soa

