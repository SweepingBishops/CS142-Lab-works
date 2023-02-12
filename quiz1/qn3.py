#!/usr/bin/env python
'''Given two sorted lists of size m and n, find the kth element of two sorted arrays in
O(log m + log n) time. 
'''

def find_k(arr1, arr2, k):
    len_1 = len(arr1)
    len_2 = len(arr2)
    if len_1 + len_2 < k or k < 1:
        return None

    if len_1 > len_2:
        return find_k(arr2, arr1, k)

    if len_1 == 0:
        return arr2[k-1]

    if k == 1:
        return min(arr1[0], arr2[0])

    mid1 = min(len_1, k//2)
    mid2 = min(len_2, k//2)

    if arr1[mid1-1] > arr2[mid2-1]:
        return find_k(arr1, arr2[mid2:], k-mid2)
    else:
        return find_k(arr1[mid1:], arr2, k-mid1)

    
if __name__ == "__main__":
    from random import randint, shuffle, choice
    for _ in range(10**3):
        generator_list = [i for i in range(100)]
        len_1 = randint(0,100)
        arr1 = [generator_list.pop(randint(0,len(generator_list)-1))
                for i in range(len_1)
               ]
        arr2 = generator_list.copy()
        arr1.sort()
        arr2.sort()
        k = randint(1,100)
        actual_value = sorted(arr1+arr2)[k-1]
        print(actual_value)
        assert find_k(arr1, arr2, k) == actual_value
