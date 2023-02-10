#!/usr/bin/env python
'''Given a list L and an integer N, write a code of merge sort to sort L that uses insertion
sort as the base case when the list is of size ≤ N.
'''

def merge_sort(input_list, critical_length):
    if len(input_list) <= critical_length:
        return insertion_sort(input_list)
    mid = len(input_list)//2
    left_list = merge_sort(input_list[:mid], critical_length)
    right_list = merge_sort(input_list[mid:], critical_length)
    return merge(left_list, right_list)

def merge(left_list, right_list):
    merged_list = list()
    while len(left_list) != 0 and len(right_list) != 0:
        if left_list[0] < right_list[0]:
            merged_list.append(left_list.pop(0))
        else:
            merged_list.append(right_list.pop(0))

    while len(left_list) != 0:  # Not empty
        merged_list.append(left_list.pop(0))

    while len(right_list) != 0:  # Not empty
        merged_list.append(right_list.pop(0))

    return merged_list

def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        current = input_list[i]
        j = i-1
        while j >= 0 and input_list[j] > current:
            input_list[j+1] = input_list[j]
            j = j-1
        input_list[j+1] = current
    return input_list

if __name__ == "__main__":
    from random import shuffle
    INPUT = [i for i in range(50)]
    template = [i for i in range(50)]
    for _ in range(10**3):
        shuffle(INPUT)
        INPUT = merge_sort(INPUT, 5)
        assert INPUT == template
