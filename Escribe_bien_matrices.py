# Escribe_bien_matrices
from entrada import leer_fichero

i = input('¿De que ejemplo va a ser el fichero?: ')

with open(f'matriz_ejemplo{i}', 'w') as f:
    num_veces_algoritmo, lista_num_alumnos, lista_matrices_amistad, lista_matrices_trabajo = leer_fichero(f'ejemplo{i}.txt')
    for i in range(num_veces_algoritmo):
        f.write(f'{lista_matrices_amistad[i]}\n\n{lista_matrices_trabajo[i]}')

