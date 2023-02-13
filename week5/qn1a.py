#!/usr/bin/env python
'''(a) Given a set of non-negative integers, a value t, and an integer k, determine
if there is a subset of size exactly k such that the sum of the elements in the set is equal to
t. Use backtracking to reduce the number of calls you make to your recursive function.
Example:
Input: [3, 34, 4, 12, 5, 2], t = 9, k = 2
Output: True, there is a subset (4, 5) of size 2 with a sum of 9.
'''
def is_subset_sum(arr, target, length):
    arr.sort()
    def _is_subset_sum(current, weight, current_subset):
        if weight + arr[current] > target:
            return False  # Since sorted array of positives
        elif weight + arr[current] == target:
            if len(current_subset) + 1 == length:
                return True
            else:
                return False

        if current == len(arr) - 1:
            return False
        #elif len(current_subset) == length - 1:
        #    return False
        else:
            return  _is_subset_sum(current+1, weight + arr[current], current_subset + [arr[current]]) \
        or _is_subset_sum(current+1, weight, current_subset)
    
    return _is_subset_sum(0, 0, [])

if __name__ == "__main__":
    arr = [0,3,4,10,14,15,18]
    target = 18
    length = 2
    print(is_subset_sum(arr, target, length))
