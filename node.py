class Node:
    def __init__(self, pos, state, parent=None, action=None, cost=0, depth=0, hn=0):
        self.pos = pos
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.hn = hn
        self.depth = depth
        self.boardSize = state.shape[0]

    def __lt__(self, other):
        return self.cost + self.hn < other.cost + other.hn

    def __str__(self):
        stateWithPlayerPos = self.state.copy().astype(object)
        stateWithPlayerPos[self.pos[0], self.pos[1]] = 'X'
        return f"Player Position: {self.pos}\nCurrent Depth: {self.depth}\nAction: {self.action}\nState:\n{stateWithPlayerPos}\n"
