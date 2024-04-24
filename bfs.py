from common import is_valid, find_empty

from collections import deque

def bfs_sudoku(board):
    """
    Implementação da busca em largura para solucionar o Sudoku.
    """
    # Inicia uma fila
    queue = deque([board])
    num_expanded_states = 0
    
    # Roda enquanto a fila não for vazia
    while queue:
        # Atualiza o estado, pegando o próximo da fila
        current_board = queue.popleft()
        
        # Incrementa o número de estados expandidos
        num_expanded_states += 1
        
        # Encontra a próxima célula a ser preenchida
        empty_pos = find_empty(current_board)
        
        if not empty_pos:
            # Se não há posições vazias, temos um resultado
            return current_board, num_expanded_states
        else:
            row, col = empty_pos
        
        # Testa os valores para a célula selecionada
        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                # Atualiza o estado, adicionando a próxima célula
                new_board = [row[:] for row in current_board]
                new_board[row][col] = num
                queue.append(new_board)
    
    return None, num_expanded_states