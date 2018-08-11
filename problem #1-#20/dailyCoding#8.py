# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 01:57:43 2018

@author: lenovo
"""

"""
DailyCodingProblem #8
24/07/2018
Asked by: Google

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class tree(object):
    
    def __init__(self, root, left = None, right = None):
        self.val = root
        self.left = left ## default None
        self.right = right ## defult None
        


def is_unival(root, root_value):
    if root is None:
        return True 
    if root.val == root_value:
        return is_unival(root.left, root_value) and is_unival(root.right, root_value)
    return False

def unival_counter(root):
    if root is None:
        return 0
    if is_unival(root, root.val):
        return 1 + unival_counter(root.left) + unival_counter(root.right)
    else:
        return unival_counter(root.left) + unival_counter(root.right)
    
tree = tree('1', tree('1', tree('1'),tree('2')),tree('1', tree('1'), tree('1')))
print(unival_counter(tree))
    
    