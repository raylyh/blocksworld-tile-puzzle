# Blocksworld Tile Puzzle
> MSc Coursework Project in COMP6231 Foundations of AI

This project explores the optimality and computational complexity of different search algorithms in a simple puzzle.

An ‘agent’ moves in a simulated NxN grid world with the goal of building towers of blocks. Each grid space contains either a ‘tile’ or the agent. Some tiles have letters on them – these are the ‘blocks’. All the other tiles are white. The agent moves up/down/left/right (except where borders prevent it). As the agent moves, the tile that they move onto slides under them into the position that they just came from (see 8-puzzle). The goal is to build a tower, with these exact blocks in these exact positions as shown in [here](blocksworld_tile_puzzle.pdf). The position of the agent at the end doesn’t matter.

## Running
Source code located in the `src` directory.

In the `src` directory,
```
python main.py
```
to run all the search algorithms given the initial board state and player position.


### Configurations
In `main.py`, variables `boardSize` and `functions` are specified to determine the size of the puzzle and the search algorithms used to find a solution

`boardSize` should be a string input for 3 specific cases or an integer:
- `"default"`: setup as specified in the assignment
- `"test1"`: 3x3 board with an optimal solution depth of 3
- `"test2"`: 4x4 board with an optimal solution depth of 14
- integer: nxn board with player starting at bottom right corner

### Methods
`functions`: a list including the following search algorithms 
- `bfs`: Breadth-first Search
- `dfs`: Depth-first Search
- `ids`: Iterative Deepening Search
- `astar`: A* Search

### Expected Output
The output shows the initial board state and the goal state, and starts the search algorithms given in `functions`. If a solution is found, all the intermediate steps are printed as board states with action taken except for depth-first search (output compressed to only actions taken).

### Environment
Python 3.6
