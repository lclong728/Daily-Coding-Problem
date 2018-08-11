# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 17:26:19 2018

@author: lenovo
"""

"""
DailyCodingProblem #16
02/08/2018
Asked by: Twitter
You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

- record(order_id): adds the order_id to the log
- get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

class log(object):
    
    def __init__(self, N):
        self.length = N
        self.order_list = [None] * N
        self.order_counter = 0
        
    def record(self, order_id):
        if self.order_counter == self.length:
            self.order_list.pop(0)
            self.order_list.append(order_id)
        else:
            self.order_list[self.order_counter] = order_id
            self.order_counter += 1
    
    def get_last(self, i):
        start_idx = self.length - i
        
        if i > self.length:
            return 0
        elif self.order_list[start_idx:] == [None] * i:
            return "there are not that much record"
        else:
            return self.order_list[start_idx:]
        
a = log(3)
a.record("001")
a.record("002")
a.record("003")
print(a.get_last(3))

a.record("004")
print(a.get_last(3))
        
        
        