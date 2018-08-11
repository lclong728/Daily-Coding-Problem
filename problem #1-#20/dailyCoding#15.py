# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 16:53:09 2018

@author: lenovo
"""

"""
DailyCodingProblem #15
01/08/2018
Asked by: Facebook

Given a stream of elements too large to store in memory, 
pick a random element from the stream with uniform probability.
"""

"""
Note:
    
Let the current element's index be i.

Choose to 'remember' the current element at probability 1/i. 
When EOF is reached, produced the element you remember.

At the end, for each element with index i there is a probability to be chosen: 1/n
because: 
    1/i * (1-1/(i+1)) * (1-1/(i+2)) * (1-1/(i+3)) * ... * (1-1/(n))
= 1/i * i/(i+1) * (i+1)/(i+2) + ... * n-1/n
= 1/n 

reference: https://stackoverflow.com/questions/23351918/select-an-element-from-a-stream-with-uniform-distributed-probability
"""

import random

def sample_generator(sample_size):
    for sample in range(sample_size):
        yield sample
        
def element_picker(sample_generator):
    sample_counter = 0
    selected_sample = None
    
    for sample in sample_generator:
        sample_counter += 1
        if random.random() <= 1/sample_counter: 
        ## random.random() is base on uniform distrivution 
            selected_sample = sample
    return selected_sample
    
print(element_picker(sample_generator(10000)))






    