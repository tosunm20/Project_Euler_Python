# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:54:42 2023

@author: 90545
"""

def abNumFinder(number):
    tam_bolen_toplam = 0
    for i in range(1,number):
        if (number%i==0) :
            tam_bolen_toplam += i
    
    if tam_bolen_toplam>number: return True
    else: return False
    

abund = list()
sumAbund = list()
mySum = 0

for i in range(1,28124):
    if abNumFinder(i): abund.append(i)

sumAbund = [0]*28124
for i in range(len(abund)):
    for j in range(i, len(abund)):
        if abund[i]+abund[j]<=28123:
            sumAbund[abund[i]+abund[j]]=abund[i]+abund[j]

for i in range(len(sumAbund)):
    if sumAbund[i]==0:
        mySum+=i