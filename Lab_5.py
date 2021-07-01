# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:26:04 2019

@author: Isaac Stalley
"""

import math
data = 0
while data <= 0:
    try:
        data = int(input("Inserte numero entero positivo:"))
    except ValueError:
        data = 0
    
    
    
    
s = 0
i = 0
while s < 1:
    print("Inserte M para para conversiones de masa (kg <-> libras)")
    print("Inserte T para para conversiones de masa (°C <-> °F)")
    print("Inserte L para para conversiones de masa (km <-> mi)")
    selection = input(":")
    if selection == "M" or selection == "m":
        s += 1
        while i < 1:
            try:
                data = float(input("Inserte cantidad:"))
                i += 1
                lib = data*2.205
                kg = data / 2.205
                print (data,"kg -> ",lib,"libras")
                print (data,"libras -> ",kg,"kg")
            except ValueError:  
                i = 0
    if selection == "T" or selection == "t":
        s += 1
        while i < 1:
            try:
                data = float(input("Inserte cantidad:"))
                i += 1
                f = (data * 9/5) + 32
                c = (data - 32) * 5/9 
                print (data,"°C -> ",f,"°F")
                print (data,"°F -> ",c,"°C")
            except ValueError:  
                i = 0
    if selection == "L" or selection == "l":
        s += 1
        while i < 1:
            try:
                data = float(input("Inserte cantidad:"))
                i += 1
                km = data * 1.609
                mi = data / 1.609
                print (data,"km -> ",mi,"mi")
                print (data,"mi -> ",km,"km")
            except ValueError:  
                i = 0
                
                
                
                
i = 0
s = 0
rc = 0
rs = 0
while i == 0:
    try:
        data = float(input("Inserte cantidad en radianes:"))
        i += 1
        while s <= 10:
            cos = (-1)**s * data**(2*s) / math.factorial(2*s) * data**(2*s)
            sen = (-1)**s * data**(2*s + 1) / math.factorial(2*s + 1)
            rc += cos
            rs += sen
            s += 1
        print ("Sen(",data,") es:",rs)
        print ("Cos(",data,") es:",rc)
    except ValueError:
        i = 0