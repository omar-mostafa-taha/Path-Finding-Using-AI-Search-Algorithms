import time
import pygame
from queue import PriorityQueue
from A_star import neighbourr,S_E,short_path,h


def greedy(grid,heuristic="manhattan"):
    
    neighbour = neighbourr(grid)   
    start,end = S_E(grid,0,0)
    queue_greed = PriorityQueue()
    queue_greed.put((0, start))
    set_willbe_visited = {start}
    visited_list=[]
    visited_list.append(start)
    path = {} 
    f_score = [ float("inf") for row in grid for spot in row ]
    f_score[start[0]*len(grid[0]) +start[1]] = h(start, end)

    step_counter = 0  # Initialize step counter
    start_time = time.time()  # Record start time

    while not queue_greed.empty():
        current = queue_greed.get()[1]
        set_willbe_visited.remove(current)
        if current == end:
            print("finishing")
            grid = short_path(grid, path, end)
            end_time = time.time()  # Record end time
            total_time = end_time - start_time  # Calculate total time
            return True, step_counter, total_time       
        for nei in neighbour[current[0]*len(grid[0]) +current[1]]:
                step_counter += 1  # Increment step counter for each explored neighbor
                f_score[nei[0]*len(grid[0]) +nei[1]] = h(nei, end)
                if nei not in  set_willbe_visited and nei not in visited_list:
                        queue_greed.put((f_score[nei[0]*len(grid[0]) +nei[1]], nei))
                        set_willbe_visited.add(nei)
                        visited_list.append(nei)
                        path[nei]=current
                        grid[nei[0]][nei[1]] = 5
                        pygame.display.update()
                        time.sleep(0.01)
            
        if current != start:
           grid[current[0]][current[1]] = 6
           pygame.display.update()
           time.sleep(0.01)
        

    end_time = time.time()  # Record end time if no path is found
    total_time = end_time - start_time  # Calculate total time
    return False, step_counter, total_time


