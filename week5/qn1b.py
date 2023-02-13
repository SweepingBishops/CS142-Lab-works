#!/usr/bin/env python
'''(b) Given a set of positive and negative integers, and a value t, and an integer k determine
if there is a subset of size exactly k, such that the sum of the elements in the set is equal to t.
Write a program that uses the function in Problem 1 as a subroutine.
'''
import qn1a

def is_subset_sum(arr, target, length):
    arr.sort()
    arr_min = min(arr)
    mutl_factor = 0
    if arr_min < 0:
        for index, value in enumerate(arr):
            arr[index] -= arr_min
        mutl_factor -= arr_min
    return qn1a.is_subset_sum(arr, target + length*mutl_factor, length)

if __name__ == "__main__":
    arr = [-1, -2, -5, 8, 9, 10]
    target = 8
    length = 2
    print(is_subset_sum(arr, target, length))
