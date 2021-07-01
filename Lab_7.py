# -*- coding: utf-8 -*-
"""
Created on Tue Oct 8 11:07:24 2019

@author: Isaac Stalley
"""

def fibo_function(n):
    if n > 1:
        fibo = 0
        while n > 1:
           fibo += fibo_function(n-1) + fibo_function(n-2)
           return fibo
    elif n == 0:
        return n
    elif n == 1 or n == -1:
        return 1
    else:
        fibo = 0
        n = abs(n)
        while n > 1:
            fibo += fibo_function(n-1) + fibo_function(n-2)
            if n % 2 == 0:
                return -1*fibo
            else:
                return fibo



def gcd_function(a,b):
    if b == 0:
        return a
    else:
        return gcd_function(b, a % b)



def string_function(s):
    length = len(s)
    new = ''
    i = 0
    c = 1
    while i < length:
        new += s[-c]
        i += 1
        c += 1
    return new



def guess_function(a):
    l = 0
    lis = []
    while l <= a:
        lis.append(l)
        l += 1
    r = 0
    mid = l // 2
    while r == 0:
        print("Su numero es?:",mid)
        i = 0
        while i == 0:
            ask = input("Inserte si el numero es <,>,=:")
            if ask == '<' or ask == '>' or ask == '=':
                i += 1
        if ask == '<':
            count = mid
            if (mid-1) in lis:
                while count <= lis[-1]:
                    lis.remove(count)
                    count += 1
                mid = lis[len(lis) // 2]
            else:
                print("Tramposo")
                return False
        if ask == '>':
            count = mid
            if (mid+1) in lis:
                while count >= lis[0]:
                    lis.remove(count)
                    count -=1
                mid = lis[len(lis) // 2]
            else:
                print("Tramposo")
                return False
        if ask == '=':
            r += 1
            return mid
        



i = 0
while i == 0:
    try:
        data = int(input("Inserte dato:"))
        i += 1
    except ValueError:
        print("Error de dato")
result = fibo_function(data)
print ("Numero Fibonacci es:", result)



i = 0
while i  == 0:
    try:
        a = int(input("Inserte primer dato para gcd:"))
        i +=1
    except ValueError:
        print("Error de dato")



s = 0
while s == 0:
    try:
        b = int(input("Inserte segundo dato para gcd:"))
        s += 1
    except ValueError:
        print("Error de dato")
print("El gcd es:",gcd_function(a,b))



data = input("Inserte hilera:")
print("Su hilera en orden inverso es:",string_function(data))



data = 100
result = guess_function(data)
if result != False:
    print("Su numero es:", result)

