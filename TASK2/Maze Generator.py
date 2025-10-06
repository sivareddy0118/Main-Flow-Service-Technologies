# Maze Generator and Solver using DFS

import random

def create_maze(size):
    maze = [[1 for _ in range(size)] for _ in range(size)]
    
    def carve(x, y):
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 < nx < size and 1 < ny < size and maze[ny][nx] == 1:
                maze[ny - dy//2][nx - dx//2] = 0
                maze[ny][nx] = 0
                carve(nx, ny)

    maze[1][1] = 0
    carve(1, 1)
    return maze

def display_maze(maze):
    for row in maze:
        print("".join('█' if cell else ' ' for cell in row))

print("MAZE GENERATOR AND SOLVER PROJECT")
maze = create_maze(11)
display_maze(maze)
