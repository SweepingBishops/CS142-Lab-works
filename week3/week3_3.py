#!/usr/bin/env python
def create_dict(ORDER):
    order_dict = dict()
    for index in range(len(ORDER)):
        order_dict[ORDER[index]] = index
    return order_dict
        

def insertion_sort(input_list, order_dict):
    for i in range(1, len(input_list)):
        current = input_list[i]
        j = i-1
        while j >= 0 and order_dict[input_list[j]] > order_dict[current]:
            input_list[j+1] = input_list[j]
            j = j-1
        input_list[j+1] = current
    return input_list


INPUT = list("dcabesfshdsakcdc")
ORDER = list("bacdefshk")
print(insertion_sort(INPUT, create_dict(ORDER)))
