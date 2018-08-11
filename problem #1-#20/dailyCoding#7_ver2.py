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

def num_ways(data):
    symbols = map(str, range(1, 27))
    if not data:
        return 1

    matches = filter(lambda symbol: data.startswith(symbol), symbols)
    encodings = [num_ways(data[len(m):]) for m in matches]
    return sum(encodings)
    
print(num_ways("123"))