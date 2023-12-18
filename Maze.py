from itertools import count
import pygame
import os
import sys
import time

from DFS import *
from grid import *
from A_star import *
from BFS import *
from greedy import *
pygame.init()

size = (706, 706)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MAZE")

width = 20
height = 20
margin = 2

grid = [[0 for x in range(33)] for y in range(33)]

found = False
done = False


clock = pygame.time.Clock()


 
while not done:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                    print("Exit")
                    pygame.quit()
                    
             if event.key == pygame.K_s:
                 print("Saving Maze")
                 savegrid(grid)
                 
             if event.key == pygame.K_l:
                 print("Loading Maze")
                 grid = loadgrid(0)
                 
             if event.key == pygame.K_f:
                 print("Filling Maze")
                 grid = [[1 for x in range(33)] for y in range(33)]
                 
             if event.key == pygame.K_1:
                 print("Loading Maze 1")
                 grid = loadgrid(1)
                 
             if event.key == pygame.K_2:
                 print("Loading Maze 2")
                 grid = loadgrid(2)
             if event.key == pygame.K_3:
                 print("Loading Maze 3")
                 grid = loadgrid(3)
             if event.key == pygame.K_4:
                 print("Loading Maze 4")
                 grid = loadgrid(4)
             if event.key == pygame.K_5:
                 print("Loading Maze 5")
                 grid = loadgrid(5)
             if event.key == pygame.K_RETURN:
                if((sum(x.count(2) for x in grid)) == 1):
                    print("Solving")
                    # bfs_solve()
                    # # a_star(grid)
                    a_star(grid)
                    # start, end = S_E(grid, 0, 0)
                    # visited = [[False for _ in range(33)] for _ in range(33)]
                    # if(dfs_solve(grid, start, visited)):
                    #     print("Found")
                    # else:
                    #     print("Not Found")
             if event.key == pygame.K_r:

                grid = [[0 for x in range(33)] for y in range(33)]
        if pygame.mouse.get_pressed()[2]:
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            if((sum(x.count(2) for x in grid)) < 1 or (sum(x.count(3) for x in grid)) < 1):
                if((sum(x.count(2) for x in grid)) == 0):
                    if(grid[row][column] == 2):
                        grid[row][column] = 0
                    elif(grid[row][column] == 3):
                        grid[row][column] = 0
                    else:
                        grid[row][column]  = 2
                else:
                    if(grid[row][column] == 3):
                        grid[row][column] = 0
                    elif(grid[row][column] == 2):
                        grid[row][column] = 0
                    else:
                        grid[row][column]  = 3
            else:
                if(grid[row][column] == 2):
                    grid[row][column] = 0
                if(grid[row][column] == 3):
                    grid[row][column] = 0
                if(grid[row][column] == 1):
                    grid[row][column] = 0
        if pygame.mouse.get_pressed()[0]:
            # if(event.button == 1):
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            print("left click")
            grid[row][column] = 1
        
                
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    screen.fill(two)
    for row in range(33):
        for column in range(33):
            if grid[row][column] == 1:
                color = three
            elif grid[row][column] == 2:
                color = one
            elif grid[row][column] == 3:
                color = five
            elif grid[row][column] == 4:
                color = one
            elif grid[row][column] == 5:
                color = six
            elif grid[row][column] == 6:
                color = seven
            else:
                color = four
            pygame.draw.rect(screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
