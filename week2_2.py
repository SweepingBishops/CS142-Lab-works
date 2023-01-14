#!/usr/bin/env python
# qn a
COURSES = ["b102", "c102", "cs142", "m102", "c102", "m102", "b102", "p102", "p102"]
# The courses list is scanned through, every time a new element is scanned, it is
# added to a list. If an element is seen the second time, it is removed from the 
# list. The element left at the end is the required element.
appearance = list()
for course in COURSES:
    if course not in appearance:
        appearance.append(course)
    else:
        appearance.remove(course)

print(f"{appearance[0]} doesn't appear twice.")

# qn b
input_list = [3, 1, 2, 5, 4, 1, 5, 3, 2]
n = 5
sum_ = 0
for num in input_list:
    sum_ += num

missing_num = n*(n+1) - sum_
print("The missing number is:", missing_num)
