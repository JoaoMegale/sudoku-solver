from common import is_valid, find_empty

def dfs(board, depth, max_depth, num_expanded_states):
    if depth > max_depth:
        return None, num_expanded_states

    empty_pos = find_empty(board)
    if not empty_pos:
        return board, num_expanded_states  # Solução encontrada

    row, col = empty_pos
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            num_expanded_states += 1
            solution, num_expanded_states = dfs(board, depth + 1, max_depth, num_expanded_states)
            if solution:
                return solution, num_expanded_states
            board[row][col] = 0  # Backtrack

    return None, num_expanded_states

def ids_sudoku(board):
    depth = 0
    num_expanded_states = 0
    while True:
        solution, num_expanded_states = dfs(board, 0, depth, num_expanded_states)
        if solution:
            return solution, num_expanded_states
        depth += 1
