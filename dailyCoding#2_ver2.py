# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 18:40:10 2018

@author: lenovo
"""
"""
DailyCodingProblem #2
18/07/2018
Asked by: Uber

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Solution ver2: binary sortings
"""

def ProductArray(GivenArray):
    
    ## init before and after list
    Before = [1] * len(GivenArray)
    After = [1] * len(GivenArray)
    
    for i in range(len(GivenArray)):
        if i == 0: 
            Before[i] = 1
        else:
            Before[i] = Before[i-1] * GivenArray[i-1]
        After[-i-1] = After[-i] * GivenArray[-i]
    return [x * y for x, y in zip(Before, After)]

print(ProductArray([1,2,3,4,5]))
