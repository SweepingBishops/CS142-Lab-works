#!/usr/bin/env python
'''Suppose you have a function F such that given two lists L1 and L2, f(L1, L2) returns the
difference of the sum of the elements of L1 and L2. Now given a list of size n that consists
of n − 1 many 1s and a single 2, find the position of 2 making at most 2 log n many calls
to the function F.
For example, if the list is [1, 1, 1, 2, 1, 1], the index is 3 where 2 occurs.
'''


def find_diff(arr1, arr2):
    global function_call_counter
    function_call_counter += 1

    diff = 0
    for x in arr1: diff += x
    for y in arr2: diff -= y
    return diff

def find_2(arr):
    left = 0
    right = len(INPUT) - 1
    while left < right:
        if (right-left) % 2 == 1:
            if INPUT[right] != 2:
                right -= 1
            else:
                break
        mid = (left + right)//2
        if arr[mid] == 2:
            return mid
        elif find_diff(INPUT[left:mid], INPUT[mid:right]) > 0:
            right = mid
        else:
            left = mid

    return right

if __name__ == "__main__":
    from random import randint
    from math import log
    for i in range(10**5):
        function_call_counter = 0
        index2 = randint(0,100)
        INPUT = [1 for i in range(100)]
        INPUT.insert(index2, 2)

        index = find_2(INPUT)
        assert index == INPUT.index(2)
        assert function_call_counter <= log(len(INPUT), 2)
