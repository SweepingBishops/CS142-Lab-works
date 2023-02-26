#!/usr/bin/env python
curr_max = 0
board = []

def find_max(n):
    '''
    The function that generates all potential max configurations. And returns max.
    '''
    # For n <= 3 the answer is 1
    if n <= 3:
        global curr_max
        curr_max = 1
        return
    

    def _find_max(current_row, queens):
        global curr_max
        if current_row == n:
            if len(queens) > curr_max:
                curr_max = len(queens)
                global board
                board = queens
        
        new_configs = place_queens(n, current_row, queens)
        for config in new_configs:
            if len(config)+(n-current_row-1) > curr_max:
                _find_max(current_row+1, config)
            # num = _find_max(current_row+1, config)
            # if num > curr_max:
            #     curr_max = num
            #     board = config

    _find_max(0,[])
        


def place_queens(n, current_row, current_queens):
    '''
    Takes the values of the queens that are already on the board
    and tries to keep a queen on every column of the given row.
    '''
    if current_row >= n:
        return current_queens

    positions = []
    for column in range(n):
        if check_square(current_queens, (current_row, column)):
            #positions.append([current_queens + [(current_row, column)]])
            positions.append(current_queens + [(current_row, column)])
    if positions:
        return positions
    else:
        return [current_queens]
        


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
        elif abs(queen[0] - square[0]) == abs(queen[1] - square[1]):
            return False
        elif abs(abs(queen[0] - square[0]) * abs(queen[1] - square[1])) == 2:
            return False
    return True

def table(config, n):
    '''Just for pretty printing the boards.'''
    print("")
    for row in range(n):
        for column in range(n):
            if (row, column) in config:
                print(f"|{chr(9819)}", end = "")
            else:
                print("| ", end = "")
        print("|")

if __name__ == "__main__":
    import sys
    n=int(sys.argv[1])
    find_max(n)
    table(board, n)
    print(curr_max)
