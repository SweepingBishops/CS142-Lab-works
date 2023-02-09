#!/usr/bin/env python
'''
Given two sorted lists, find the element in the kth position
of the merged and sorted list.
'''

arr1 = [1,4,6,19,25]
arr2 = [7,9,10]
K = 4


def find_k(arr1, arr2, k):
    if k == 1:
        return min(arr1[0], arr2[0])
    if len(arr1) == 1:
        return arr1[0]
    elif len(arr2) == 1:
        return arr2[0]

    if len(arr1) > k:
        arr1 = arr1[:k+1]
    if len(arr2) > k:
        arr2 = arr2[:k+1]
    arr1_check = len(arr1)//2
    arr2_check = len(arr2)//2

    if arr1[arr1_check] < arr2[arr2_check]:
        return find_k(arr1[arr1_check+1:], arr2, k - arr1_check)
    elif arr1[arr1_check] > arr2[arr2_check]:
        return find_k(arr1, arr2[arr2_check+1:], k - arr2_check)
    else:
        return arr1[arr1_check]

print(find_k(arr1, arr2, K))
