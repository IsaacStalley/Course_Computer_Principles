# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:57:42 2019

@author: Isaac Stalley
"""

data = input("1. Factor mas grande, Inserte numero:")
i = 2
try:
    data = int(data)
    while (True):
        if data <= i:
            print ("Factores primos mas grandes:", data)
            break
        elif data % i == 0:
            data = data // i
            print("Factores primos mas grandes:", data)
            break
        else:
            i += 1
except ValueError:
    print("Error de dato")
    
    
    
    
data = input("2. Numeros amigos, Inserte numero:")
result = 0
result2 = 0
i = 1
j = 1
try:
    data = int(data)
    while i < data:
        if data % i == 0:
            result = result + i
        i += 1
    while j < result:
        if result % j == 0:
            result2 = result2 + j
        j += 1
    if result2 == data:
        print("True, Numeros amigos:",data,",",result)
    else:
        print("False, No existe numero amigo")
except ValueError:
    print("Error de dato")
    
    
    
    

data = input("3. Numeros perfectos, Inserte numero:")
result = 0
result2 = 0
i = 1
j = 1
try:
    data = int(data)
    while i < data:
        if data % i == 0:
            result = result + i
        i += 1
    
    if result == data:
        print("True, Numero perfecto:",data)
    else:
        print("False, No es numero perfecto")
except ValueError:
    print("Error de dato")
    
    
   
    
    
data = input("4. Numero narcisista, Inserte numero:")
j = 0
narc = 0
try:
    data = int(data)
    data1 = data
    data2 = data
    while data1 > 0:
        data1 = data1 // 10
        j += 1
    while data2 > 0:
        i = data2 % 10
        data2 = data2 // 10
        narc += i**j
    if narc == data:
        print ("True,",data,", es numero narcisista")
    else:
        print("False,",data,", no es numero narcisista")
       
except ValueError:
    print("Error de dato")




try:
    data = int(input("5. Convercion a binario, Inserte numero:"))
    i = 2
    c = ""
    while data > 0:
        r = data % i
        data = data // 2
        c += str(r)
    print("En binario:",c)
except ValueError:
    print("Error de dato")
    
    
    
    
try:
    i = int(input("6. Inserte la cantidad de numeros:"))
    num = 1
    print("Inserte numero",num,)
    j = int(input(":"))
    m = j
    x = j
    i -= 1
    s = 1
    prom = j
    while i > 0:
        num += 1
        print("Inserte numero",num,)
        data = int(input(":"))
        if data < m:
            m = data
        if data > x:
            x = data
        prom += data
        i -= 1
        s += 1
    prom = prom // s
    print("Minimo:",m)
    print("Maximo:",x)
    print("Promedio:",prom)
except ValueError:
    print("Error de dato")
    

    
    
try:
    a = float(input("7. Suma de Reimann, Inserte a:"))
    b = float(input("Inserte b:"))
    m = float(input("Inserte m:"))
    x = (b - a) / m
    n = 0
    r = 0
    while m > 0:
        n += x
        f = n**3 - 2*n**2 - n - 7
        r += f*x
        m -= 1
    #resultado varia un poco del ejemplo porque use la formula de suma de Riemann de lado derecha (toma diferentes puntos en la funcion)
    print("Tomando la suma de Reimann de lado derecha:")
    print("Suma de Riemann es:",r)
except ValueError:
    print ("Error de dato")