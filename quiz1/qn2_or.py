#!/usr/bin/env python
'''Suppose there are n stairs. You are standing at the bottom (0th stair) and want to reach
the top. If you are at ith stair, you can climb either 1 stair or jump i stairs at a time.
How many ways you can reach the top?
(a) Write the recursive formulation to count the number of ways to reach the top.
(b) Write a program to count the number in O(n) time.
'''
#  Recursive formula:
#  f(n) = f(n-1) + f(n/2)   if n is even
#  f(n) = f(n-1)            if n is odd

def count_ways(n):
    counts = [None, 1, 1]  # Base cases for steps 0, 1 and 2.
    counts.extend([0]*n)
    def _count_ways(n):
        if counts[n] != 0:
            return counts[n]
        if n%2 == 0:
            counts[n] = _count_ways(n-1) + _count_ways(n//2)
            return counts[n]
        else:
            counts[n] = _count_ways(n-1)
            return counts[n]
    return _count_ways(n)


if __name__ == "__main__":
    step = 4
    print(count_ways(step))
