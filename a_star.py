import heapq
from common import is_valid
import numpy as np

def count_filled_3x3_blocks(tabuleiro):
    """
    Retorna a quantidaed de blocos 3x3 preenchidos no tabuleiro.
    """
    blocos_preenchidos = 0
    for bloco_linha in range(0, 9, 3):
        for bloco_coluna in range(0, 9, 3):
            bloco = []
            for i in range(3):
                for j in range(3):
                    bloco.append(tabuleiro[bloco_linha + i][bloco_coluna + j])
            if 0 not in bloco:
                blocos_preenchidos += 1
    return blocos_preenchidos


def count_filled_columns(tabuleiro):
    """
    Retorna a quantidade de colunas preenchidas no tabuleiro.
    """    
    colunas_preenchidas = 0
    for coluna in range(9):
        if all(tabuleiro[linha][coluna] != 0 for linha in range(9)):
            colunas_preenchidas += 1
    return colunas_preenchidas


def count_filled_rows(tabuleiro):
    """
    Retorna a quantidade de linhas preenchidas no tabuleiro.
    """    
    linhas_preenchidas = 0
    for linha in tabuleiro:
        if 0 not in linha:
            linhas_preenchidas += 1
    return linhas_preenchidas


def count_filled_segments(board):
    """
    Retorna a quantidade de segmentos (linhas + colunas + blocos) preenchidos 
    no tabuleiro. O resultado é multiplicado por -1 pois o heap prioriza o 
    menor elemento, mas o objetivo é maximizar.
    """    
    rows = count_filled_rows(board)
    cols = count_filled_columns(board)
    blocks = count_filled_3x3_blocks(board)
    
    return 27 - (rows + cols + blocks)


def find_best_cell(board):
    """
    Encontra a célula que maximiza a heurística.
    """    
    max_filled_segments = 27
    best_cell = None
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                new_board = [row[:] for row in board]
                new_board[i][j] = 10 # Valor auxiliar
                filled_segments = count_filled_segments(new_board)
                if filled_segments <= max_filled_segments:
                    max_filled_segments = filled_segments
                    best_cell = (i,j)
                    
    return best_cell


def a_star_sudoku(board):
    """
    Implementação do algoritmo A* para solucionar o Sudoku.
    """
    # Fila de prioridade
    open_heap = []
    
    # Valor inicial da heurística
    initial_h = count_filled_segments(board)
    
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

        print("Board:\n", np.array(current_board))

        if num_expanded_states == 10:
            return None, 0

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
                new_h = count_filled_segments(new_board)
                
                # Atualiza o valor de f (g+h)
                new_f = new_g + new_h
                
                # Adiciona o estado ao heap, junto com seu valor de f
                heapq.heappush(open_heap, (new_f, new_g, new_h, new_board))

    return None, num_expanded_states