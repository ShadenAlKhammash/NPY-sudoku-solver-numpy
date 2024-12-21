import numpy as np
import collections
import itertools

# Part 1:
def string_puzzle_to_arr(puzzle):
    return np.array([list(line.strip()) for line in puzzle.split('\n') if line.strip()], dtype= int)

class Board:
    def __init__(self, puzzle):
        if isinstance(puzzle, str):
            self.arr = string_puzzle_to_arr(puzzle)
        else: 
            self.arr = puzzle

    def get_row(self, row_index):
        return self.arr[row_index]

    def get_column(self, col_index):
        return self.arr[:, col_index]

    def get_block(self, pos_1, pos_2):
        start_row = pos_1 * 3
        start_col = pos_2 * 3
        return self.arr[start_row : start_row+3, start_col: start_col+3]

    def iter_rows(self):
        return [row for row in self.arr]

    def iter_columns(self):
        return [col for col in self.arr.T]

    def iter_blocks(self):
        return [self.get_block(i, j) for i in range(3) for j in range(3)]


# Part 2:
def is_subset_valid(arr):
    pass

def is_valid(board):
    pass


# Part 3:
def find_empty(board):
    pass

def is_full(board):
    pass

def find_possibilities(board, x, y):
    pass


# Part 4:
def adapt_long_sudoku_line_to_array(line):
    pass

def read_sudokus_from_csv(filename, read_solutions=False):
    pass

def detect_invalid_solutions(filename):
    pass