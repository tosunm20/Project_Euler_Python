# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:31:51 2023

@author: 90545
"""

from num2words import num2words

def myfunc(number):
    number_in_words = num2words(number)
    number_in_words = (list(number_in_words))
    if '-' in number_in_words:
        number_in_words.replace("-","")
    if ' ' in number_in_words:
        number_in_words.remove(" ", "")
    
    return number_in_words
        

total = 0
for i in range(1, 1001
               ):
    numLength =len(myfunc(i))
    total += numLength

print(total)