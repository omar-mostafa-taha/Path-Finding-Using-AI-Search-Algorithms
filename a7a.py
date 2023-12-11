from tkinter import * 
from itertools import count
import pygame
import numpy as np
from queue import PriorityQueue
import queue
import os
import sys
grid = [[0 for x in range(33)] for y in range(33)]
neighbour = []



def run_maze_game(num_algorithms, num_mazes):
    global grid, neighbour,algorithms
    #colors
    one = (79, 189, 186)
    two = (206, 171, 147)
    three = (227, 202, 165)
    four = (255, 251, 233)
    five = (246, 137, 137)
    six = (255, 0, 0)
    seven = (0, 255, 0)


    
    pygame.init()
    
    size = (706, 706)
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("MAZE")
    
    width = 20
    height = 20
    margin = 2
    
    maze_loaded = False
    done = False
    clock = pygame.time.Clock()
    found = False
    
    def loadgrid(index):
        global  grid  
        if(index ==1):
            grid = np.loadtxt(r'./Downloads/Maze-Pathfinding-main/Maze1/maze.txt').tolist()
        elif(index ==2):
            grid = np.loadtxt(r'./Downloads/Maze-Pathfinding-main/Maze2/maze.txt').tolist()
        elif(index ==3):
            grid = np.loadtxt(r'./Downloads/Maze-Pathfinding-main/Maze3/maze.txt').tolist()
        elif(index ==4):
            grid = np.loadtxt(r'./Downloads/Maze-Pathfinding-main/Maze4/maze.txt').tolist()
        elif(index ==5):
            grid = np.loadtxt(r'./Downloads/Maze-Pathfinding-main/Maze5/maze.txt').tolist()
                
    def neighbourr():
        global grid,neighbour
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
                
                
    def h(p1, p2):
    	x1, y1 = p1
    	x2, y2 = p2
    	return abs(x1 - x2) + abs(y1 - y2)
    
    def S_E(maze,start,end):
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if(grid[x][y]==2):
                    start =x,y
                if(grid[x][y]==3):
                    end =x,y
           
        return start,end
    
    def short_path(came_from, current):
         grid[current[0]][current[1]] = 4
         while current in came_from:
             current = came_from[current]
             grid[current[0]][current[1]] = 4
            
        
            
    def a_star():
        global grid, neighbour
        neighbourr()
    
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
                short_path(came_from, end)
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
                        # grid[nei[0]][nei[1]] = 5
                        # pygame.display.update()
                        # time.sleep(0.01)
        
            # if current != start:
            #     grid[current[0]][current[1]] = 6
            #     pygame.display.update()
            #     time.sleep(0.01)
            
    
        return False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if not maze_loaded:
                loadgrid(num_mazes)
                print(f"Loading Maze")
                maze_loaded = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if num_algorithms == 1:
                        print("Solving using A*")
                        a_star()  # Run A* algorithm
                   # elif num_algorithms == 2:
                    #    print("Solving using Gready")
                     #   gready(grid, neighbour)  # Run Gready algorithm
                    #elif num_algorithms == 3:
                     #   print("Solving using BFS")
                      #  bfs(grid, neighbour)  # Run BFS algorithm
                    #elif num_algorithms == 4:
                     #   print("Solving using DFS")
                      #  dfs(grid, neighbour)
                
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
        

def get_values():
    try:
        num_algo = int(entry_algorithms.get())
        num_maze = int(entry_mazes.get())

        if num_algo <= 0 and num_algo > 4:
            raise ValueError
        if num_algo <= 0 and num_algo > 5:
            raise ValueError
        run_maze_game(num_algo, num_maze)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers greater than zero.")


# Create the main window
root = Tk()
root.title("Maze Game")  # Set the title of the window


# Set window size to 800x600 and center it on the screen
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#set the title inside the window 
welcome = Frame(root)
welcome.place(relx=0.5, rely=0.1, anchor="center")
welcome_lable = Label(welcome, text="Welcome To Our Maze" , font=("Arial", 24))
welcome_lable.grid(row=0, column=0, pady=5)  



# Create a frame to hold the widgets
frame = Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create labels and entry widgets for number of algorithms and mazes
label_algorithms = Label(frame, text="Enter the number of algorithms:")
label_algorithms.grid(row=0, column=0, pady=5)  # Use grid to place the label

entry_algorithms = Entry(frame)
entry_algorithms.grid(row=0, column=1, pady=5)  # Use grid to place the entry field

#set the name of algorithms 
name_of_algorithms = Label(frame, text="1 - A_star, 2 - Gready, 3 - BFS, 4 - DFS")
name_of_algorithms.grid(row=0, column=2, pady=5)  # Use grid to place the label

label_mazes = Label(frame, text="Enter the number of mazes:")
label_mazes.grid(row=1, column=0, pady=5)  # Use grid to place the label

entry_mazes = Entry(frame)
entry_mazes.grid(row=1, column=1, pady=5)  # Use grid to place the entry field

#set the number of mazes
name_of_algorithms = Label(frame, text="From 1 to 5")
name_of_algorithms.grid(row=1, column=2, pady=5)  # Use grid to place the label

#creat a frame for sumbit the answers 
submit = Frame(root)
submit.place(relx=0.5, rely=0.7, anchor="center")
# Button to submit the values
submit_button = Button(submit, text="Submit", command=get_values, width=10, height=2)
submit_button.grid(row=0, column=0, columnspan=2, pady=10)  # Use grid to place the button



root.mainloop()
