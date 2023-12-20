from tkinter import * 
from itertools import count
from tkinter import messagebox
import pygame
import numpy as np
from queue import PriorityQueue
import queue
import os
import sys
from DFS import *
from grid import *
from A_star import *
from BFS import *
from greedy import *
from Iterative_DFS import *



def run_maze_game(num_algorithms, num_mazes):
    
    grid = loadgrid(num_mazes)   
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
                        a_star(grid)  # Run A* algorithm
                    elif num_algorithms == 2:
                        print("Solving using Gready")
                        greedy(grid)  # Run Gready algorithm
                    elif num_algorithms == 3:
                        print("Solving using BFS")
                        bfs_solve(grid)  # Run BFS algorithm
                    elif num_algorithms == 4:
                        print("Solving using DFS")
                        dfs(grid)
                    elif num_algorithms == 5:
                        print("Solving using Iterative DFS")
                        iter_dfs(grid)    
                
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

        if (num_algo <= 0 or num_algo > 5) or (num_maze <= 0 or num_maze > 5):
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
name_of_algorithms = Label(frame, text="1 - A_star, 2 - Gready, 3 - BFS, 4 - DFS , 5 - iterative DFS" )
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
