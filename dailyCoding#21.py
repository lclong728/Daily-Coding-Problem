# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 23:58:55 2018

@author: lenovo
"""

"""
DailyCodingProblem #21
07/08/2018
Asked by: SnapChat

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

def room_required(array):
    rooms = 0
    room_occupied = 0
    if array != None and type(array) == list:
        sort_time_lst = sorted([(i, j) for i, j in array])
        start_time = [i for i,j in sort_time_lst]
        end_time = [j for i,j in sort_time_lst]
        
        i = j = 0
        while i < len(sort_time_lst) and j < len(sort_time_lst):
            if start_time[i] < end_time[j]:
                room_occupied += 1
                rooms = max(room_occupied, rooms)
                i += 1
            else:
                room_occupied -= 1
                j += 1
            
    return rooms

print(room_required([(30, 75), (0, 50), (60, 150)]))
print(room_required([(90,91), (94, 120), (95, 112), (110, 113), (150, 190), (180, 200)]))
                
    
        