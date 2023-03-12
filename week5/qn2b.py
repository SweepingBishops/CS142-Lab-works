#!/usr/bin/env python
def find_max(n):
    """
    The function that generates all potential max configurations. And returns max.
    """
    # For n <= 3 the answer is 1
    if n <= 3:
        curr_max = 1
        board = [(0, 0)]
        return board, curr_max
    curr_max = 0
    board = []

    def _find_max(current_row, queens):
        nonlocal curr_max
        nonlocal board

        if curr_max == n:
            return
        if current_row == n:
            if len(queens) > curr_max:
                curr_max = len(queens)
                board = queens
            return

        new_configs = place_queens(n, current_row, queens)
        for config in new_configs:
            if len(config) + (n - current_row - 1) > curr_max:
                _find_max(current_row + 1, config)

    _find_max(0, [])
    return board, curr_max


def place_queens(n, current_row, current_queens):
    """
    Takes the values of the queens that are already on the board
    and tries to keep a queen on every column of the given row.
    """
    if current_row >= n:
        return current_queens

    positions = []
    for column in range(n):
        if check_square(current_queens, (current_row, column)):
            positions.append(current_queens + [(current_row, column)])

    if positions:
        return positions
    else:
        return [current_queens]


def check_square(queens, square):
    """
    Takes the values of the queens already on the board and returns
    whether a queen can be kept on a given square or not.
    """
    if not queens:
        return True
    for queen in queens:
        if square[0] == queen[0] or square[1] == queen[1]:
            return False
        elif abs(queen[0] - square[0]) == abs(queen[1] - square[1]):
            return False
        elif abs(queen[0] - square[0]) * abs(queen[1] - square[1]) == 2:
            return False
    return True


def pretty_print(config, n):
    """Just for pretty printing the boards."""
    for row in range(n):
        for column in range(n):
            if (row, column) in config:
                print(f"|{chr(9819)}", end="")
            else:
                print("| ", end="")
        print("|")
    print("")


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    board, num = find_max(n)
    pretty_print(board, n)
    print(num)
