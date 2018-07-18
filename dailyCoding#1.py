# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 23:09:12 2018

@author: lenovo
"""

'''
Daily Coding Problem #1
17/07/2018

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

## dynamic programming

def isExist(targetList, targetNum):
    partnerList = []
    targetNum = int(targetNum)
    for num in targetList:
        partner = targetNum - num
        if num in partnerList:
            return True
        else:
            partnerList.append(partner)
    return False

print(isExist([10, 12, 3, 5], 8))