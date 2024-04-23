from common import is_valid, find_empty

from collections import deque

def bfs_sudoku(board):
    queue = deque([board])
    num_expanded_states = 0
    
    while queue:
        current_board = queue.popleft()
        num_expanded_states += 1
        empty_pos = find_empty(current_board)
        
        if not empty_pos:
            # Se não há posições vazias, o Sudoku está resolvido
            return current_board, num_expanded_states
        else:
            row, col = empty_pos
        
        # Tentar todos os números possíveis nessa posição
        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                # Cria uma cópia do estado atual e adiciona o número ao tabuleiro
                new_board = [row[:] for row in current_board]
                new_board[row][col] = num
                queue.append(new_board)
    
    return None, num_expanded_states  # Se nenhum estado de solução for encontrado