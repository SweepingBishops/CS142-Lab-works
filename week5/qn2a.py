#!/usr/bin/env python
'''(a) Given an n×n chess board, you must place n queens on the board so that no
two queens attack each other. Print a matrix satisfying the conditions with positions with
queens marked with ‘1’ and empty spaces with ‘0’. You must solve the n queens problem
using backtracking.
'''

def generate_configurations(n):
    '''The function that generates all the possible configurations.'''
    # There are no possible solution to the problem if n <= 2
    if n <= 2:
        return False

    configs = place_queen([], 0)

    for row in range(1,n):
        current_configs = list()
        for current_queens in configs:
            possible = place_queen(current_queens, row)
            if possible:
                current_configs.extend(possible)
        configs = current_configs
    return configs


def place_queen(current_queens, row):
    '''
    Takes the values of the queens that are already on the board
    and tries to keep a queen on every column of the given row.
    Returns the positions which are acceptable.
    '''
    if row > n:
        return current_queens
    positions = []
    for i in range(n):
        if check_square(current_queens, (row, i)):
            positions.append(current_queens + [(row, i)])
    if positions:
        return positions
    else:
        return False


def check_square(queens, square):
    '''
    Takes the values of the queens already on the board and returns
    whether a queen can be kept on a given square or not.
    '''
    if not queens:
        return True
    for queen in queens:
        if square[0] == queen[0] or square[1] == queen[1]:
            return False
        if abs(queen[0] - square[0]) == abs(queen[1] - square[1]):
            return False
    return True

    
def table(configs, n):
    '''Just for pretty printing the boards.'''
    for config in configs:
        print("")
        for row in range(n):
            for column in range(n):
                if (row, column) in config:
                    print(f"|{chr(9819)}", end = "")
                else:
                    print("| ", end = "")
            print("|")
    print(len(configs))

if __name__ == "__main__":
    n=8
    table(generate_configurations(n),n)
