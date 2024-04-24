from bfs import bfs_sudoku
from ids import ids_sudoku
from gbfs import gbfs_sudoku
from a_star import a_star_sudoku

import time
import numpy as np

def main():
    
    input_strs = "107006450 025340008 060001070 053000029 610009800 000602007 001093200 008000000 040078591"
    linhas = input_strs.split()
    input_board = [list(map(int, linha)) for linha in linhas]
    
    metodo = input("metodo: ")

    start_time = time.time()

    if metodo == "B":
        solution, num_expanded_states = bfs_sudoku(input_board)
    if metodo == "I":
        solution, num_expanded_states = ids_sudoku(input_board)
    if metodo == "G":
        solution, num_expanded_states = gbfs_sudoku(input_board)
    if metodo == "A":
        solution, num_expanded_states = a_star_sudoku(input_board)

    end_time = time.time()

    elapsed_time_ms = int((end_time - start_time) * 1000)

    if solution:
        print(f"Number of states expanded: {num_expanded_states}")
        print(f"Execution time: {elapsed_time_ms} milliseconds")
        print("Solution:\n", np.array(solution))
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()