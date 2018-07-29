# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:59:58 2018

@author: lenovo
"""

"""
DailyCodingProblem #11
27/07/2018
Asked by: Twitter

Implement an autocomplete system. 
That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal]
"""
import re
 
def string_querier(string, target_arr):
    pattern = '^'+ string
    return [i for i in target_arr if re.search(pattern , i)]
    
print(string_querier('de', ['deer', 'deal', 'dog']))