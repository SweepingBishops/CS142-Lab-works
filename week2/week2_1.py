#!/usr/bin/env python
'''Program to find the power of a number using 2log(exponent) 
   multiplications.'''

# Inputs (note: only non-negative exponents are supported).
base = 7
exp = 100

counter = 0

# This function is used internally to calculate the power when the 
# exponent is of the form of 2^m.
# Accepts the base and the power of 2, i.e 'm' in the above comment.
def _2_k_exp(base, exp):
    global counter
    if exp == 0:
        return base
    reduced_exp = _2_k_exp(base, exp-1)
    counter += 1
    return reduced_exp * reduced_exp

# The function for calculating the power.
# Accepts the base and the exponent.
def power(base, exp):
    rev_bin_exp = bin(exp)[-1:1:-1]
    prod = 1
    for i in range(len(rev_bin_exp)):
        if rev_bin_exp[i]=="1":
            prod *= _2_k_exp(base, i)
    return prod

val = power(base, exp)
# Checks if the calculated value is correct, using the standard
# exponent operator in python.
assert val == base**exp
print(f"{base}^{exp} = {val}")
print(f"counter = {counter}")
