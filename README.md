# Blocksworld Tile Puzzle

## Description
AI Coursework assignment in COMP6231 Foundations of AI

An ‘agent’ moves in a simulated NxN grid world with the goal of building towers of blocks. Each grid space contains either a ‘tile’ or the agent. Some tiles have letters on them – these are the ‘blocks’. All the other tiles are white. The agent moves up/down/left/right (except where borders prevent it). As the agent moves, the tile that they move onto slides under them into the position that they just came from (see 8-puzzle). The goal is to build a tower, with these exact blocks in these exact positions as shown in [here](blocksworld_tile_puzzle.pdf). The position of the agent at the end doesn’t matter.

## Methods
- Breadth-first Search
- Depth-first Search
- Iterative Deepening Search
- A* Search

## Environment
Python 3.6
