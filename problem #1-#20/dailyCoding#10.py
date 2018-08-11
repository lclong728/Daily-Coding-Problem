# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 19:55:12 2018

@author: lenovo
"""

"""
DailyCodingProblem #10
26/07/2018
Asked by: Apple

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds

"""
import time

def delay_function(function, sleep_time):
    print('delay function start!')
    time.sleep(sleep_time)
    return function


def function():
    return 'after delay'

print(delay_function(function(), 10))