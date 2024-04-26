from bfs import bfs_sudoku
from ids import ids_sudoku
from ucs import ucs_sudoku
from gbfs import gbfs_sudoku
from a_star import a_star_sudoku

import time
import sys
import numpy as np

def main():
    if len(sys.argv) != 11:
        print("Usage: <method> <row1> <row2> <row3> <row4> <row5> <row6> <row7> <row8> <row9>")
        sys.exit(1)

    method = sys.argv[1]
    input_board = [list(map(int, list(sys.argv[i+2]))) for i in range(9)]
    
    start_time = time.time()

    if method == "B":
        solution, num_expanded_states = bfs_sudoku(input_board)
    elif method == "I":
        solution, num_expanded_states = ids_sudoku(input_board)
    elif method == "U":
        solution, num_expanded_states = ucs_sudoku(input_board)
    elif method == "G":
        solution, num_expanded_states = gbfs_sudoku(input_board)
    elif method == "A":
        solution, num_expanded_states = a_star_sudoku(input_board)

    end_time = time.time()

    elapsed_time_ms = int((end_time - start_time) * 1000)

    if solution:
        print(f"{num_expanded_states} {elapsed_time_ms}")
        print(" ".join("".join(map(str, row)) for row in solution))
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()