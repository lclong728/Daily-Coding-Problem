# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 01:33:18 2018

@author: lenovo
"""

"""
DailyCodingProblem #14
31/07/2018
Asked by: Google

The area of a circle is defined as πr^2. 
Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import random


def pi_estimator():
    success_cnt = 0
    total = 0 
    prev_pi = 0
    est_pi = 3
    
    while True:
        coordin_lst = []
        for i in range(1000000):
            coordin_lst.append((random.random(), random.random()))
            if coordin_lst[i][0]**2 + coordin_lst[i][1]**2 <= 1:
                success_cnt +=1
            total +=1
        prev_pi = est_pi
        est_pi = 4 * float(success_cnt/total)
        print('prev_pi = {}, est_pi = {}'.format(prev_pi, est_pi))
        if abs(prev_pi - est_pi) < 1e-5:
            return float('{0:.3f}'.format(est_pi))

print(pi_estimator())

