#!/usr/bin/env python
def bin_search(array, target, left_check, right_check):
    """Binary search function.
    left_check and right_check should be initialised to 0
    and len(array)-1 respectively."""
    # Stop condition for the recursion is when the length of
    # the list we're considering becomes 1.
    if left_check == right_check:
        if array[left_check] >= target:
            return left_check
        else:
            return left_check + 1

    check_index = (left_check + right_check) // 2
    if array[check_index] >= target:
        return bin_search(array, target, left_check, check_index)
    else:
        # This condition is here to prevent infinite recursion,
        # this condition pretty much only happens when the length
        # of the considered list becomes 2.
        if check_index == left_check:
            check_index = right_check
        return bin_search(array, target, check_index, right_check)


def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        current = input_list[i]
        j = i - 1
        del input_list[i]
        index = bin_search(
            input_list[: j + 1], current, 0, len(input_list[: j + 1]) - 1
        )
        # Just to note that python implements the .insert() method
        # in O(n) time. But that does not affect the number of
        # comparisons.
        input_list.insert(index, current)
    return input_list


if __name__ == "__main__":
    # input_list = [4,5,7,2,47,34,72,4]
    # print(insert(input_list))
    for i in range(10**3):
        starter_list = [i for i in range(100)]
        input_list = starter_list.copy()
        insertion_sort(input_list)
        assert input_list == sorted(starter_list)
