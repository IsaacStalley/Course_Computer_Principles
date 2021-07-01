# -*- coding: utf-8 -*-
"""
Created on Thur Nov 14 11:26:04 2019

@author: Isaac Stalley
"""
def numeros_primos(n):
    f = open("numeros_primos.txt","w+")
    counter = 0
    num = 2
    while counter < n:
        for i in range(2,num):
            if (num % i == 0):
                break
        else:
            f.write(str(num) + '\n')
            counter += 1
        num += 1
    f.close()

path = 'C:/users/public/iris.data'
f = open(path,'r')
matrix = []
for i in f:
    temp = i.split(',')
    if len(temp) == 5:
        temp[4] = temp[4][: -1]
        for j in range(len(temp)-1):
            temp[j] = float(temp[j])
        matrix.append(temp)
f.close()

print(matrix)
