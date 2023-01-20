#!/usr/bin/env python
def find_max(input_list):
    if len(input_list) == 1:
        return input_list[0]
    mid = len(input_list)//2
    left_max = find_max(input_list[:mid])
    right_max = find_max(input_list[mid:])
    if left_max > right_max:
        return left_max
    else:
        return right_max

print(find_max([1,2,3,4,5]))
