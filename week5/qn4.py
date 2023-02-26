#!/usr/bin/env python
class ChessBoard():
    values = {
              "k":9812,
              "q":9813,
              "r":9814,
              "b":9815,
              "n":9816,
              "p":9817,
              "K":9818,
              "Q":9819,
              "R":9820,
              "B":9821,
              "N":9822,
              "P":9823,
              }
    def __init__(self):
        self.board = dict()
        for row in range(8):
            for column in range(8):
                self.board[(row, column)] = 0
    
    def starting_position(self):
        for i in range(8):
            self.board[(1,i)] = "P"
            self.board[(6,i)] = "p"
            if i == 0 or i == 7:
                self.board[(0,i)] = "R"
                self.board[(7,i)] = "r"
            if i == 1 or i == 6:
                self.board[(0,i)] = "N"
                self.board[(7,i)] = "n"
            if i == 2 or i == 5:
                self.board[(0,i)] = "B"
                self.board[(7,i)] = "b"
            if i == 3:
                self.board[(0,i)] = "Q"
                self.board[(7,i)] = "q"
            if i == 4:
                self.board[(0,i)] = "K"
                self.board[(7,i)] = "k"

    def print(self):
        for row in range(8):
            for column in range(8):
                piece = self.board[(row, column)]
                if piece:
                    print(f"|{chr(ChessBoard.values[piece])}", end = "")
                else:
                    print("| ", end = "")
            print("|")


chess_board = ChessBoard()
chess_board.starting_position()
chess_board.print()
