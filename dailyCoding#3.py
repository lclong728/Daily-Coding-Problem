# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 18:17:32 2018

@author: lenovo
"""

"""
DailyCodingProblem #3
19/07/2018
Asked by: Google

Given the root to a binary tree, 
implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.
"""

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def deserialize(string):
    component = iter(string.split(','))
    val = next(component)
    
    def MergeComponentHelper(val):
        if val != 'None':
            node = Node(val)
            node.left = MergeComponentHelper(next(component))
            node.right = MergeComponentHelper(next(component))
            return node
        else: 
            return None

    return MergeComponentHelper(val)
    


def serialize(node):
    component_lst = []
    SeperateComponentHelper(node, component_lst)
    return ','.join(component_lst)

def SeperateComponentHelper(node, lst):
    if node is not None:
        lst.append(str(node.val))
        if node.val is not None:
            SeperateComponentHelper(node.left, lst)
            SeperateComponentHelper(node.right, lst)
    else:
        lst.append('None')
 

def test():    
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serial = serialize(node)
    deserial = deserialize(serial)
    print(serial)
    if deserial.__class__ == Node:
        print('pass')
        print(deserial.right.val)
    else:
        print('fail')
    
    
test()

    
    
    