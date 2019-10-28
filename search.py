# Search Algorithms
import numpy as np
import random
from operator import add
from enum import Enum
from node import Node
# Tree Search Idea
"""
function tree_search(problem, strategy) returns a solution, or failure
initialize the search tree using the initial state of problem
loop do
    if there are no candidates for expansion then return failure
    choose a leaf node for expansion according to strategy
    if the node contains a goal state then return the corresponding solution
    else expand the node and add the resulting nodes to the search tree
"""

class Direction(Enum):
    UP = [-1, 0]
    DOWN = [1, 0]
    LEFT = [0, -1]
    RIGHT = [0, 1]

# print(random.sample(Direction, 1))

def expand(currentNode, isRandom=False):
    # successors = empty set
    successors = []
    # Find possible action
    if isRandom:
        randomActions = random.sample(list(Direction), 4)

    for ind, action in enumerate(Direction):
        if isRandom:
            action = randomActions[ind]
        newPos = list(map(add, currentNode.pos, action.value))
        # check out of bound
        if -1 in newPos or currentNode.boardSize in newPos:
            continue
        else:
            # Update the board state
            newState = np.copy(currentNode.state)
            newState[currentNode.pos[0], currentNode.pos[1]], newState[newPos[0], newPos[1]] = newState[newPos[0], newPos[1]], newState[currentNode.pos[0], currentNode.pos[1]]
            # Save the node
            s = Node(newPos, newState, currentNode, action, currentNode.cost+1, currentNode.depth+1)
            successors.append(s)
    # print("SUCCESSORS")
    # print(successors)
    return successors


def bfs(playerPos, startState, goalState, maxNodes=500000):
    # TIME = total number of nodes generated
    TIME = 0
    # fringe = insert(makeNode(initial-state))
    fringe = [Node(playerPos, startState)]
    TIME += 1
    # loop
    while True:
        # Terminate Loop if too long
        if TIME > maxNodes:
            return 0, TIME
        # if there are no candidates for expansion then return failure
        if not fringe:
            return 0, TIME
        # choose a leaf node for expansion according to strategy
        currentNode = fringe.pop(0)
        # print("Current Node: ")
        # print(currentNode)
        # if the node contains a goal state then return the corresponding solution
        # else expand the node and add the resulting nodes to the search tree
        if (currentNode.state == goalState).all():
            print("Goal Found!")
            return currentNode, TIME
        else:
            # new successors go at end of fringe (FIFO)
            successors = expand(currentNode)
            fringe += successors
            TIME += len(successors)


def dfs(playerPos, startState, goalState, currentDepth=np.inf):
    # TIME = total number of nodes generated
    TIME = 0
    # fringe = insert(makeNode(initial-state))
    fringe = [Node(playerPos, startState)]
    TIME += 1
    # loop
    while True:
        # if there are no candidates for expansion then return failure
        if not fringe:
            return 0, TIME
        # choose a leaf node for expansion according to strategy
        currentNode = fringe.pop(0)
        # print("Current Node: ")
        # print(currentNode)
        # if the node contains a goal state then return the corresponding solution
        # else expand the node and add the resulting nodes to the search tree
        if (currentNode.state == goalState).all():
            print("Goal Found!")
            return currentNode, TIME
        else:
            # new successors go at front of fringe (LIFO)
            if currentNode.depth < currentDepth:
                successors = expand(currentNode, isRandom=True)
                fringe = successors + fringe
                TIME += len(successors)


def ids(playerPos, startState, goalState):
    # TIME = total number of nodes generated
    TIME = 0
    # Start from Depth 0
    DEPTH = 0
    while True:
        result, time = dfs(playerPos, startState, goalState, currentDepth=DEPTH)
        print("Depth Limited Search: At Depth: {}, Nodes Generated: {}".format(DEPTH, time))
        TIME += time
        if result:
            return result, TIME
        else:
            DEPTH += 1


def astar():
    return 4
