# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 23:22:39 2018

@author: lenovo
"""

"""
DailyCodingProblem #13
30/07/2018
Asked by: Amazon

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def distinct_counter(s, k): #string s and int k
    
    if k > len(s):
        return 0
    else:
        start_idx, end_idx, max_len = 0, k, k
        while end_idx < len(s):
            end_idx += 1
            while True:
                distinct_char = len(set(s[start_idx:end_idx]))
                if distinct_char <= k:
                    break
                start_idx += 1
            max_len = max(max_len, end_idx - start_idx) 
        return max_len
        
    
print(distinct_counter('abccba', 2))    