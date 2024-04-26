from common import is_valid, count_choices

import heapq

def heuristic(board):
    """
    Retorna a quantidade de células que podem ser automaticamente
    preenchidas (apenas 1 opção) em um tabuleiro.
    """
    count = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                if count_choices(board, i, j) == 1:
                    count += 1
                
    return count


def find_best_cell(board):
    """
    Retorna a célula com a menor quantidade de escolhas válidas.
    """
    min_count = float('inf')
    best_cell = None
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                count = count_choices(board, i, j)
                if count <= min_count:
                    min_count = count
                    best_cell = (i,j)
                    
    return best_cell
    

def a_star_sudoku(board):
    """
    Implementação do algoritmo A* para solucionar o Sudoku.
    """
    # Fila de prioridade
    open_heap = []
    
    # Valor inicial da heurística
    initial_h = heuristic(board)
    
    # Valores iniciais de g, h e f
    g = 0
    h = initial_h
    f = h + g
    
    # Adiciona o tabuleiro e o f iniciais ao heap
    heapq.heappush(open_heap, (f, g, h, board))
    num_expanded_states = 0
    
    while open_heap:
        # Atualiza o estado de acordo com a fila de prioridade
        current_f, current_g, current_h, current_board = heapq.heappop(open_heap)
        num_expanded_states += 1

        # print("Board:\n", np.array(current_board))

        # Encontra a melhor célula de acordo com a heurística
        best_cell = find_best_cell(current_board)
        
        # Caso a função retorne None, significa que não há mais células vazias
        if not best_cell:
            return current_board, num_expanded_states

        # Atualiza a célula a ser preenchida
        row, col = best_cell
        
        # Testa os valores para a célula selecionada
        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                
                # Atualiza o tabuleiro
                new_board = [row[:] for row in current_board]
                new_board[row][col] = num
                
                # Atualiza o custo até então (g)
                new_g = current_g + 1
                
                # Atualiza o valor da heurística
                new_h = heuristic(new_board)
                
                # Atualiza o valor de f (g+h)
                new_f = new_g + new_h
                
                # Adiciona o estado ao heap, junto com seu valor de f
                heapq.heappush(open_heap, (new_f, new_g, new_h, new_board))

    return None, num_expanded_states