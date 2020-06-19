# Search Algorithms
import numpy as np
import random
import bisect
from operator import add
from enum import Enum
from node import Node
"""
Tree Search Idea:
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


def expand(currentNode, isRandom=False):
    # successors = empty set
    # isRandom: used for DFS to randomise the order of the successors
    successors = []
    # Find possible action
    if isRandom:
        randomActions = random.sample(list(Direction), 4)
    for ind, action in enumerate(Direction):
        if isRandom:
            action = randomActions[ind]
        newPos = list(map(add, currentNode.pos, action.value))
        # check if new position is out of bound
        if -1 in newPos or currentNode.boardSize in newPos:
            continue
        else:
            # Update the board state
            newState = np.copy(currentNode.state)
            newState[currentNode.pos[0], currentNode.pos[1]], newState[newPos[0], newPos[1]] = newState[newPos[0], newPos[1]], newState[currentNode.pos[0], currentNode.pos[1]]
            # Save the node
            s = Node(newPos, newState, currentNode, action, currentNode.cost+1, currentNode.depth+1)
            successors.append(s)
    return successors


def bfs(playerPos, startState, goalState, maxNodes=5000000):
    # TIME = total number of nodes generated
    TIME = 0
    fringe = [Node(playerPos, startState)]
    TIME += 1

    while True:
        # print(f"Total Nodes Generated: {TIME}\n")
        # Terminate Loop if too long
        if TIME > maxNodes:
            return 0, TIME
        # if there are no candidates for expansion then return failure
        if not fringe:
            return 0, TIME
        # choose a leaf node for expansion according to strategy
        # print(f"Size of Fringe: {len(fringe)}")
        currentNode = fringe.pop(0)
        # print(f"***Current Selected Node***\n{currentNode}")
        # if the node contains a goal state then return the corresponding solution
        # else expand the node and add the resulting nodes to the search tree
        if (currentNode.state == goalState).all():
            print("Goal Found!")
            return currentNode, TIME
        else:
            # new successors go at end of fringe (FIFO)
            successors = expand(currentNode)
            # print(f"***Successors generated, add to fringe***")
            fringe += successors
            TIME += len(successors)


def dfs(playerPos, startState, goalState, maxDepth=np.inf):
    # TIME = total number of nodes generated
    TIME = 0
    fringe = [Node(playerPos, startState)]
    TIME += 1
    # loop
    while True:
        # print(f"Total Nodes Generated: {TIME}\n")
        # if there are no candidates for expansion then return failure
        if not fringe:
            return 0, TIME
        # choose a leaf node for expansion according to strategy
        # print(f"Size of Fringe: {len(fringe)}")
        currentNode = fringe.pop(0)
        # if the node contains a goal state then return the corresponding solution
        # else expand the node and add the resulting nodes to the search tree
        if (currentNode.state == goalState).all():
            print("Goal Found!")
            return currentNode, TIME
        else:
            # new successors go at front of fringe (LIFO)
            # if current depth is smaller than the maximum depth
            # then expand on the current selected node
            # this if-statement has no effect in DFS
            if currentNode.depth < maxDepth:
                successors = expand(currentNode, isRandom=True)
                # print(f"***Successors generated, add to fringe***")
                fringe = successors + fringe
                TIME += len(successors)
            # else:
                # print("***At the final depth and no expansion of nodes***")


def ids(playerPos, startState, goalState):
    # TIME = total number of nodes generated
    TIME = 0
    # Start from Depth 0
    DEPTH = 0
    while True:
        result, time = dfs(playerPos, startState, goalState, maxDepth=DEPTH)
        print("[[Depth Limited Search: At Depth: {}, Nodes Generated: {}]]\n".format(DEPTH, time))
        TIME += time
        if result:
            return result, TIME
        else:
            DEPTH += 1


def astar(playerPos, startState, goalState):
    # Evaluation Function fn = gn + hn
    # gn = cost so far, hn = estimated cost from n to goal
    # Manhattan Distance / Linear Conflict
    def eval(node):
        hn = 0
        for i in range(1, node.boardSize):  # find the blocks in the puzzle
            xCur, yCur = np.where(node.state == i)
            xGoal, yGoal = np.where(goalState == i)
            hn += abs(xCur - xGoal) + abs(yCur - yGoal)
        return hn

    # TIME = total number of nodes generated
    TIME = 0
    fringe = [Node(playerPos, startState)]
    TIME += 1
    # loop
    while True:
        # print(f"Total Nodes Generated: {TIME}\n")
        # if there are no candidates for expansion then return failure
        if not fringe:
            return 0, TIME
        # choose a leaf node for expansion according to strategy
        # print(f"Size of Fringe: {len(fringe)}")
        # print("[[ NODES IN FRINGE ]] ")
        # for ind, node in enumerate(fringe):
        #     print(f"Node Position in Fringe: {ind+1}, Node g(n): {node.cost}, Node h(n): {node.hn}\nNode Details:\n{node}")
        currentNode = fringe.pop(0)
        # if the node contains a goal state then return the corresponding solution
        # else expand the node and add the resulting nodes to the search tree
        if (currentNode.state == goalState).all():
            print("Goal Found!")
            return currentNode, TIME
        else:
            # order the nodes in fringe in decreasing order of desirability
            # i.e. ascending order of f(n)
            # print(f"***Successors generated, add to fringe***")
            successors = expand(currentNode, isRandom=False)
            for nodes in successors:
                nodes.hn = eval(nodes)
                bisect.insort_left(fringe, nodes)
            # print(f"***Fringe sorted***")
            TIME += len(successors)
