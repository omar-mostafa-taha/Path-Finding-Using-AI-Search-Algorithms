def dfs_solve(maze, current, visited):
    global found
    i, j = current
    if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)) or maze[i][j] == 1 or visited[i][j]:
        return False

    visited[i][j] = True

    if maze[i][j] == 3:
        print("Found a path")
        found = True
        return True

    # Explore in all four directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        new_i, new_j = i + dx, j + dy
        if dfs_solve(maze, (new_i, new_j), visited):
            maze[i][j] = 4  # Mark the path
            return True

    return False