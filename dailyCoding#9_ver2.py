# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 19:57:25 2018

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
[1,2,3,4,5,6,7,8] should return 20, since we pick 2,4,6 and 8
"""

def maximum_sum(array):
    init_max_idx, init_max_num = find_list_max(array)
    return router(array, init_max_idx, init_max_num)
    
def router(array, idx, max_sum):
    if idx-2 < 0:
        if idx + 2 < len(array):
            return max_sum + after_max_sum(array[idx+2:], 0)
        else:
             return max_sum
    else:
        if idx + 3 > len(array):
            return max_sum + before_max_sum(array[0:idx-1], 0)
        else:
            return max_sum + before_max_sum(array[0:idx-1], 0) + after_max_sum(array[idx+2:], 0)
    
def find_list_max(array):
    return max([i for i, j in enumerate(array) if j == max(array)]), max(array) ## return tuple
        
def before_max_sum(before_array, before_max_sum):
    
    if len(before_array) == 1:
        return before_max_sum + before_array[0]
    elif len(before_array) == 0:
        return before_max_sum
    else:
        before_max_idx, before_max = find_list_max(before_array)
        before_max_sum += before_max
        return router(before_array, before_max_idx, before_max_sum)

def after_max_sum(after_array, after_max_sum):
    
    if len(after_array) == 1:
        return after_max_sum + after_array[0]
    elif len(after_array) == 0:
        return after_max_sum
    else:
        after_max_idx, after_max = find_list_max(after_array)
        after_max_sum += after_max
        return router(after_array, after_max_idx, after_max_sum)
    
        
print(maximum_sum([1,2,3,4,2,2,2,4]))