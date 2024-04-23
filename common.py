def is_valid(board, row, col, num):
    # Verificar se o número não aparece na mesma linha
    if num in board[row]:
        return False
    
    # Verificar se o número não aparece na mesma coluna
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Verificar se o número não aparece no mesmo bloco 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None
