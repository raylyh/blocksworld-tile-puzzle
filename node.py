class Node:
    def __init__(self, player, state, parent=None, action=None, cost=0, depth=0):
        self.player = player
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth

    def __repr__(self):
        return "Player: %s\n State: \n%s\n Parent: \n%s\n " % (self.player, self.state, self.parent)
