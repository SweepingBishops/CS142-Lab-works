#!/usr/bin/env python
def insertion_sort(input_list):
    counter = 0
    for i in range(1, len(input_list)):
        current = input_list[i]
        j = i - 1
        while j >= 0 and input_list[j] > current:
            counter += 1
            input_list[j+1] = input_list[j]
            j = j - 1
        input_list[j+1] = current
    return counter


print(insertion_sort([2, 4, 3, 5, 1]))
