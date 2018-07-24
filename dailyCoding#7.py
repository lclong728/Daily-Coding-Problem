# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 21:48:31 2018

@author: lenovo
"""

"""
DailyCodingProblem #7 
23/07/2018
Asked by: Facebook

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""



def counting(data, length, control_lst):
    if length <= 1:
        if int(data) != 0: 
            return 1
        else:
            return 0
    elif int(data[0]) == 0:
        return 0
    elif control_lst[length] != None:
        return control_lst[length]
    else:
        result = counting(data, length-1, control_lst)
        if int(data[0:1]) <= 26:
            result += counting(data, length -2, control_lst)
        return result
    
def num_ways(data):
    control_lst = [None]*(len(data)+1) ## initing a list with all null to control the repeatants
    return counting (data, len(data), control_lst)
        
print(num_ways("123212"))
    