import numpy as np
n = int(input('¿Tamaño matriz?: '))

with open(f'ejemplo{n}.txt', 'w') as f:
    f.write('1\n')
    f.write(f'{n}\n')
    linea = 0
    num_aleatorios = [np.random.randint(9)]*(2*(n*(n-1))) # generamos TODOS los números
    
    for numero in range(len(num_aleatorios)):
        if numero != 0 and (n-1)%numero == 0:
            linea += 1
            f.write(f'\n')
        f.write(f'{num_aleatorios[numero]} ')
