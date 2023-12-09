import time
import pygame
from queue import PriorityQueue

def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def neighbourr(grid,neighbour):
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


def S_E(grid,start,end):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if(grid[x][y]==2):
                start =x,y
            if(grid[x][y]==3):
                end =x,y
       
    return start,end

def short_path(grid, came_from, current):
     grid[current[0]][current[1]] = 4
     while current in came_from:
         current = came_from[current]
         grid[current[0]][current[1]] = 4
 
def a_star(grid, neighbour):
    
    neighbourr(grid, neighbour)
    
    start,end = S_E(grid,0,0)
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    open_set_his = {start}
    came_from = {}
    
    g_score = [float("inf") for row in grid for spot in row ]
    g_score[start[0]*len(grid[0]) +start[1]] = 0
    f_score = [ float("inf") for row in grid for spot in row ]
    f_score[start[0]*len(grid[0]) +start[1]] = h(start, end)

    
    while not open_set.empty():
        current = open_set.get()[2]
        open_set_his.remove(current)
        if current == end:
            print("finishing")
            short_path(grid, came_from, end)
            return True
        for nei in neighbour[current[0]*len(grid[0]) +current[1]]:
            temp_g_score = g_score[current[0]*len(grid[0]) +current[1]] + 1
            if temp_g_score < g_score[nei[0]*len(grid[0]) +nei[1]]:
                came_from[nei] = current
                g_score[nei[0]*len(grid[0]) +nei[1]] = temp_g_score
                f_score[nei[0]*len(grid[0]) +nei[1]] = temp_g_score + h(nei, end)
                if nei not in open_set_his:
                    count += 1
                    open_set.put((f_score[nei[0]*len(grid[0]) +nei[1]], count, nei))
                    open_set_his.add(nei)
                    grid[nei[0]][nei[1]] = 5
                    pygame.display.update()
                    time.sleep(0.01)
    
        if current != start:
            grid[current[0]][current[1]] = 6
            pygame.display.update()
            time.sleep(0.01)
        

    return False







