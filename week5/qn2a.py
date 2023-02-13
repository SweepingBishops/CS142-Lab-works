#!/usr/bin/env python
'''(a) Given an n×n chess board, you must place n queens on the board so that no
two queens attack each other. Print a matrix satisfying the conditions with positions with
queens marked with ‘1’ and empty spaces with ‘0’. You must solve the n queens problem
using backtracking.
'''

def generate_configurations(n):
    if n <= 2:
        return False

    def place_queen(current_queens, rank):
        if rank > n:
            return current_queens
        positions = []
        for i in range(n):
            if check_square(current_queens, (rank, i)):
                positions.append(current_queens + [(rank, i)])
        if positions:
            return positions
        else:
            return False


    current_configs = place_queen([], 0)
    for queen in range(1,n):
        configs = list()
        #print(f"Current configs: {current_configs}")
        for current_queens in current_configs:
            #print(f"Current queens: {current_queens}")
            possible = place_queen(current_queens, queen)
            if possible:
                configs.extend(possible)
        #print(f"Configs: {configs}")
        current_configs = configs.copy()
    return current_configs


def check_square(queens, square):
    if not queens:
        return True
    #print(f"in check_sq: {queens}")
    for queen in queens:
        if square[0] == queen[0] or square[1] == queen[1]:
            return False
        if abs(queen[0] - square[0]) == abs(queen[1] - square[1]):
            return False
    return True
    
def table(configs, n):
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
