# Simple version: find largest rectangle of 1s in a binary matrix

matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

max_area = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "1":
            width = 1
            while j + width < len(matrix[i]) and matrix[i][j + width] == "1":
                width += 1
            max_area = max(max_area, width)

print("Maximum Rectangle Area:", max_area)
