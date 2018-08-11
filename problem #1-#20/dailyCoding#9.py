# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 23:02:57 2018

@author: lenovo
"""

"""
DailyCodingProblem #9
25/07/2018
Asked by: Airbnb

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
Numbers can be 0 or negative.

For example, 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.
"""

def maximum_sum(given_array):
    return helper(given_array, 0, 0) ## init helper function 
    
def helper(array, idx, max_sum):
    position_para= 2
    if idx + 2 < len(array):
        while idx + position_para < len(array):
            if array[idx] + array[idx + position_para] > max_sum:
                max_sum = array[idx] + array[idx + position_para]
            position_para += 1 
        return helper(array, idx + 1, max_sum)
    else:
        return max_sum
        
print(maximum_sum([-1, 3, 4, -1, -3]))