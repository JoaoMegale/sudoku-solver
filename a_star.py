import heapq
from common import is_valid

def count_filled_3x3_blocks(tabuleiro):
    """
    Retorna a quantidaed de blocos 3x3 preenchidos no tabuleiro (máximo 9)
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
    Retorna a quantidade de colunas preenchidas no tabuleiro (máximo 9)
    """    
    colunas_preenchidas = 0
    for coluna in range(9):
        if all(tabuleiro[linha][coluna] != 0 for linha in range(9)):
            colunas_preenchidas += 1
    return colunas_preenchidas


def count_filled_rows(tabuleiro):
    """
    Retorna a quantidade de linhas preenchidas no tabuleiro (máximo 9)
    """    
    linhas_preenchidas = 0
    for linha in tabuleiro:
        if 0 not in linha:
            linhas_preenchidas += 1
    return linhas_preenchidas


def count_filled_segments(board):
    """
    Retorna a quantidade de segmentos (linhas + colunas + blocos) preenchidos 
    no tabuleiro (máximo 27)
    """    
    rows = count_filled_rows(board)
    cols = count_filled_columns(board)
    blocks = count_filled_3x3_blocks(board)
    
    return (rows + cols + blocks)


def find_best_cell(board):
    """
    Encontra a célula que maximiza a heurística usada
    """    
    max_filled_segments = 0
    best_cell = None
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                new_board = [row[:] for row in board]
                new_board[i][j] = 10 # Valor auxiliar
                filled_segments = count_filled_segments(new_board)
                if filled_segments >= max_filled_segments:
                    max_filled_segments = filled_segments
                    best_cell = (i,j)
                    
    return best_cell


def a_star_sudoku(board):
    """
    Implementação do algoritmo A* para solucionar o Sudoku
    """
    # Fila de prioridade para gerenciar a expansão dos estados
    open_heap = []
    initial_h = count_filled_segments(board)
    # max_f = 9 + 9 + 9
    g = 0
    h = initial_h
    f = h + g
    heapq.heappush(open_heap, (f, board))
    num_expanded_states = 0
    
    while open_heap:
        _, current_board = heapq.heappop(open_heap)
        num_expanded_states += 1

        best_cell = find_best_cell(current_board)
        if not best_cell:
            return current_board, num_expanded_states  # Solução encontrada

        row, col = best_cell
        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                new_board = [row[:] for row in current_board]
                new_board[row][col] = num
                g += h
                h = count_filled_segments(board)
                f = g + h
                heapq.heappush(open_heap, (f, new_board))

    return None, num_expanded_states
