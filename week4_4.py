#!/usr/bin/env python
def find_median(array1, array2):
    # Stop condition for the recursion.
    if len(array1) == 2:
        return (max(array1[0], array2[0]), min(array1[1], array2[1]))

    # Different check indices depending on the whether the
    # list is even or odd.
    left_check, right_check = len(array1) // 2, len(array1) // 2 + len(array1) % 2 - 1

    # If the two elements we check are equal then they have to be the medians.
    if array1[left_check] == array2[right_check]:
        return (array1[left_check], array1[left_check])
    elif array1[left_check] < array2[right_check]:
        return find_median(array1[left_check:], array2[: right_check + 1])
    else:
        return find_median(array1[: left_check + 1], array2[right_check:])


if __name__ == "__main__":
    array1 = [1, 4, 6, 18]
    array2 = [2, 4, 7, 10]

    median = find_median(array1, array2)
    array3 = array1 + array2
    array3.sort()
    med = len(array3) // 2
    assert array3[med], array3[med + 1] == median
    print(median)
