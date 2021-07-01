# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:24:12 2019

@author: Isaac Stalley
"""

import math
data = input("Inserte un valor para convertir a °F:")
try:
    data = float(data)
    data = (data*9/5)+32
    print("El valor en °F es:", data)
except ValueError:
    print("Error de dato")
    
    
    

data = input("Inserte un numero entero para calcular si es cuadrado:")
try:
    data = int(data)
    if math.sqrt(data)**2 == data:
        print("Es cuadrado")
    else:
        print("No es cuadrado",)
except ValueError:
    print("Error de dato")
    
    
    
    
data = input("Inserte dato en radianes para calcular sinc:")
try:
    data = float(data)
    if data != 0:
       data = math.sin(math.pi*data) / (math.pi*data)
       print("Sinc es:",data)
    else:
        data = 1
        print ("Sinc es:",data)
except ValueError:
    print("Error de dato")
    
    
    

money = input("Inserte cantidad de dinero:")
try:
    money = int(money)
    if money >= 100:
       hundreds = money // 100
       money = money % 100
       print("Monedas de 100:", hundreds)
    if money >= 25:
       twentyfive = money // 25
       money = money % 25
       print("Monedas de 25:", twentyfive)
    if money >= 5:
       fives = money // 5
       money = money % 5
       print("Monedas de 5:", fives)
    if money >= 1:
       ones = money // 1
       print("Monedas de 1:", ones)
except ValueError:
    print("Error de dato")