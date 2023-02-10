#!/usr/bin/env python
'''Given a list of size n consisting of consecutive 1s followed by consecutive 2s, find the
position of transition from 1 to 2 in O(log n) time.
For example, if the list is [1, 1, 1, 2, 2, 2, 2], the index is 3 where the transition occurs.
'''

def find_transition(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left)//2

        if arr[mid] == 2:
            if arr[mid-1] == 1:
                return mid
            else:
                right = mid-1
        else:
            if arr[mid+1] == 2:
                return mid+1
            else:
                left = mid+1
    else:
        return -1 #  Not found.

if __name__ == "__main__":
    from random import randint
    for _ in range(10**3):
        ONES = [1]*randint(1,20)
        TWOS = [2]*randint(1,20)
        INPUT = ONES + TWOS
        transition_point = find_transition(INPUT)
        assert transition_point == INPUT.index(2)
