#!/usr/bin/env python
def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list
    mid = len(input_list)//2
    left_list = merge_sort(input_list[:mid])
    right_list = merge_sort(input_list[mid:])
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


sorted_list = merge_sort([68,34,52,12,9,32,67,99])
assert sorted_list == sorted([68,34,52,12,9,32,67,99])
print(sorted_list)
