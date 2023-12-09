import numpy as np

#colors
one = (79, 189, 186)
two = (206, 171, 147)
three = (227, 202, 165)
four = (255, 251, 233)
five = (246, 137, 137)
six = (255, 0, 0)
seven = (0, 255, 0)

def savegrid(grid):
    np.savetxt(r"./Downloads/Maze-Pathfinding-main/maze.txt",grid)

def loadgrid(index):
    if(index ==0):
        grid = np.loadtxt(r"maze.txt").tolist()
    elif(index ==1):
        grid = np.loadtxt(r"Maze1\maze.txt").tolist()
    elif(index ==2):
        grid = np.loadtxt(r"Maze2\maze.txt").tolist()
    elif(index ==3):
        grid = np.loadtxt(r"Maze3\maze.txt").tolist()
    elif(index ==4):
        grid = np.loadtxt(r"Maze4\maze.txt").tolist()
    elif(index ==5):
        grid = np.loadtxt(r"Maze5\maze.txt").tolist()
    return grid