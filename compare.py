import pygame
from BFS import bfs_solve
from A_star import a_star
from greedy import greedy
from DFS import dfs
from grid import loadgrid
from Iterative_DFS import iter_dfs
from prettytable import PrettyTable  # Make sure to install this library

def run_algorithm(algorithm, maze, heuristic_function=None):
    if algorithm == "A*":
        found_path, steps, visited_cells, goal_path_length, execution_time = a_star(maze, heuristic_function)
    elif algorithm == "Gready":
        found_path, steps, visited_cells, goal_path_length, execution_time = greedy(maze, heuristic_function)
    elif algorithm == "BFS":
        found_path, steps, visited_cells, goal_path_length, execution_time = bfs_solve(maze)
    elif algorithm == "DFS":
        found_path, steps, visited_cells, goal_path_length, execution_time = dfs(maze)
    elif algorithm == "Iterative DFS":
        found_path, steps, visited_cells, goal_path_length, execution_time = iter_dfs(maze)

    return found_path, steps, visited_cells, goal_path_length, execution_time

def main():
    pygame.init()

    # Set up the display mode
    size = (706, 706)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("MAZE")

    # Initialize your grid and other variables here

    # Load the default maze or set it up as needed
    maze_num = int(input("Enter the maze number (1-5): "))
    grid = loadgrid(maze_num)

    # Specify the heuristic functions you want to test
    heuristic_functions = ["manhattan", "euclidean", "octile", "chebyshev"]

    for heuristic_function in heuristic_functions:
        table = PrettyTable()
        table.field_names = ["Algorithm", "Found Path", "Steps", "Execution Time", "Visited Cells", "Goal Path Length"]

        algorithms = ["A*", "Gready", "BFS", "DFS", "Iterative DFS"]

        for algorithm in algorithms:
            maze_copy = [row[:] for row in grid]  # Create a copy of the maze for each algorithm
            found_path, steps, visited_cells, goal_path_length, execution_time = run_algorithm(algorithm, maze_copy, heuristic_function)

            table.add_row([algorithm, found_path, steps, f"{execution_time:.5f} seconds", visited_cells, goal_path_length])

        print(f"Heuristic Function: {heuristic_function}")
        print(table)
        print("\n")

    pygame.quit()

if __name__ == "__main__":
    main()
