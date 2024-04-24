from common import is_valid, find_empty

def dfs(board, depth, max_depth, num_expanded_states):
    """
    Implementação da busca em profundidade para solucionar o Sudoku, com
    profundidade limitada.
    """    
    # Verifica se a profundidade máxima foi atingida
    if depth > max_depth:
        return None, num_expanded_states
    
    # Verifica se ainda há células vazias
    empty_pos = find_empty(board)
    if not empty_pos:
        return board, num_expanded_states

    # Escolhe a próxima célula a ser explorada
    row, col = empty_pos
    
    # Testa os valores para a célula selecionada
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            
            # O valor encontrado é adicionado ao tabuleiro
            board[row][col] = num
            num_expanded_states += 1
            
            # Chamada recursiva para a função, com a profundidade incrementada
            solution, num_expanded_states = dfs(board, depth + 1, max_depth, num_expanded_states)
            
            # Checa se a solução foi encontrada
            if solution:
                return solution, num_expanded_states
            
            # Caso a solução não foi encontrada, faz o backtrack
            board[row][col] = 0

    return None, num_expanded_states

def ids_sudoku(board):
    """
    Implementação do algoritmo Iterative Deepening Search para 
    solucionar o Sudoku.
    """
    # Inicia com profundidade 0
    max_depth = 0
    num_expanded_states = 0
    
    # Incrementa a profundidade limite a cada repetição do DFS, até encontrar uma solução
    while True:
        solution, num_expanded_states = dfs(board, 0, max_depth, num_expanded_states)
        if solution:
            return solution, num_expanded_states
        max_depth += 1