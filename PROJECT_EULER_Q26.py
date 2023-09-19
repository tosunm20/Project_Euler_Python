# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:56:06 2023

@author: 90545
"""

devir=0
bolen = 2


while bolen<1000:
    
    bolunen = 1
    kalanlar = []
    while True:
        kalan = bolunen % bolen
        if kalan in kalanlar:
            first_kalan_index = kalanlar.index(kalan)
            last_kalan_index = len(kalanlar)
            if (last_kalan_index-first_kalan_index)>devir:
                devir=last_kalan_index-first_kalan_index
                num = bolen
            break
        bolunen = kalan * 10
        kalanlar.append(kalan)
            
    bolen+=1

print(num)