#!/usr/bin/env python
INPUT = [1, 5, 6, 8, 13, 17, 22, 45]
TARGET = 132

check_left = 0
check_right = len(INPUT)-1
try:
    while INPUT[check_left] * INPUT[check_right] != TARGET:
        if INPUT[check_left] * INPUT[check_right] > TARGET:
            check_right -= 1
        else:
            check_left +=1
except IndexError:
    print("Product does not exist in the list.")

print(f"check_left={check_left}\ncheck_right={check_right}\nleft_element = {INPUT[check_left]}\nright_element = {INPUT[check_right]}")
print(f"{INPUT[check_left]}*{INPUT[check_right]}={INPUT[check_right]*INPUT[check_left]}")
