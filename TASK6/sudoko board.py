# Program to check if a Sudoku board is valid

def is_valid_sudoku(board):
    for i in range(9):
        row = [x for x in board[i] if x != '.']
        col = [board[j][i] for j in range(9) if board[j][i] != '.']
        if len(row) != len(set(row)) or len(col) != len(set(col)):
            return False
    return True

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print("Sudoku Board is Valid?", is_valid_sudoku(board))
