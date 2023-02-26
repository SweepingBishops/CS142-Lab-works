#!/usr/bin/env python
def find_diff(arr1, arr2):
    diff = 0
    for x in arr1: diff += x
    for y in arr2: diff -= y
    return diff


def find_2(arr):
    def slice(left, right):
        mid1 = left + (right - left)//3 + 1
        mid2 = mid1 + (right - left)//3 + 1

        if left == right:
            return left

        diff = find_diff(arr[left:mid1], arr[mid2:right+1])
        if diff > 0:
            return slice(left, mid1-1)
        elif diff < 0:
            return slice(mid2, right)
        else:
            return slice(mid1, mid2-1)
    return slice(0, len(arr)-1)

if __name__ == "__main__":
    from random import randint
    for _ in range(10**3):
        arr = [1 for __ in range(3**5)]
        index = randint(0,3**3-1)
        arr[index] = 2
        assert arr.index(2) == find_2(arr)
