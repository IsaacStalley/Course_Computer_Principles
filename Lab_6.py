# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:38:46 2019

@author: Isaac Stalley
"""
import math

def point_function(a,b,c,d):
    return math.sqrt((d-b)**2+(c-a)**2)

def interseccion_cr(a,b,c,d,e,f,g):
    length1 = a
    length2 = point_function(b, c, d, e)
    length3 = point_function(b,c,d,(e+f))
    length4 = point_function(b,c,(d+g),e)
    length5 = point_function(b,c,(d+g),(e+f))
    if length1 >= length2 or length1 >= length3 or length1 >= length4 or length1 >= length5:
        return  True
    else:
        return False

inputs = ['x1', 'y1', 'x2','y2']
i =  0
while(i < len(inputs)):
    value = input("Inserte '" + inputs[i] + "':")
    try:
        inputs[i] = float(value)
        i+=1
    except ValueError:
        print("error de dato")

result = point_function(inputs[0], inputs[1], inputs[2], inputs[3])
print("La distancia es:",result)



inputs2 = ['r1', 'x1', 'y1','x2','y2']
i =  0
while(i < len(inputs2)):
    value = input("Inserte '" + inputs2[i] + "':")
    try:
        inputs2[i] = float(value)
        i+=1
    except ValueError:
        print("error de dato")

point1 = point_function(inputs2[1], inputs2[2], inputs2[3], inputs2[4])
point2 = inputs2[0]
if point2 >= point1:
    print("Punto 2 si pertenece al circulo")
else:
    print("Punto 2 no pertenece al circulo")
    
    
    
inputs3 = ['r1', 'x1', 'y1','x2','y2','h','a']
i =  0
while(i < len(inputs3)):
    value = input("Inserte '" + inputs3[i] + "':")
    try:
        inputs3[i] = float(value)
        i+=1
    except ValueError:
        print("Error de dato")


result2 = interseccion_cr(inputs3[0], inputs3[1], inputs3[2], inputs3[3], inputs3[4], inputs3[5], inputs3[6])
print(result2)