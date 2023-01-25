#!/usr/bin/env python
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
        if left_list[0] < right_list[0]:
            merged_list.append(left_list.pop(0))
        else:
            count += 1
            merged_list.append(right_list.pop(0))

    while len(left_list) != 0:  # Not empty
        count += 1
        merged_list.append(left_list.pop(0))

    while len(right_list) != 0:  # Not empty
        merged_list.append(right_list.pop(0))

    return merged_list


if __name__ == "__main__":
    # sorted_list = merge_sort([68,34,52,12,9,32,67,99])
    sorted_list = merge_sort([2, 4, 3, 5, 1])
    assert sorted_list == sorted([2, 4, 3, 5, 1])
    print(sorted_list)
    print(count)
