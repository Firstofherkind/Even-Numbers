# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:33:31 2021

@author: JENI
"""


def even_numbers(X):
    even = []
    for i in range (X):
        if i % 2 == 0:
              even.append(i)
    return even
    
    
print(even_numbers(10))
            