# Blockworld Tile Puzzle
# Python 3.7.4
import numpy as np
import random
from search import bfs, dfs, ids, astar


# create the start position, start state, and goal state
def createPlayerStartGoal(size):
    # default setup in the assignment
    if size == "default":
        playerPos = [3, 3]
        start = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 3, 0]])
        goal = np.array([[0, 0, 0, 0], [0, 1, 0, 0], [0, 2, 0, 0], [0, 3, 0, 0]])
    # test for a smaller boardsize and depth solution
    elif size == "test1":
        playerPos = [2, 2]
        start = np.array([[0, 0, 0], [1, 0, 0], [0, 2, 0]])
        goal = np.array([[0, 0, 0], [0, 1, 0], [0, 2, 0]])
    elif size == "test2":
        playerPos = [0, 0]
        start = np.array([[0, 0, 0, 2], [0, 0, 0, 0], [0, 1, 0, 0], [0, 3, 0, 0]])
        goal = np.array([[0, 0, 0, 0], [0, 1, 0, 0], [0, 2, 0, 0], [0, 3, 0, 0]])
    else:  # random setup
        size = int(size)
        start, goal = np.zeros(size * size), np.zeros(size * size)
        posStart = random.sample(range(size*size-1), k=size-1)    # random size-1 positions for blocks, bottom-right corner is player
        posGoal = range(1+size, size*size, size)    # goal size-1 positions must be at 2nd column
        start[posStart] = range(1, size)     # put them into the puzzle
        goal[posGoal] = range(1, size)  # put them in to the puzzle
        playerPos = [size-1, size-1]
        start = np.reshape(start, (size, size)).astype(int)
        goal = np.reshape(goal, (size, size)).astype(int)
    return playerPos, start, goal


def main():
    # define the testing board states and the starting position
    boardSize = "test2"
    playerStart, startState, goalState = createPlayerStartGoal(boardSize)
    # Search functions to run
    # Available options: bfs, dfs, ids, astar
    functions = [dfs]
    print("Start")
    print(startState)
    print("Goal")
    print(goalState)
    print(f"Player Position at Start: {playerStart}")
    for func in functions:
        # Run the search algorithm
        print("Start")
        print(startState)
        print("Goal")
        print(goalState)
        print(f"Player Position at Start: {playerStart}")
        print("Start " + str(func.__name__))
        solution, time = func(playerStart, startState, goalState)

        # if solution is found, output the solution's full path
        # else only output the total number of nodes generated
        if solution:
            print("\n****** Solution ******")
            print(f"Total Nodes Generated: {time}")
            print(f"Maximum Depth: {solution.depth}")
            print("\n****** Full Path ******")
            # special case for dfs: Recursion Error since the depth of the
            # solution can be very large so we only print the steps of action
            if func == dfs:
                toPrint = []
                currentNode = solution
                while True:
                    string = currentNode.action.name[0]
                    toPrint.insert(0, string)
                    currentNode = currentNode.parent
                    if currentNode.action is None:
                        break
                print(' '.join(toPrint))
            else:
                toPrint = []
                currentNode = solution
                while True:
                    stateWithPlayerPos = currentNode.state.copy().astype(object)
                    stateWithPlayerPos[currentNode.pos[0], currentNode.pos[1]] = 'X'
                    string = f"Player Position: {currentNode.pos}\nCurrent Depth: {currentNode.depth}\nAction: {currentNode.action}\nState:\n{stateWithPlayerPos}\n"
                    toPrint.insert(0, string)
                    currentNode = currentNode.parent
                    if currentNode is None:
                        break
                print('\n'.join(toPrint))
        else:
            print("****** No Solution ******")
            print("Total Nodes Generated: ", time)
        print("\n\n")
    return

if __name__ == "__main__":
    main()
