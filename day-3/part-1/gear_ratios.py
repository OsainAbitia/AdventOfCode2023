import re

DIRECTIONS = [
        (-1, -1), # Top-left
        (-1, 0),  # Up
        (-1, 1),  # Top-right
        (0, -1),  # Left
        (0, 1),   # Right
        (1, -1),  # Bottom-left
        (1, 0),   # Down
        (1, 1)    # Bottom-right
    ]
processed_locations = set()

def isValidCharacter(char: str) -> bool:
    return not (char.isdigit() or char == '.')

def isAdjacentToSymbol(board: list, row: int, col: int) -> bool:
    for dx, dy in DIRECTIONS:
        if 0 <= row + dx < len(board) and 0 <= col + dy < len(board[row + dx]):
            if isValidCharacter(board[row + dx][col + dy]):
                return True
    return False

def gearRatios(board: list) -> int:
    total = 0
    for i, row in enumerate(board):
        j = 0
        while j < len(row):
            if row[j].isdigit() and (i, j) not in processed_locations:
                number, init_j = row[j], j
                while j + 1 < len(row) and row[j + 1].isdigit():
                    number += row[j + 1]
                    j += 1
                
                for col_index in range(init_j, j + 1):
                    processed_locations.add((i, col_index))
                    if isAdjacentToSymbol(board, i, col_index):
                        total += int(number)
                        break
            j += 1
    return total
                

if __name__ == '__main__':
    with open('../input.txt') as f:
        board = [line.rstrip() for line in f]
    print(gearRatios(board))
