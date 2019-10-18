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
        return "Player Position: {}\nState:\n{}\n".format(self.pos, self.state) + textwrap.indent("Parent:\n{}".format(self.parent), "   ")
