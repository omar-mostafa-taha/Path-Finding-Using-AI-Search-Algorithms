import time
import pygame
from queue import PriorityQueue
from A_star import neighbourr,S_E,short_path,h


def greedy(grid):
    
    neighbour = neighbourr(grid)   
    start,end = S_E(grid,0,0)
    queue_greed = PriorityQueue()
    queue_greed.put((0, start))
    visited_set = {start}
    visited_list=[]
    visited_list.append(start)
    path = {} 
    f_score = [ float("inf") for row in grid for spot in row ]
    f_score[start[0]*len(grid[0]) +start[1]] = h(start, end)

    
    while not queue_greed.empty():
        current = queue_greed.get()[1]
        visited_set.remove(current)
        if current == end:
            print("finishing")
            grid = short_path(grid, path, end)
            return True       
        for nei in neighbour[current[0]*len(grid[0]) +current[1]]:
                f_score[nei[0]*len(grid[0]) +nei[1]] = h(nei, end)
                if nei not in visited_set and nei not in visited_list:
                        queue_greed.put((f_score[nei[0]*len(grid[0]) +nei[1]], nei))
                        visited_set.add(nei)
                        visited_list.append(nei)
                        path[nei]=current
                        grid[nei[0]][nei[1]] = 5
                        pygame.display.update()
                        time.sleep(0.01)
            
        if current != start:
           grid[current[0]][current[1]] = 6
           pygame.display.update()
           time.sleep(0.01)
        

    return False