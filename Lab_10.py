# -*- coding: utf-8 -*-
"""
Created on Tue Nov 6 11:26:04 2019

@author: Isaac Stalley
"""
def stringcount_function(a,b):
    words = a.split()
    count = 0
    for i in range(len(words)):
        if b in words[i]:
            count += 1
    return count

def stringlist_function(a):
    letters = []
    counter = []
    for i in range(len(a)):
        if a[i] not in letters:
            letters.append(a[i])
            counter.append(1)
        else:
            temp = letters.index(a[i])
            counter.insert(temp, counter[temp]+1)
    return letters, counter

def stringuppercase_function(a):
    holder = a.split()
    print(holder)
    new = ''
    for i in range(len(holder)):
        new += holder[i].capitalize()
        if i+1 < len(holder):
            new += ' '
    return new

def cifrar(a,b):
    new = ''
    for i in range(len(a)):
        temp = ord(a[i]) + b
        new += chr(temp)
    return new
