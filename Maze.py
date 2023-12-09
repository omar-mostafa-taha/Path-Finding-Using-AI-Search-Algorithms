from itertools import count
import pygame

import queue
import os
import sys
import time

from grid import *
from A_star import *

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
neighbour=[]

clock = pygame.time.Clock()



def bfs_shortestpath(maze, path=""):
    global grid
    i,j=startp(maze,0,0)
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                
                grid[j][i] = 4
                
def startp(maze,i,j):
    for x in range(len(maze[0])):
        try:
            i =(maze[x].index(2))
            j = x
            print(j)
            return i,j
        except:
            pass

def bfs(maze, moves,i,j):
    global found
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == 1.0):
            return False
        if maze[j][i] == 3:
            print("Found: " + moves)
            bfs_shortestpath(maze, moves)
            found =True
            return True
            break
    return True


def bfs_solve():
    global grid
    nums= queue.Queue()
    nums.put("")
    add = ""
    i,ii =startp(grid,0,0)
    while found != True: 
        add = nums.get()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if bfs(grid, put,i,ii):
                nums.put(put)
            if(found == True):
                break
            
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
                    a_star(grid, neighbour)
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
