# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:34:41 2021

@author: Comp
"""

W= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print (most_frequent(W))