def is_valid(board, row, col, num):
    """
    Verifica se um número pode ser inserido em determinada célula.
    """
    # Checa linha
    if num in board[row]:
        return False
    
    # Checa coluna
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Checa bloco 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def find_empty(board):
    """
    Procura pela próxima célula vazia no tabuleiro.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def count_choices(board, row, col):
    """
    Conta quantos valores válidos existem para uma célula.
    """
    count = 0
    for num in range(10):
        if is_valid(board, row, col, num):
            count += 1
            
    return count