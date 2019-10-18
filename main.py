# Blockworld Tile Puzzle
# Python 3.7.4
import numpy as np
import pandas as pd
import random
from search import bfs, dfs, ids, astar
from node import Node


# design interface
def createPlayerStartGoal(size):
    if size == "default":  # default setup in the assignment
        player = ((3, 3))
        start = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 3, 0]])
        goal = np.array([[0, 0, 0, 0], [0, 1, 0, 0], [0, 2, 0, 0], [0, 3, 0, 0]])
    elif size == "test1":
        player = ((1, 1))
        start = np.array([[0, 0, 0], [1, 0, 0], [0, 2, 0]])
        goal = np.array([[0, 0, 0], [0, 1, 0], [0, 2, 0]])
    else:  # random setup
        size = int(size)
        start, goal = np.zeros(size * size), np.zeros(size * size)
        posStart = random.sample(range(size*size-1), k=size-1)    # random size-1 positions for blocks, bottom-right corner is player
        posGoal = range(1+size, size*size, size)    # goal size-1 positions must be at 2nd column
        start[posStart] = range(1, size)     # put them into the puzzle
        goal[posGoal] = range(1, size)  # put them in to the puzzle
        player = ((size-1, size-1))
        start = np.reshape(start, (size, size))
        goal = np.reshape(goal, (size, size))
    return player, start, goal


def main():
    boardSize = 3
    playerStart, startState, goalState = createPlayerStartGoal("test1")
    print("Start")
    print(startState)
    print("Goal")
    print(goalState)
    print("Start BFS")
    solution = bfs(playerStart, startState, goalState)
    if solution:
        print("Solution Found: ", solution)
    else:
        print("No Solution")
    return


if __name__ == "__main__":
    main()
