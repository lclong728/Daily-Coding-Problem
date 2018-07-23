## Problem Description:

#### Problem 1:
##### Asked by: Google
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

Example: 
given [10, 15, 3, 7] and k of 17
return true since 10 + 7 is 17

#### Problem 2:
##### Asked by: Uber
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

Example:
Input Array =  [1, 2, 3, 4, 5] 
The expected output should be [120, 60, 40, 30, 24] 
Input Array = [3, 2, 1]
The expected Iutput would be [2, 3, 6]

#### Problem 3:
##### Asked by: Google
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

Example:
given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

#### Problem 4:
##### Asked by: Stripe
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

Example:
Input = [3, 4, -1, 1] 
The ans should give 2
Input = [1, 2, 0] 
The ans should give 3

#### Problem 5:
##### Asked by: Jane Street
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.

Example: 
car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pairs
Implement car and cdr.

#### Problem 6:
##### Asked by: Google
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

#### Problem 6:
##### Asked by: Facebook
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.

Example:
The message '111' would return 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.