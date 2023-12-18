import time
from A_star import S_E

def iter_dfs(maze):
    n_rows = len(maze)
    n_cols = len(maze[0])

    start, end = S_E(maze, 0, 0)
    stack = [(start, [])]  # stack to store the current position and path
    visited = [[False] * n_cols for _ in range(n_rows)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    step_counter = 0  # Initialize step counter
    visited_cells = 0  # Initialize visited cell count
    start_time = time.time()  # Record start time

    while stack:
        current, path = stack.pop()  # Adjust stack handling to pop from the end (DFS behavior)
        i, j = current

        if 0 <= i < n_rows and 0 <= j < n_cols and maze[i][j] != 1 and not visited[i][j]:
            visited[i][j] = True
            visited_cells += 1  # Increment visited cell count

            # If goal found, return the path
            if maze[i][j] == 3:
                print("Found a path")
                path = path + [(i, j)]

                # Mark visited cells
                for row in range(n_rows):
                    for col in range(n_cols):
                        if visited[row][col]:
                            maze[row][col] = 6

                # Mark the path to the goal
                for (i, j) in path:
                    maze[i][j] = 4
                   
                end_time = time.time()  # Record end time
                total_time = end_time - start_time  # Calculate total time
                goal_path_length = len(path)  # Calculate goal path length
                return True, step_counter, visited_cells, goal_path_length, total_time

            # Explore in all four directions
            for dx, dy in directions[::-1]:  # to keep the same visiting order as the recursive DFS
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < n_rows and 0 <= new_j < n_cols and not visited[new_i][new_j]:
                    stack.append(((new_i, new_j), path + [(i, j)]))
                    step_counter += 1  # Increment step counter for each explored neighbor

    print("No path found to the goal")
    end_time = time.time()  # Record end time if no path is found
    total_time = end_time - start_time  # Calculate total time
    return False, step_counter, visited_cells, goal_path_length, total_time
