# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 18:31:41 2018

@author: lenovo
"""

"""
DailyCodingProblem #18
04/08/2018
Asked by: Google

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
"""

def sub_arr_max(array, k):
    max_lst = []
    start_idx, end_idx = 0, k
    
    while end_idx <= len(array):
        max_lst.append(max(array[start_idx: end_idx]))
        start_idx += 1
        end_idx += 1
    
    return max_lst

print(sub_arr_max([10, 5, 2, 7, 8, 7], 3))
    