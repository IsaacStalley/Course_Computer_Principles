"""
Created on Sat Nov 16 20:24:12 2019

@author: Isaac Stalley
"""

def intercambiar_filas(matriz, i, j):
    temp = matriz[i]
    matriz[i] = matriz[j]
    matriz[j] = temp
    return matriz

def multiplicar_fila(matriz, i, escalar):
    for x in range(len(matriz[i])):
        matriz[i][x] = matriz[i][x] * escalar
    return matriz

def sumar_filas(matriz, i, j, escalar):
    for x in range(len(matriz[i])):
        matriz[i][x] = matriz[i][x] + matriz[j][x] * escalar
    return matriz

def restar_filas(matriz, i, j, escalar):
    for x in range(len(matriz[i])):
        matriz[i][x] = matriz[i][x] - matriz[j][x] * escalar
    return matriz

def cargar_matriz(nombre_archivo):
    try:
        f = open(nombre_archivo, 'r')
        matriz = []
        for x in f:
            temp = x.split(',')
            temp[-1] = temp[-1][: -1]
            for j in range(len(temp)):
                temp[j] = float(temp[j])
            matriz.append(temp)
        if len(matriz) == 3:
            if len(matriz[0]) == 4 and len(matriz[1]) == 4 and len(matriz[2]) == 4:
                return matriz
            else:
                print("Archivo de matriz no aceptado")
        else:
            print("No existe solución para el sistema")
        f.close()
    except IOError:
        print("El archivo especificado no existe")

def gauss_jordan(matriz):
    for x in range(3):
        if matriz[0][x] == 0 and matriz[1][x] == 0 and matriz[2][x] == 0:
            return None
        if matriz[x][0] == 0 and matriz[x][1] == 0 and matriz[x][2] == 0:
            return None
    stop = False
    while stop == False:
        if matriz[0][0] == 0:
            if matriz[1][0] == 0:
                matriz = intercambiar_filas(matriz, 0, 2)
            else:
                matriz = intercambiar_filas(matriz, 0, 1)
        if matriz[1][1] == 0:
            matriz = intercambiar_filas(matriz, 1, 2)
        if matriz[0][1] != 0 or matriz[0][2] != 0 or matriz[0][0] != 1:
            value = matriz[0][0]
            for i in range(4):
                matriz[0][i] = matriz[0][i] / value  
            matriz = restar_filas(matriz, 1, 0, matriz[1][0])
            matriz = restar_filas(matriz, 2, 0, matriz[2][0])
        if matriz[0][0] == -1:
            for i in range(4):
                if matriz[0][i] != 0:
                    matriz[0][i] = matriz[0][i] * -1
        if matriz[1][0] != 0 or matriz[1][2] != 0 or matriz[1][1] != 1:
            value = matriz[1][1]
            for i in range(4):
                matriz[1][i] = matriz[1][i] / value
            matriz = restar_filas(matriz, 0, 1, matriz[0][1])
            matriz = restar_filas(matriz, 2, 1, matriz[2][1])
        if matriz[1][1] == -1:
            for i in range(4):
                if matriz[1][i] != 0:
                    matriz[1][i] = matriz[1][i] * -1
        if matriz[2][0] != 0 or matriz[2][1] != 0 or matriz[2][2] != 1:
            value = matriz[2][2]
            for i in range(4):
                matriz[2][i] = matriz[2][i] / value
            matriz = restar_filas(matriz, 0, 2, matriz[0][2])
            matriz = restar_filas(matriz, 1, 2, matriz[1][2])
        if matriz[2][2] == -1:
            for i in range(4):
                if matriz[2][i] !=0:
                    matriz[2][i] = matriz[2][i] * -1
        test = 0
        for i in range(3):
            for x in range(3):
                if matriz[i][x] == 0:
                    test += 1
        if test == 6:
            stop = True      
    print("Valor 1:",matriz[0][3])
    print("Valor 2:",matriz[1][3])
    print("Valor 3:",matriz[2][3])
    return matriz

#path = cargar_matriz('test.csv')
#gauss_jordan(path)