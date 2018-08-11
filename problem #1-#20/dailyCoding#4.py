# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:52:40 2018

@author: lenovo
"""

"""
DailyCodingProblem #4
20/07/2018
Asked by: Stripe

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""

import numpy as np

def MissingInt(arr):
    arr.sort()
    arr = np.array(arr)
    arr = arr[arr > 0] # make it constant space
    if len(arr) == 0:
        return None
    elif arr[0] == 1:
        min_int = 1
        for i in range(len(arr)):
            if arr[i] == min_int:
                min_int+=1
            else:
                return min_int
    else:
        return 1
    
    
            
print(MissingInt([1,2, 2, 9, 9, 9]))