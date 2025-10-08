# Program to check if a Sudoku board is valid

def is_valid_sudoku(board):
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            if board[i][j] != '.' and board[i][j] in row:
                return False
            if board[j][i] != '.' and board[j][i] in col:
                return False
            row.add(board[i][j])
            col.add(board[j][i])
    return True

sudoku = [
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

print("Sudoku Board is Valid?", is_valid_sudoku(sudoku))
