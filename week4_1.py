#!/usr/bin/env python
def evaluate(expression):
    if len(expression) == 1:
        return expression[0]
    level = 0
    for index in range(len(expression)):
        char = expression[index]
        if char == "(":
            level += 1
        elif char == ")":
            level -= 1
        elif char in "+-":
            # If level is 1 it means that the operator is one bracket deep.
            # That is the operator that we want to split the expression at.
            if level == 1:
                left_expression = expression[1:index]
                right_expression = expression[index + 1 : -1]
                if char == "+":
                    return int(evaluate(left_expression)) + int(
                        evaluate(right_expression)
                    )
                else:
                    return int(evaluate(left_expression)) - int(
                        evaluate(right_expression)
                    )


# expression = list("((3+2)-((1-2)+5))")
expression = list("(1+(1+(1+(1-(1+1)))))")
print(evaluate(expression))
