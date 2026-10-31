import numpy as np

def validador_I_AR(fichero_entrada, fichero_salida, fichero_salida_profesor=None):
    
    """
    Función que valida el algoritmo implementado para el ejercicio H_AR.
    Parámetros:
        * fichero_entrada: ruta al fichero con los datos de entrada con los que se ha alimentado el algoritmo propuesto.
        * fichero_salida: ruta al fichero con los resultados generados por el algoritmo propuesto.
        * fichero_salida_profesor: ruta al fichero con los resultados de prueba proporcionados por el profesor (opcional).
    """
    
    file_salida= open(fichero_salida)
    
    file_salida_prof= None
    if fichero_salida_profesor is not None:
        file_salida_prof= open(fichero_salida_profesor)

    contador = 0
    porcentaje_acumulado = 0

    with open(fichero_entrada) as file:
        num_pruebas= int(file.readline())
        
        for i in range(num_pruebas):
            num_alumnos= int(file.readline())            
            
            mat_= []
            for j in range(0,num_alumnos):
                a = [int(number) for number in file.readline().strip().split(' ')]  
                mat_.append(a)

            amistad= np.vstack(mat_)  
            
            mat_= []
            for j in range(0,num_alumnos):
                a = [int(number) for number in file.readline().strip().split(' ')]  
                mat_.append(a)

            trabajo= np.vstack(mat_)  
            
            beneficio= int(file_salida.readline())
            s= [int(number) for number in file_salida.readline().strip().split(' ')]  
            
            beneficio_prof= None
            if file_salida_prof:
                beneficio_prof= int(file_salida_prof.readline())
                file_salida_prof.readline()

            if len(s) != len(set(s)):
                print(f"ERROR en el caso {i}: La asignación obtenida contiene alumnos repetidos.")
            else:
                beneficio_calculado=0
                for j in range(0,len(s)-1,2):
                    a= s[j]
                    b= s[j+1]
                    
                    if a < b:
                        beneficio_calculado += ((amistad[a,b-1]+amistad[b,a])*(trabajo[a,b-1]+trabajo[b,a]))  
                    else: # b < a
                        beneficio_calculado += ((amistad[a,b]+amistad[b,a-1])*(trabajo[a,b]+trabajo[b,a-1])) 
                                        
                if beneficio != beneficio_calculado:
                    print(f"ERROR en el caso {i}: el beneficio de la asignación no se ha calculado correctamente. Beneficio indicado: {beneficio}. Beneficio correcto: {beneficio_calculado}")
                elif (beneficio_prof is not None):
                    #and (ratio_variacion is not None) and (beneficio < (beneficio_prof * (1-ratio_variacion))):
                    if beneficio > beneficio_prof:
                        print (f"En el caso {i}: El beneficio de tu algoritmo {beneficio}, es superior al de los profesores {beneficio_prof}.")
                    elif beneficio == beneficio_prof:
                        contador += 1
                        porcentaje_acumulado += 100
                        print (f"En el caso {i}: Todo correcto y el porcentaje de beneficio es del 100%.")
                    else:
                        if beneficio != 0:
                            porcentaje = 100-(((beneficio_prof-beneficio) / beneficio) * 100)
                            contador += 1
                        contador += 1
                        porcentaje_acumulado += porcentaje
                        print (f"En el caso {i}: Todo correcto y el porcentaje de beneficio ({beneficio},{beneficio_prof}) es del {round(porcentaje,2)}%.")
                else:
                    print(f"Todo correcto para el caso {i}.")     
    if beneficio != 0: 
        print(f"La media porcentual para {contador}.")
    else:
        print(f"La media porcentual para {contador} casos es del {round(porcentaje_acumulado/contador,2)}%.")
                

#Ejemplo de invocación   
letra = input('¿De qué fichero estamos hablando?: ')             
validador_I_AR(f'705{letra}.in', f'705{letra}.in_estudiantes', fichero_salida_profesor=f'705{letra}.out')
