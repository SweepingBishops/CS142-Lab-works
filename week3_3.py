#!/usr/bin/env python
def find_index(expression, str_):
    for index in range(len(expression)):
        if expression[index] == str_:
            return index
    else:
        return -1

def insertion_sort(input_list, order):
    for i in range(1, len(input_list)):
        current = input_list[i]
        j = i-1
        while j >= 0 and find_index(order, input_list[j]) > find_index(order, current):
            input_list[j+1] = input_list[j]
            j = j-1
        input_list[j+1] = current
    return input_list

INPUT = list("dcabesfshdsakcdc")
ORDER = list("bacdefshk")
print(insertion_sort(INPUT, ORDER))
