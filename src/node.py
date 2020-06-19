# define a node class to represent the board state

class Node:
    def __init__(self, pos, state, parent=None, action=None, cost=0, depth=0, hn=0):
        """ params
        pos: current position: Tuple(row, col)
        state: current board state: numpy.array
        parent: parent node: Node
        action: previous action: Direction(Enum) 
        cost: cost so far to reach this state: int
        hn: estimated cost to reach the goal: int
        depth: depth of the state: int
        boardSize: length of board size: int
        """
        self.pos = pos
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.hn = hn
        self.depth = depth
        self.boardSize = state.shape[0]

    def __lt__(self, other):
        # comparison between the total cost of two nodes: used in astar search
        return self.cost + self.hn < other.cost + other.hn

    def __str__(self):
        stateWithPlayerPos = self.state.copy().astype(object)
        stateWithPlayerPos[self.pos[0], self.pos[1]] = 'X'
        return f"Player Position: {self.pos}\nCurrent Depth: {self.depth}\nAction: {self.action}\nState:\n{stateWithPlayerPos}\n"
