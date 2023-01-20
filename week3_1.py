#!/usr/bin/env python
def find_index(expression, str_):
    for index in range(len(expression)):
        if expression[index] == str_:
            return index
    else:
        return -1

            
def evaluate(expression):
    if len(expression) == 1:
        return expression[0]
    index = find_index(expression, ")")
    if index == -1:
        print("Couldn't find ')'. Exiting...")
        exit(1)
    if expression[index-2] == "+":
        expression[index-4] = int(expression[index-3]) + int(expression[index-1])
        for i in range(4):
            del expression[index-3]
        return evaluate(expression)
    else:
        expression[index-4] = int(expression[index-3]) - int(expression[index-1])
        for i in range(4):
            del expression[index-3]
        return evaluate(expression)

print(evaluate(list("((3+2)-((1-2)+5))")))
#print(evaluate(list("(3+2)")))
