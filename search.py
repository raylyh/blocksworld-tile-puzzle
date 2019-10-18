# Search Algorithms
import numpy as np
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


def expand(node):
    # successors = empty set
    successors = []
    # Find possible action

    # for each eaction, result in successor_function(node) do
    # s = new node
    # successors += s
    print(successors)
    return successors


def bfs(player, start, goal):
    # fringe = insert(makeNode(initial-state))
    fringe = [Node(player, start)]
    # loop
    TIME = 0
    while True:
        if TIME == 10:
            break
        print("Time Complexity: ", TIME)
        # if there are no candidates for expansion then return failure
        if not fringe:
            return 0
        # choose a leaf node for expansion according to strategy
        currentNode = fringe.pop(0)
        TIME += 1
        print("Current Node: ", currentNode)
        # if the node contains a goal state then return the corresponding solution
        # else expand the node and add the resulting nodes to the search tree
        if np.array_equal(currentNode.state, goal):
            print("Goal Found!")
            return currentNode
        else:
            # new successors go at end of fringe (FIFO)
            fringe += expand(currentNode)

    return 0


def dfs():
    return 2


def ids():
    return 3


def astar():
    return 4
