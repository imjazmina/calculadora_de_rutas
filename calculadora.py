import random

#Matriz bidimensional
filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("ingrese el numero de columnas: "))
mapa = [[0 for _ in range(columnas)] for _ in range(filas)]

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

def imprimir_mapa(mapa):
    for row in mapa:
        for celda in row:
            if celda == 0:
                print(f'[0]', end= ' ')
            elif celda == 1:
                print(f'[🏛️]', end= ' ')
            elif celda == 2:
                print(f'[🌊]', end= ' ')
            elif celda == 3:
                print(f'[🚧]', end= ' ')
            else:
                print(f'[{celda}]', end=' ')  
        print("\n")

def generar_obstaculos(filas, columnas, cantidad_obstaculos, mapa, fil_entrada, col_entrada, fil_salida, col_salida):
    obstaculos = [1, 2, 3]
    colocados = 0

    while colocados < cantidad_obstaculos:
        x = random.randint(0, filas - 1)
        y = random.randint(0, columnas - 1)

        mx = [x + 2, x - 2]
        my = [y + 2, y -2]

        nueva_x = random.choice(mx)
        nueva_y = random.choice(my)

        if (
            (nueva_x, nueva_y) != (fil_entrada, col_entrada)
            and (nueva_x, nueva_y) != (fil_salida, col_salida)
            and coordenadas_validas(nueva_x,nueva_y)
            and mapa[nueva_x][nueva_y] == 0
            #validar que los adyacentes no sean 3
        ):
            mapa[nueva_x][nueva_y] = random.choice(obstaculos)
            colocados += 1

def insertar_obstaculo(mapa, fila, columna):
    while True: 
        x_obstaculo, y_obstaculo = map(int,input("ingrese las coordenadas del nuevo obstaculo separado por comas").split(","))
        if not coordenadas_validas(x_obstaculo, y_obstaculo):
            print("Coordenadas invalidas. Ingrese nuevamente")
        elif (x_obstaculo, y_obstaculo) == (fil_entrada, col_entrada) and (x_obstaculo, y_obstaculo) == (fil_salida, col_salida):
            print("El obstaculo no puede estar sobre la entrada o salida")
        else:
            break
            
    tipo_obstaculo = int(input("Ingrese el tipo de obstaculo. 1 para 🏛️. 2 para 🌊. 3 para 🚧. : "))
    if tipo_obstaculo in [1, 2, 3]:
        mapa[x_obstaculo][y_obstaculo] = tipo_obstaculo
    else:
        print("Ingrese una opcion valida")
    
    return mapa[x_obstaculo][y_obstaculo]

cantidad_obstaculos = filas * columnas / 3
generar_obstaculos(filas, columnas, cantidad_obstaculos, mapa, fil_entrada, col_entrada, fil_salida, col_salida)
mapa[fil_entrada][col_entrada] = 'E'
mapa[fil_salida][col_salida] = 'S'
imprimir_mapa(mapa)

#funcion agregar obstaculo nuevo
opcion = input("Desea agregar/editar algun obstaculo? Y/N \nPresione N para salir: ").upper()
while opcion != 'N':
    insertar_obstaculo(mapa, filas, columnas)
    imprimir_mapa(mapa)
    opcion = input("Desea agregar/editar otro obstaculo? Y/N \nPresione N para salir: ").upper()


