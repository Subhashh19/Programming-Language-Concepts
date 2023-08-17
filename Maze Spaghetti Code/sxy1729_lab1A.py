'''
Name: Sai Subhash Yalamadala 
UTA ID: 1002031729
Language: Python
OS: macOS 

'''
import random

def initialize_maze(x, y, value=0):
    maze = []
    for i in range(x):
        maze.append([value] * y)
    return maze    

def explore_direction(x, y, nx, ny):
    if x - nx == 0:
        if y - ny == 1:
            return 2  # return up
        else:
            return 1  # return down
    else:
        if x - nx == 1:
            return 3  # return left
        else:
            return 4  # return right

def generate_maze(width, height):
    # Initialize the maze grid
    maze = initialize_maze(height, width)
    # Initialize the path grid
    path = initialize_maze(height, width)

    # recursive function call
    def traverse(x, y, c):
        # Mark the current cell
        maze[y][x] = c
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Random the order of directions
        random.shuffle(directions)
        for dx, dy in directions:
            # Calculate the next coordinates
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= width or ny >= height:
                # Skip if next coordinates are out of bounds
                continue
            if maze[ny][nx] != 0:
                # Skip if the next cell is already visited
                continue
            # Determine and store the direction
            path[y][x] = explore_direction(x, y, nx, ny)
            # Recursively traverse the next cell
            traverse(nx, ny, c + 1)

    # Select a random starting position
    x = random.randint(0, width - 1)
    # traverse from top row
    traverse(x, 0, 1)

    return maze, path

# Prints the maze and path grids
def print_maze(maze, path):
    # Find the start point from top row
    start_point = maze[0].index(1)
    print(".", end="")
    for i in range(len(maze[0])):
        if i == start_point:
            print("  ", end="")
        else:
            print("--", end="")
        print(".", end="")
    print("\n", end="")

    for i in range(len(maze)):
        print("|  ", end="")
        for j in range(1, len(maze[0])):
            if abs(maze[i][j-1] - maze[i][j]) == 1:
                print("   ", end="")
            else:
                print("I  ", end="")
        print("I")

        if i != len(maze) - 1:
            for j in range(len(maze[0])):
                if abs(maze[i+1][j] - maze[i][j]) == 1:
                    print(":  ", end="")
                else:
                    print(":--", end="")
            print(".")

    # Find the end point from bottom row
    end_point = maze[len(maze)-1].index(max(maze[len(maze)-1]))
    print(".", end="")
    for i in range(len(maze[0])):
        if i == end_point:
            print("  ", end="")
        else:
            print("--", end="")
        print(".", end="")
    print("\n", end="")

def main():
    maze_width = 0
    maze_height = 0

    while maze_width < 2 or maze_height < 2:
        try:
            maze_width, maze_height = map(int, input("Enter the width and length of the maze: ").split(','))
        except ValueError:
            print("Invalid input. Please try again.")

        if maze_width < 2 or maze_height < 2:
            print("Invalid dimensions. Minimum width and height should be 2. Try again.")

    # Generate the maze
    maze, path = generate_maze(maze_width, maze_height)
    print("\nAMAZING PROGRAM")
    print("CREATIVE COMPUTING MORRISTOWN, NEW JERSEY")
    print("\n\n")
    # Print the maze
    print_maze(maze, path)
    print("OK")

main()
'''
References: https://github.com/russpj/Amazing 
'''