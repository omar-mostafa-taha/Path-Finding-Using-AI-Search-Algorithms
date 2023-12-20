import time
import pygame
import math
from queue import PriorityQueue

def h(p1, p2,heuristic="manhattan"):
    cost = 0
    if heuristic == "manhattan":
        x1, y1 = p1
        x2, y2 = p2
        cost =  abs(x1 - x2) + abs(y1 - y2)
    elif heuristic == "euclidean":
        x1, y1 = p1
        x2, y2 = p2
        cost = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    elif heuristic == "octile":
        x1, y1 = p1
        x2, y2 = p2
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        cost = max(dx, dy) + (math.sqrt(2) - 1) * min(dx, dy)
    elif heuristic == "chebyshev":
        x1, y1 = p1
        x2, y2 = p2
        cost = max(abs(x1 - x2), abs(y1 - y2))
    return cost

def neighbourr(grid):
    neighbour = [[]for col in range(len(grid)) for row in range(len(grid))]
    count=0
    for i in range(len(grid)):
        for j in range(len(grid)):
            neighbour[count] == []
            if (i > 0 and grid[i - 1][j] != 1):
                neighbour[count].append((i-1,j))
            if (j > 0 and grid[i][j - 1] != 1):
                neighbour[count].append((i,j-1))
            if (i < len(grid) - 1 and grid[i + 1][j] != 1):
                neighbour[count].append((i+1,j))
            if (j < len(grid) - 1 and grid[i][j + 1] != 1):
                neighbour[count].append((i,j+1))
            count+=1
    return neighbour   


def S_E(grid,start,end):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if(grid[x][y]==2):
                start =x,y
            if(grid[x][y]==3):
                end =x,y
       
    return start,end

def short_path(grid, came_from, current):
     goal_path_length = 0
     grid[current[0]][current[1]] = 4
     goal_path_length += 1
     while current in came_from:
         current = came_from[current]
         grid[current[0]][current[1]] = 4
         goal_path_length += 1
     return grid, goal_path_length
 
def a_star(grid,heuristic="manhattan"):
    
    neighbour = neighbourr(grid)

    start,end = S_E(grid,0,0)
    open_set = PriorityQueue()
    visited_cells = 0
    open_set.put((0,start))
    visited_cells += 1
    open_set_his = {start}
    came_from = {}
    
    g_score = [float("inf") for row in grid for spot in row ]
    g_score[start[0]*len(grid[0]) +start[1]] = 0
    f_score = [ float("inf") for row in grid for spot in row ]
    f_score[start[0]*len(grid[0]) +start[1]] = h(start, end)

    step_counter = 0  # Initialize step counter
    start_time = time.time()  # Record start time
    while not open_set.empty():
        current = open_set.get()[1]
        open_set_his.remove(current)
        if current == end:
            grid,goal_path_length = short_path(grid,came_from, end)
            end_time = time.time()  # Record end time
            total_time = end_time - start_time  # Calculate total time
            return True, step_counter, visited_cells, goal_path_length, total_time
        for nei in neighbour[current[0]*len(grid[0]) +current[1]]:
            step_counter += 1  # Increment step counter for each explored neighbor
            temp_g_score = g_score[current[0]*len(grid[0]) +current[1]] + 1
            if temp_g_score < g_score[nei[0]*len(grid[0]) +nei[1]]:
                came_from[nei] = current
                g_score[nei[0]*len(grid[0]) +nei[1]] = temp_g_score
                f_score[nei[0]*len(grid[0]) +nei[1]] = temp_g_score + h(nei, end)
                if nei not in open_set_his:
                    open_set.put((f_score[nei[0]*len(grid[0]) +nei[1]],  nei))
                    visited_cells += 1
                    open_set_his.add(nei)
                    grid[nei[0]][nei[1]] = 5
                    pygame.display.update()
                    time.sleep(0.01)
    
        if current != start:
            grid[current[0]][current[1]] = 6
            pygame.display.update()
            time.sleep(0.01)
        

    end_time = time.time()  # Record end time if no path is found
    total_time = end_time - start_time  # Calculate total time
    return False, step_counter, visited_cells, goal_path_length, total_time







