# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 00:16:21 2018

@author: lenovo
"""

"""
DailyCodingProblem #5
21/07/2018
Asked by: Jane Street

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
"""

def cons(a, b):
    return lambda f: f(a, b)

def car(f):
    return f(lambda a, b: a)

def cdr(f):
    return f(lambda a, b: b)

print(cdr(cons(1, 2)))

