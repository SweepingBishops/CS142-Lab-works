#!/usr/bin/env python
def find_fib(n):
    storage = [0]*2*n
    def fib(n):
        if storage[n-1] != 0:
            return storage[n-1]
        elif n == 0:
            return 0
        elif n == 1:
            return 1

        storage[n-1] = fib(n-1) + fib(n-2)
        return storage[n-1]
    return fib(n)

#breakpoint()
print(find_fib(100))
