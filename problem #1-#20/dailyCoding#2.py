# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:27:41 2018

@author: lenovo
"""

"""
DailyCodingProblem #2
18/07/2018
Asked by: Uber

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

solution ver1: linear sortings
"""

class ProductArray(object):
    
    def __init__(self, GivenArray):
        self.array = GivenArray
        self.length = len(GivenArray)
        
    def BeforeList(self):
        beforeList = [1]*self.length
        for i in range(self.length):
            num = 0
            while num < i:
                beforeList[i] *= self.array[num]
                num += 1
        return beforeList
    
    def AfterList(self):
        afterList = [1]*self.length
        for i in range(self.length):
            num = self.length - 1
            while num > i:
                afterList[i] *= self.array[num]
                num -= 1
        return afterList
           
    ## ANS
    def Result(self):
        result = [self.BeforeList()[i] * self.AfterList()[i] for i in range(self.length)]
        return result
        
    
a = ProductArray([9,9,9])
print(a.Result())