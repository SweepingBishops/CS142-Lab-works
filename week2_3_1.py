#!/usr/bin/env python
# Both methods for this question basically do the same thing.
# It first sorts the positions that are not a multiple, ignoring the 
# multiples, and then sorts the rest ignoring the previously sorted
# elements.
input_list = [31,12,21,55,14,1,51,30,2,7]
k = 3
mult_indices = [i for i in range(len(input_list)) if (i+1)%k == 0]
not_mult_indices = [i for i in range(len(input_list)) 
                    if i not in mult_indices]

def insertion_sort_acs(input_list):
    for i in range(len(mult_indices)):
        current = input_list[mult_indices[i]]
        j = i - 1
        while j >= 0 and current < input_list[mult_indices[j]]:
            input_list[mult_indices[j+1]] = input_list[mult_indices[j]]
            j -= 1
        input_list[mult_indices[j+1]] = current

def insertion_sort_desc(input_list):
    for i in range(len(not_mult_indices)):
        current = input_list[not_mult_indices[i]]
        j = i - 1
        while j >= 0 and current > input_list[not_mult_indices[j]]:
            input_list[not_mult_indices[j+1]] = input_list[not_mult_indices[j]]
            j -= 1
        input_list[not_mult_indices[j+1]] = current


insertion_sort_acs(input_list)
insertion_sort_desc(input_list)
print(input_list)
