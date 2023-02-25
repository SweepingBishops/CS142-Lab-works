#!/usr/bin/env python

def find_max(n, current_row, queens):
    '''
    The function that generates all potential max configurations. And returns max.
    '''
    # For n <= 3 the answer is 1
    if n <= 3:
        return 1
    if current_row == n-1:
        return len(queens)

    new_configs = place_queens(n, current_row, queens)
    return max([find_max(n, current_row+1, pos) for pos in new_configs])
        


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


if __name__ == "__main__":
    import sys
    n=int(sys.argv[1])
    print(find_max(n,0,[]))
