#Matriz bidimensional
filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("ingrese el numero de columnas: "))
mapa = [[" " for _ in range(filas)] for _ in range(columnas)]

#salida =  int(input("Ingrese la coordenada de salida: "))

fil_entrada, col_entrada = int(input("Ingrese la coordenada de entrada: ")).split(",")
fil_salida, col_salida = salida.split()

mapa[fil_entrada][col_entrada] == 'E'
mapa[fil_salida][col_salida] == 'S'

for row in mapa:
    for celda in row:
        print(f'[{celda}]', end= ' ')
    print("\n")

#Ingresar coordenadas de entrada y salida

