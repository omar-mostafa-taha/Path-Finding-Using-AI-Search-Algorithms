import pygame
from BFS import bfs_solve
from A_star import a_star, S_E
from greedy import greedy
from DFS import dfs
from grid import loadgrid, savegrid
from Iterative_DFS import iter_dfs

def run_algorithm(algorithm, maze, heuristic_function=None):
    if algorithm == "BFS":
        found_path, steps, visited_cells, goal_path_length, execution_time= bfs_solve(maze)
    elif algorithm == "DFS":
        found_path, steps, visited_cells, goal_path_length, execution_time= dfs(maze)
    elif algorithm == "Iterative DFS":
        found_path, steps, visited_cells, goal_path_length, execution_time = iter_dfs(maze)

    return found_path, steps, visited_cells, goal_path_length, execution_time

def main():
    table = {
        "Algorithms": [],
        "Heuristic Function": [],
        "Number of steps": [],
        "Execution Time": [],
        "Number of visited cells": [],
    }

    pygame.init()

    # Set up the display mode
    size = (706, 706)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("MAZE")

    # Initialize your grid and other variables here

    # Load the default maze or set it up as needed
    grid = loadgrid(0)

    # Specify the heuristic functions you want to test
    heuristic_functions = ["manhattan", "euclidean", "octile", "chebyshev"]

    for heuristic_function in heuristic_functions:
        print(f"Heuristic Function: {heuristic_function}")
        table["Heuristic Function"].append(heuristic_function)
        algorithms = ["BFS","DFS", "Iterative DFS"]

        for algorithm in algorithms:
            table["Algorithms"].append(algorithm)
            print(f"Running {algorithm}")
            maze_copy = [row[:] for row in grid]  # Create a copy of the maze for each algorithm
            found_path, steps, visited_cells, goal_path_length, execution_time = run_algorithm(algorithm, maze_copy, heuristic_function)

            if found_path:
                print(f"Algorithm: {algorithm}, Steps: {steps}, Execution Time: {execution_time:.5f} seconds, Visited Cells: {visited_cells}, goal path length: {goal_path_length}")
            else:
                print(f"Algorithm: {algorithm}, No path found")

            # Append values to the table
            table["Number of steps"].append(steps)
            table["Execution Time"].append(execution_time)
            table["Number of visited cells"].append(visited_cells)

    pygame.quit()

if __name__ == "__main__":
    main()
