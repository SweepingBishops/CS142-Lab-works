#!/usr/bin/env python
def insertion_sort_asc(input_list, check_mult):
    for i in range(len(input_list)):
        if i % check_mult == 0:
            continue
        current = input_list[i]
        if (i-1)%check_mult == 0:
            j = i - 2
        else:
            j = i - 1
        while j >= 0 and input_list[j] > current:
            if (j+1) % check_mult != 0:
                input_list[j+1] = input_list[j]
            else:
                input_list[j+2] = input_list[j]

            if (j-1)%check_mult == 0:
                j -= 2
            else:
                j -= 1

        if (j+1) % check_mult != 0:
            input_list[j+1] = current
        else:
            input_list[j+2] = current

    return input_list


def insertion_sort_desc(input_list, check_mult):
    for i in range(0, len(input_list), check_mult):
        current = input_list[i]
        j = i - check_mult
        while j >= 0 and input_list[j] < current:
            input_list[j + check_mult] = input_list[j]
            j -= check_mult
        input_list[j + check_mult] = current
    return input_list


INPUT = [31, 12, 21, 55, 22, 1, 51, 30, 2, 7]
# INPUT = [7,8,9,7,6,5,4,3,2,1]
check_mult = 3

INPUT = insertion_sort_asc(INPUT, check_mult)
INPUT = insertion_sort_desc(INPUT, check_mult)

print(INPUT)
