# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 23:31:37 2018

@author: lenovo
"""

"""
DailyCodingProblem #20
06/08/2018
Asked by: Google

Given two singly linked lists that intersect at some point, find the intersecting node. 
The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.
"""

class linked_list(object):
    
    def __init__(self, value = None, next_node = None):
        self.val = value
        self.next = next_node
        
    def add_node(self, new_node = None):
        self.next = new_node
        return new_node
    
    def next_ptr(self):
        return self.next
    
    
def find_intersact(A, B):
    if A != None and B != None:
        while A.val != B.val:
            A = B if A.next == None else A.next
            B = A if B.next == None else B.next
        return A

A = linked_list(3)
A.add_node(linked_list(7)).add_node(linked_list(28)).add_node(linked_list(120))

B = linked_list(99)
B.add_node(linked_list(1)).add_node(linked_list(8)).add_node(linked_list(10))


print(find_intersact(A, B).val)
       

            
