import heapq
from common import is_valid

def count_choices(board, row, col):
    """
    Heurística utilizada. Conta quantos valores válidos existem para uma célula.
    """
    if board[row][col] != 0:
        return 0
    valid_numbers = set(range(1, 10))
    # Remove números já na linha
    valid_numbers -= set(board[row])
    # Remove números já na coluna
    valid_numbers -= set(board[i][col] for i in range(9))
    # Remove números já no bloco 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            valid_numbers -= {board[i][j]}
    return len(valid_numbers)


def find_least_choices_cell(board):
    """
    Encontra a célula com o menor número de escolhas válidas, ou seja, que
    minimiza a heurística.
    """
    min_choices = float('inf')
    best_cell = None
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                choices_count = count_choices(board, i, j)
                if choices_count < min_choices:
                    min_choices = choices_count
                    best_cell = (i, j)
    return best_cell


def gbfs_sudoku(board):
    """
    Implementação do algoritmo GBFS para solucionar o Sudoku
    """
    # Fila de prioridade para gerenciar a expansão dos estados
    open_heap = []
    initial_choices = sum(count_choices(board, i, j) for i in range(9) for j in range(9) if board[i][j] == 0)
    heapq.heappush(open_heap, (initial_choices, board))
    num_expanded_states = 0

    while open_heap:
        _, current_board = heapq.heappop(open_heap)
        num_expanded_states += 1

        least_choices_cell = find_least_choices_cell(current_board)
        if not least_choices_cell:
            return current_board, num_expanded_states  # Solução encontrada

        row, col = least_choices_cell
        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                new_board = [row[:] for row in current_board]
                new_board[row][col] = num
                new_choices = sum(count_choices(new_board, i, j) for i in range(9) for j in range(9) if new_board[i][j] == 0)
                heapq.heappush(open_heap, (new_choices, new_board))

    return None, num_expanded_states


input_strs = ["107006450", "025340008", "060001070", "053000029", "610009800", "000602007", "001093200", "008000000", "040078591"]
input_board = [list(map(int, list(row))) for row in input_strs]

board, num = gbfs_sudoku(input_board)

