from queue import Queue
from A_star import S_E

def bfs_solve(maze):
    n_rows = len(maze)
    n_cols = len(maze[0])
    
    start, end = S_E(maze,0,0)
    queue = Queue()
    queue.put([start,[]]) # empty list to store the path
    visited = [[False] * n_cols for _ in range(n_rows)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while not queue.empty():
        current, path = queue.get()
        i, j = current
        if  (0 <= i < n_rows and 0 <= j < n_cols) and (maze[i][j] != 1) and (not visited[i][j]):
            visited[i][j] = True
            
            # if goal found return the path
            if maze[i][j] == 3:
                print("Found a path")
                path = path + [(i, j)]
                
                # mark visited cells 
                for row in range(n_rows):
                    for col in range(n_cols):
                        if visited[row][col]:
                            maze[row][col] = 6
                            
                # mark the path to the goal
                for (i,j) in path:
                    maze[i][j] = 4
                    
                return True
    
            # Explore in all four directions
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                queue.put( [ (new_i, new_j), path + [(i, j)] ] )
                
    print("No path found to the goal")
    return False

    
    
    
