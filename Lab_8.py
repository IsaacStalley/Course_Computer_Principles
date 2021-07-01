# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:15:15 2019

@author: Isaac Stalley
"""
import math
def promedio_function(a):
    i = 0
    counter = 0
    while i < len(a):
        counter += a[i]
        i += 1
    if len(a) != 0:
        promedio = counter / len(a)
        return promedio
    else:
        return 0


def desvest_function(a):
    i = 0
    desvest = 0
    sums = 0
    promedio = promedio_function(a)
    while i < len(a):
        counter = a[i]
        sums += (counter - promedio)**2
        i += 1
    if len(a) != 0:
        desvest += math.sqrt(sums / len(a))
    return desvest


def sort_function(a):
    i = 0
    counter = 0
    while counter <= len(a):
        while i+1 <= len(a)-1:
            if a[i] > a[i+1]:
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp
            i += 1
        i = 0
        counter += 1
    return a


def replace_function(a,b,c):
    i = 0
    while i <= len(a)-1:
        if a[i] == b:
            a[i] = c
        i += 1
    return a


#presione enter para probar la lista vacia
data = input("Inserte una lista para el promedio (separado por comas):")
list_1 = data.split(',')
list_2 = []
i = 0
while (i < len(list_1) and len(list_1) > 1):
    counter = list_1[i]
    s = False
    while s == False:
        try:
            counter = float(counter)
            s = True
        except ValueError:
            print("Corrige dato en la posicion,",i,)
            counter = input(":")
    list_2.append(counter)
    i += 1
print("El promedio de la lista es:",promedio_function(list_2))


#presione enter para probar la lista vacia
data = input("Inserte una lista para desvest (separado por comas):")
list_1 = data.split(',')
list_2 = []
i = 0
while (i < len(list_1) and len(list_1) > 1):
    counter = list_1[i]
    s = False
    while s == False:
        try:
            counter = float(counter)
            s = True
        except ValueError:
            print("Corrige dato en la posicion,",i,)
            counter = input(":")
    list_2.append(counter)
    i += 1
print("El desviacion estandar de la lista es:",desvest_function(list_2))


#presione enter para probar la lista vacia
data = input("Inserte una lista para sortear (separado por comas):")
list_1 = data.split(',')
list_2 = []
i = 0
while (i < len(list_1) and len(list_1) > 1):
    counter = list_1[i]
    s = False
    while s == False:
        try:
            counter = float(counter)
            s = True
        except ValueError:
            print("Corrige dato en la posicion,",i,)
            counter = input(":")
    list_2.append(counter)
    i += 1
print("La lista en orden es:",sort_function(list_2))


#presione enter para probar la lista vacia
data = input("Inserte una lista (separado por comas):")
list_1 = data.split(',')
list_2 = []
i = 0
while (i < len(list_1) and len(list_1) > 1):
    counter = list_1[i]
    s = False
    while s == False:
        try:
            counter = float(counter)
            s = True
        except ValueError:
            print("Corrige dato en la posicion,",i,)
            counter = input(":")
    list_2.append(counter)
    i += 1
i = 0
while i == 0:
    try:
        b = float(input("Inserte valor para sustituir:"))
        i +=1
    except ValueError:
        print("Error de dato")
i = 0
while i == 0:
    try:
        c = float(input("Inserte nuevo valor para reemplazar:"))
        i +=1
    except ValueError:
        print("Error de dato")
print("La nueva lista es:",replace_function(list_2,b,c))