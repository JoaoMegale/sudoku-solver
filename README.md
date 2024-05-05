# Sudoku Solver

Este programa é um resolvedor de Sudoku que suporta vários algoritmos de busca para encontrar a solução. O usuário pode especificar o algoritmo e fornecer o estado inicial do Sudoku através da linha de comando.

## Uso

Para executar este programa, você precisará passar dois argumentos na linha de comando:
1. A letra correspondente ao algoritmo de busca desejado.
2. A tabela do Sudoku, onde cada linha do Sudoku é separada por um espaço.

## Algoritmos disponíveis

B - Breadth First Search <br>
I - Iterative Deepening Search <br>
U - Uniform Cost Search <br>
G - Greedy Best-First Search <br>
A - A* Search <br>

## Comando para execução

```bash
python3 main.py <algoritmo> <sudoku>
python3 main.py G 800000000 003600000 070090200 050007000 000045700 000100030 001000068 008500010 090000400


