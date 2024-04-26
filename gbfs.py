from common import is_valid, count_choices

import heapq

def heuristic(board):
    """
    Retorna a soma total das escolhas de todas as células do tabuleiro.
    """
    total = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                total += count_choices(board, i, j)
                
    return total


def find_best_cell(board):
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
    Implementação do algoritmo Greedy Best-First Search para 
    solucionar o Sudoku.
    """
    # Fila de prioridade
    open_heap = []
    
    # Valor inicial da heurística
    initial_choices = heuristic(board)
    
    # Adiciona ao heap o tabuleiro e heurística inicial
    heapq.heappush(open_heap, (initial_choices, board))
    
    num_expanded_states = 0

    while open_heap:
        # Atualiza o estado de acordo com a fila de prioridade
        _, current_board = heapq.heappop(open_heap)
        num_expanded_states += 1

        # Encontra a melhor célula de acordo com a heurística
        least_choices_cell = find_best_cell(current_board)
        
        # Caso a função retorne None, significa que não há mais células vazias
        if not least_choices_cell:
            return current_board, num_expanded_states

        # Atualiza a célula a ser preenchida
        row, col = least_choices_cell
        
        # Testa os valores para a célula selecionada
        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                
                # Atualiza o tabuleiro
                new_board = [row[:] for row in current_board]
                new_board[row][col] = num
                
                # Atualiza a heurística
                new_choices = heuristic(new_board)
                
                # Adiciona tabuleiro e heurística ao heap
                heapq.heappush(open_heap, (new_choices, new_board))

    return None, num_expanded_states

