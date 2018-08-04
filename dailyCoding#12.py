# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 23:08:16 2018

@author: lenovo
"""

"""
DailyCodingProblem #12
28/07/2018
Asked by: Amazon

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
- 1, 1, 1, 1
- 2, 1, 1
- 1, 2, 1
- 1, 1, 2
- 2, 2
"""

def step_counter(N): ## only climb 1 or 2 steps
    if N == 0 or N == 1:
        return 1
    elif N < 0:
        return 0
    else:
        return step_counter(N-1) + step_counter(N-2)
print("ans for solution 1 @only climb 1 or 2 steps:")
print(step_counter(8))
print("--------------------")

def step_counter_2(N,step_list):
    memo = dict()
    return counter2_helper(N, step_list, memo)

def counter2_helper(N, step_list, memory): 
    if N == 0 or N == 1:
        return 1
    else:
        if N in memory:
            return memory[N]
        else:
            result = 0
            for step in step_list:
                if N >= step:
                    result += counter2_helper(N-step, step_list, memory)
                    memory[N] = result
            return result
    
print("ans for solution 2 @climb any step in step_list:")
print(step_counter_2(8, [1,3,5])) 