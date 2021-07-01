# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:33:15 2019

@author: Isaac Stalley
"""
import random
try:
    data = int(input("1. Inserte año:"))
    if data % 4 == 0:
        if data % 400 == 0:
            print("Año:",data,"es bisiesto")
        elif data % 100 == 0:
            print("Año:",data,"no es bisiesto")
        else:
            print("Año:",data,"es bisiesto")
    else:
        print("Año:",data,"no es bisiesto")
except ValueError:
    print("Error de dato")
    

    
    
try:
    data = int(input("2. Inserte numero:"))
    i = 2
    while i < data:
        if data % i == 0:
            print("Numero:",data,"no es primo")
            i += data
        i += 1
    if data % data == 0 and i <= data:
            print("Numero:",data,"es primo")
except ValueError:
    print("Error de dato")
    



try:
    data = random.random()*100+1
    data = int(data)
    i = 101
    while i != data:
        dato = int(input("Adivine el numero de 1 a 100:"))
        i = dato
        if i < data:
            print("Su numero es menor")
        if i > data:
            print("Su numero es mayor")
        if i == data:
            print("Su numero es igual!")
except ValueError:
    print("Error de dato")




try:
    start = 0
    while start != 1:
        print("Inserte 1 para empezar:")
        start = int(input(":"))
    coins = 200
    while coins <= 300:
        i = 0
        coins2 = coins
        while i <= 3:
            if (coins2 % 3) == 1:
                r = coins2 // 3
                coins2 = coins2 - r -1
                if i == 3:
                    print(coins,"Si es la cantidad")
                    result = coins
            else:
                print(coins,"No es la cantidad")
                break
            i += 1
        coins = coins + 1
    print("Cantidad es:", result)
except ValueError:
    print("Error de dato")