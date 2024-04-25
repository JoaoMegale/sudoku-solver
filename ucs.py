from common import is_valid, find_empty

import heapq

def ucs_sudoku(board):
    """
    Implementação do algoritmo Uniform Cost Search para solucionar o Sudoku.
    """
    # Inicia uma fila de prioridade
    queue = []
    heapq.heappush(queue, (0, board))

    expanded_states = 0

    while queue:
        # Atualiza o custo e o tabuleiro atual
        cost, current_board = heapq.heappop(queue)
        expanded_states += 1
        
        # Encontra a primeira célula vazia
        empty_pos = find_empty(current_board)
        
        # Verifica se há posições vazias
        if not empty_pos:
            return current_board, expanded_states
        else:
            row, col = empty_pos
        
        # Testa os valores para a célula selecionada
        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                # Atualiza o estado, incrementa o custo e adiciona ao heap
                new_board = [row[:] for row in current_board]
                new_board[row][col] = num
                heapq.heappush(queue, (cost + 1, new_board))

    return None, expanded_states

