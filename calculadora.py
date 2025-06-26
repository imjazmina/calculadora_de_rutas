#Matriz bidimensional
filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("ingrese el numero de columnas: "))
mapa = [[" " for _ in range(filas)] for _ in range(columnas)]

# Ingresar y validar coordenadas de entrada y salida
def coordenadas_validas(fil, col):
    return 0 <= fil < filas and 0 <= col < columnas 

while True:
    fil_entrada, col_entrada = map(int, input("Ingrese la coordenada de entrada separado por comas: ").split(","))
    if coordenadas_validas(fil_entrada, col_entrada):
        break
    else:
        print("Coordenadas invalidas. Intente de nuevo")

while True:
    fil_salida, col_salida = map(int, input("Ingrese las coordenadas de la salida separado por comas: ").split(","))
    if coordenadas_validas(fil_salida, col_salida):
        break
    else:
        print("Coordenadas invalidas. Intente de nuevo")

mapa[fil_entrada][col_entrada] = 'E'
mapa[fil_salida][col_salida] = 'S'

for row in mapa:
    for celda in row:
        print(f'[{celda}]', end= ' ')
    print("\n")

#agregar obstaculos
