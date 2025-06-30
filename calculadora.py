import random
from heapq import heappush, heappop

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
                print('[ ]', end= ' ')
            elif celda == 1:
                print('[🏛️]', end= ' ') 
            elif celda == 2:
                print('[🌊]', end= ' ')
            elif celda == 3:
                print('[🚧]', end= ' ')
            elif celda == '*':
                print('[✅]', end=' ')
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

def insertar_obstaculo(mapa, fila, columna):# fila y columna no se utilizan
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

# A ⭐
#heuristica
def distancia_manhatan(fil_entrada, col_entrada, fil_salida, col_salida):
    return abs(fil_entrada-fil_salida) + abs(col_entrada - col_salida)

# funcion para crear la lista con las coordenadas del camino mas corto una vez llegado al objetivo
def reconstruir_camino(visitado, pos_actual):
    camino = [pos_actual]
    while pos_actual in visitado: 
        pos_actual = visitado[pos_actual] 
        camino.append(pos_actual) 
    camino.reverse()#reversa los elementos en la lista para que al imprimir lo muestre desde el inicio 
    return camino

def obtener_movimientos(pos, filas, columnas):
    movimientos = []
    x, y = pos
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    for dx, dy in direcciones:
        nueva_x = x + dx
        nueva_y = y + dy
        if 0 <= nueva_x < filas and 0 <= nueva_y < columnas:
            movimientos.append((nueva_x, nueva_y))
    return movimientos

def a_estrella(mapa, filas, columnas, fil_entrada, fil_salida, col_entrada, col_salida):
    por_recorrer = []
    pos_inicio = (fil_entrada, col_entrada)
    pos_salida = (fil_salida, col_salida)

    heappush(por_recorrer, (0, pos_inicio))

    visitado = {}
    g_score = {pos_inicio: 0}
    f_score = {pos_inicio: distancia_manhatan(*pos_inicio, *pos_salida)}

    while por_recorrer:
        _, actual = heappop(por_recorrer)

        if actual == pos_salida:
            return reconstruir_camino(visitado, actual)
        
        movimientos = obtener_movimientos(actual, filas, columnas)
        for movimiento in movimientos:

            if mapa[movimiento[0]][movimiento[1]] in [1,2,3]:
                continue

            intento_g_score = g_score[actual] + 1
            if movimiento not in g_score or intento_g_score < g_score[movimiento]:
                visitado[movimiento] = actual
                g_score[movimiento] = intento_g_score
                f_score[movimiento] = intento_g_score + distancia_manhatan(*movimiento, *pos_salida)
                heappush(por_recorrer, (f_score[movimiento], movimiento))

    return None # no se encontro un camino
  

cantidad_obstaculos = int(filas * columnas / 3)
generar_obstaculos(filas, columnas, cantidad_obstaculos, mapa, fil_entrada, col_entrada, fil_salida, col_salida)
mapa[fil_entrada][col_entrada] = 'E'
mapa[fil_salida][col_salida] = 'S'
camino = a_estrella(mapa, filas, columnas, fil_entrada, fil_salida, col_entrada, col_salida)
if camino:
    for x, y in camino:
        if (x, y) != (fil_entrada, col_entrada) and (x, y) != (fil_salida, col_salida):
            mapa[x][y] = '*'
else:
    print("No se encontro un camino al destino.")

imprimir_mapa(mapa)
#funcion limpiar mapa
for i in range(filas):
    for j in range(columnas):
        if mapa[i][j] == '*':
            mapa[i][j] = 0


#funcion agregar obstaculo nuevo
opcion = input("Desea agregar/editar algun obstaculo? Y/N \nPresione N para salir: ").upper()
while opcion != 'N':
    insertar_obstaculo(mapa, filas, columnas)
    #funcion limpiar mapa
    for i in range(filas):
        for j in range(columnas):
            if mapa[i][j] == '*':
                mapa[i][j] = 0
    camino = a_estrella(mapa, filas, columnas, fil_entrada, fil_salida, col_entrada, col_salida)
    
    if camino:
        for x, y in camino:
            if (x, y) != (fil_entrada, col_entrada) and (x, y) != (fil_salida, col_salida):
                mapa[x][y] = '*'
    imprimir_mapa(mapa)

    opcion = input("Desea agregar/editar otro obstaculo? Y/N \nPresione N para salir: ").upper()

