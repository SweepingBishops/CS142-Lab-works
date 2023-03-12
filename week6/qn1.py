#!/usr/bin/env python
from time import time, sleep
N = 9  # N has to be a perfect square.
n = int(N**0.5)
board = [
    [0,0,0, 0,0,0, 2,0,0,],
    [0,8,0, 0,0,7, 0,9,0,],
    [6,0,2, 0,0,0, 5,0,0,],

    [0,7,0, 0,6,0, 0,0,0,],
    [0,0,0, 9,0,1, 0,0,0,],
    [0,0,0, 0,2,0, 0,4,0,],

    [0,0,5, 0,0,0, 6,0,3,],
    [0,9,0, 4,0,0, 0,7,0,],
    [0,0,6, 0,0,0, 0,0,0,],
    ]

def check_legal(val,row,col):
    for i in range(N):
        if val == board[i][col] or val == board[row][i]:
            return False

    row_offset, col_offset = row % n, col % n
    sub_row_beg = row - row_offset
    sub_row_end = sub_row_beg + n
    sub_col_beg = col - col_offset
    sub_col_end = sub_col_beg + n
    for i in range(sub_row_beg, sub_row_end):
        for j in range(sub_col_beg, sub_col_end):
            if val == board[i][j]:
                return False
    
    return True

def place_value(row, col):
    if col >= N:
        col = 0
        row += 1

    if row >=N:
        end = time()
        pretty_print()
        print(f"Time: {end-start}")
        exit()

    while board[row][col] != 0:
        col += 1
        if col >= N:
            col = 0
            row += 1
        if row >=N:
            end = time()
            pretty_print()
            print(f"Time: {end-start}")
            exit()

    for val in range(1, N+1):
        if check_legal(val, row, col):
            board[row][col] = val
            pretty_print()
            sleep(0.05)
            place_value(row, col+1)
    else:
        board[row][col] = 0
        return


def pretty_print():
    print("\x1bc")
    for row in range(N):
        print("|", end = "")
        for col in range(N):
            print(f"{board[row][col]}|",end="")
            if (col+1)%n == 0 and col+1!=N:
                print(" |", end = "")
        if (row+1)%n == 0:
            print("\n")
        else:
            print("")


start = time()
place_value(0,0)
