# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 12:51:55 2023

@author: 90545
"""

import sympy

counter=0
for a in range(-999,1000):
    for b in sympy.primerange(1,1000):
        temp=0
        n=0
        while sympy.isprime(n**2 + a*n + b):
            temp +=1 
            n += 1
        if temp > counter:
            counter = temp
            maxa = a
            maxb = b
print(maxa*maxb)
print(counter)