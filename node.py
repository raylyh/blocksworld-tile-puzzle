import textwrap


class Node:
    def __init__(self, pos, state, parent=None, action=None, cost=0, depth=0):
        self.pos = pos
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth
        self.boardSize = state.shape[0]

    def __str__(self):
        stateWithPlayerPos = self.state.copy().astype(object)
        stateWithPlayerPos[self.pos[0], self.pos[1]] = 'X'
        return "Player Position: {}\nAction: {}\nState:\n{}\nParent:".format(self.pos, self.action, stateWithPlayerPos) + textwrap.indent("\n{}".format(self.parent), " ")
