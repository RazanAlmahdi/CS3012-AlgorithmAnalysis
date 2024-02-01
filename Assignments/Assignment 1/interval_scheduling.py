#!/usr/bin/env python
# coding: utf-8

# In[4]:


def interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])  # sort intervals by their end time
    count = 0  # number of non-overlapping intervals
    end_time = -float('inf')
    for interval in intervals:
        if interval[0] >= end_time:
            count += 1
            end_time = interval[1]
    return count

with open('interval_scheduling.txt') as f:
    intervals = [tuple(map(int, line.strip().split(','))) for line in f]
print(interval_scheduling(intervals))

