#!/usr/bin/env python
import week2_4
from random import shuffle

count = 0

def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list
    mid = len(input_list) // 2
    left_list = merge_sort(input_list[:mid])
    right_list = merge_sort(input_list[mid:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    global count
    merged_list = list()
    while len(left_list) != 0 and len(right_list) != 0:
        if left_list[0] <= right_list[0]:
            merged_list.append(left_list.pop(0))
        else:
            count += len(left_list)
            merged_list.append(right_list.pop(0))
    while len(left_list) != 0:  # Not empty
        merged_list.append(left_list.pop(0))

    while len(right_list) != 0:  # Not empty
        merged_list.append(right_list.pop(0))

    return merged_list


if __name__ == "__main__":
    # Code to check if it actually works.
    # Uses a previous weeks insertion sort 
    # alg to check.
    starter_list = [i for i in range(100)]
    for i in range(10**3):
        count = 0
        print(i)
        shuffle(starter_list)
        test_list = starter_list.copy()
        array = starter_list.copy()
        correct_count = week2_4.insertion_sort(test_list)
        merge_sort(starter_list)
        if count != correct_count:
            print(f"list: {array}\ncorrect count: {correct_count}\ncount: {count}")
