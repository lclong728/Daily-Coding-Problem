# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 00:25:32 2018

@author: lenovo
"""

"""
DailyCodingProblem #6
22/07/2018
Asked by: Google

An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. 
Implement an XOR linked list; 
it has an add(element) which adds the element to the end, 
and a get(index) which returns the node at index.

reference to: https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_06_10.py
"""


'''
## XOR Linked List Object
## Since there are no pointer in Python, List index is used to preform the address fo Linked List
the Node is same as: 
NodeObject = {
        val = data
        both = *npr // a pointer which contain  prev ^ next
}
'''

class Node(object):
    
    def __init__(self, val, prev_address, next_address):
        self.val = val
        self.both = prev_address ^ next_address
    
    def next_node(self, prev_address):
        return self.both ^ prev_address
    
    def prev_node(self, next_address):
        return self.both ^ next_address
        

class XORLinkedList(object):
    
    def __init__(self):
        self.memory = [Node(None, -1, -1)] ## init the Node when nothing in the Linked List

        
    def add(self, val):
        current_node_idx = 0
        prev_node_idx = -1
        current_node = self.memory[0]
        
        while True:
            next_node_index = current_node.next_node(prev_node_idx)
            if next_node_index == -1:  # reach the end on the list
                break
            prev_node_idx, current_node_idx = current_node_idx, next_node_index
            current_node = self.memory[next_node_index]
            
        new_node_idx = len(self.memory)
        current_node.both = prev_node_idx ^ new_node_idx
        self.memory.append(Node(val, current_node_idx, -1))
        
        
    def get(self, index):
        current_idx = 0
        previous_idx = -1
        current_node = self.memory[0] 
        for cnt in range(index + 1):
            previous_idx, current_idx = current_idx, current_node.next_node(previous_idx)
            current_node = self.memory[current_idx]
        return current_node.val
        
                  
a = Node(1, -1, 1)
print(a.both)

b = XORLinkedList()
for i in [1, 2,3,4,5,6,7,8]:
    b.add(i)
    
print(b.get(3))
print(b.memory)


