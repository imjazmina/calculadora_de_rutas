#Matriz bidimensional
filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("ingrese el numero de columnas: "))
mapa = [[" " for _ in range(filas)] for _ in range(columnas)]

#ingresar las coordenadas entreada y salida
fil_entrada, col_entrada = map(int, input("Ingrese la coordenada de entrada separado por comas: ").split(","))
fil_salida, col_salida = map(int, input("Ingrese las coordenadas de la salida separado por comas: ").split(","))

mapa[fil_entrada][col_entrada] = 'E'
mapa[fil_salida][col_salida] = 'S'

for row in mapa:
    for celda in row:
        print(f'[{celda}]', end= ' ')
    print("\n")

#agregar obstaculos
