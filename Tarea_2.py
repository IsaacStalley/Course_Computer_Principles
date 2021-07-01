# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:15:15 2019

@author: Isaac Stalley
"""
import random
def word_function():
    i = 0
    while i == 0:
        try:
            amount = int(input("Inserte cantidad de palabras:"))
            i += 1
        except ValueError:
            print("Inserte un numero")
    i = 0
    words = []
    while i < amount:
        print("Inserte palabra",i+1)
        words.append(input(":"))
        i += 1
    return words

def compare_function(a,b):
    i = 0
    compare = []
    while i < len(a):
        if a[i] == b:
            compare.append(i)
        i += 1
    return compare

def count_function(a,b):
    i = 0
    count = 0
    while i < len(a):
        if a[i] == b:
            count += 1
        i += 1
    return count

def unique_function(a):
    i = 0
    unique = []
    while i < len(a):
        count = 0
        holder = a[i]
        s = 0
        while count < len(a):
            if holder == a[count]:
                s += 1
            count += 1
        if s == 1:
            unique.append(holder)
        i += 1
    return unique

def elim_function(a):
    i = 0
    while i < len(a):
        count = 0
        holder = a[i]
        s = 0
        while count < len(a):
            if holder == a[count]:
                s += 1
            count += 1
        if s > 1:
            a.remove(holder)
        else:
            i += 1
    return a

def largest_function(a):
    i = 0
    largest = 0
    while i < len(a):
        count = 0
        holder = a[i]
        s = 0
        while count < len(a):
            if holder == a[count]:
                s += 1
            count += 1
        if s > largest:
            largest = s
            result = holder
        else:
            i += 1
    return result

def acum_function(a):
    i = 1
    total = a[0]
    acum = [total]
    while i < len(a):
        total += a[i]
        acum.append(total)
        i += 1
    return acum

def comparacion_function(a,b):
    i = 0
    results = []
    while i < len(a) and i < len(b):
        if a[i] > b[i]:
            results.append(True)
        else:
            results.append(False)
        i += 1
    return results

def pascal_function(a,b):
    if a == 0:
        return b
    if b == 0:
        return 1
    else:
        return (a*pascal_function(a-1,b-1)) / b

def pascal_print(n):
    i = 1
    result = [1]
    while i < n:
        result.append(pascal_function(n,i))
        i += 1
    result.append(1)
    print(result)

def palindromo_function(a):
    i = 0
    while i < len(a):
        if a[i] == a[-(i+1)]:
            i += 1
        else:
            return False
    return True

def dice_function():
    return random.randint(1,20)

i = 0
result = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while i < 20000:
    throw = dice_function()
    result[throw-1] = result[throw-1] + 1
    i += 1
c = 0
while c < 20:
    print("Cantidad de veces que salio cara",c+1,":",result[c])
    c += 1