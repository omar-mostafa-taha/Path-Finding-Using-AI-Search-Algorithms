import time
from A_star import S_E

def dfs(maze):
    start, end = S_E(maze, 0, 0)
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    found_path, steps, visited_cells, goal_path_length, execution_time = dfs_solve(maze, start, visited)
    return found_path, steps, visited_cells, goal_path_length, execution_time

def dfs_solve(maze, current, visited, step_counter=0, visited_cells=0, goal_path_length=0, start_time=None):
    global found_path

    if start_time is None:
        start_time = time.time()  # Initialize start time only if not set

    i, j = current

    if not (0 <= i < len(maze) and 0 <= j < len(maze[0])) or maze[i][j] == 1 or visited[i][j]:
        return False, step_counter, visited_cells, goal_path_length, 0  # Return 0 execution time if the current cell is invalid

    visited[i][j] = True
    visited_cells += 1  # Increment visited cell count

    if maze[i][j] == 3:
  
        maze[i][j] = 4  # Mark the goal cell
        goal_path_length += 1  # Increment goal path length
        end_time = time.time()  # Record end time
        total_time = end_time - start_time  # Calculate total time
        found_path = True  # Set the global found_path variable
        return True, step_counter, visited_cells, goal_path_length, total_time

    maze[i][j] = 6  # Mark visited cell

    # Explore in all four directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        new_i, new_j = i + dx, j + dy
        if 0 <= new_i < len(maze) and 0 <= new_j < len(maze[0]) and not visited[new_i][new_j]:
            subpath_found, subpath_steps, subpath_visited_cells, subpath_goal_path_length, subpath_total_time = dfs_solve(
                maze, (new_i, new_j), visited, step_counter + 1, visited_cells, goal_path_length, start_time
            )
            step_counter = subpath_steps  # Use the step count from the subpath
            visited_cells = subpath_visited_cells  # Use the visited cell count from the subpath
            goal_path_length = subpath_goal_path_length  # Use the goal path length from the subpath

            if subpath_found:
                maze[i][j] = 4  # Mark the path
                goal_path_length += 1  # Increment goal path length
                end_time = time.time()  # Record end time
                total_time = end_time - start_time + subpath_total_time  # Calculate total time
                return True, step_counter, visited_cells, goal_path_length, total_time

    return False, step_counter, visited_cells, goal_path_length, 0
