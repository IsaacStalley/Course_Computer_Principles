# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:26:04 2019

@author: Isaac Stalley
"""
def crear_matriz(a,b,c):
    matrix = []
    temp = []
    for i in range(b):
        temp.append(c)
    for j in range(a):
        matrix.append(temp)
    return matrix

def matriz_identidad(n):
    matrix = []
    for i in range(n):
        counter = 1
        temp = []
        while counter < n:
            temp.append(0)
            counter += 1 
        temp.insert(i,1)
        matrix.append(temp)
    return matrix

def suma_matrices(a,b):
    new = []
    try:
        for i in range(len(a)):
            temp = []
            for j in range(len(a[i])):
                temp.append(a[i][j]+b[i][j])
            new.append(temp)
        return new
    except IndexError:
        return []

def product_matrices(a,b):
    new = []
    try:
        counter = 0
        while counter < len(a):
            temp = []
            for i in range(len(a)):
                vtemp = 0
                for j in range(len(a[i])):
                    vtemp += a[counter][j]*b[j][i]
                temp.append(vtemp)
            counter +=1
            new.append(temp)
        return new
    except IndexError:
        return []    

def submatriz(M,f,c):
    try:
        for i in range(len(M)):
            del M[i][c]
        del M[f]
        return M
    except IndexError:
        return []