# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:50:31 2018

@author: lenovo
"""

"""
DailyCodingProblem #19
05/08/2018
Asked by: Facebook

A builder is looking to build a row of N houses that can be of K different colors. 
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, 
return the minimum cost which achieves this goal.
"""

def cost_optimizer(cost_matrix):
    col = len(cost_matrix[0]) #how many corlor in the matrix is the cols num in the matrix
    
    cost_stack = [0] * col # init a list for cost calculating 
    for house in cost_matrix: #each house
        temp_cost = [0] * col
        for i in range(col):
            temp_cost[i] = house[i] + min(cost_stack[:i] + cost_stack[i+1:])# painting the color using the ith color
        cost_stack = temp_cost
    
    return min(cost_stack)

cost = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
print(cost_optimizer(cost))