# Blockworld Tile Puzzle
# Python 3.7.4
import numpy as np
import pandas as pd
import random
from search import bfs, dfs, ids, astar
from node import Node


# design interface
def createStartGoal(size):
    start, goal = np.zeros(size * size), np.zeros(size * size)
    if size == "default":  # default setup in the assignment
        start = np.array([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [1, 2, 3, 0]])
        goal = np.array([[0, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 2, 0, 0],
                         [0, 3, 0, 0]])
    else:  # random setup
        size = int(size)
        posStart = random.sample(range(size*size-1), k=size-1)    # random size-1 positions for blocks, bottom-right corner is player
        posGoal = range(1+size, size*size, size)    # goal size-1 positions must be at 2nd column
        start[posStart] = range(1, size)     # put them into the puzzle
        goal[posGoal] = range(1, size)  # put them in to the puzzle
        start = np.reshape(start, (size, size))
        goal = np.reshape(goal, (size, size))
    return start, goal


def main():
    boardSize = 3
    print(bfs(), dfs(), ids(), astar())
    # keep track of player position (start at bottom-right corner)
    x, y = boardSize-1, boardSize-1
    z = Node(x, y)
    startState, goalState = createStartGoal(boardSize)
    print(startState)
    print(goalState)
    return


if __name__ == "__main__":
    main()
