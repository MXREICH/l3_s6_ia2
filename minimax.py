class Pruning:
    def __init__(self, mastermind_tree):
        self.game_tree = mastermind_tree  # GameTree
        self.root = mastermind_tree.root  # GameNode
        return

    def alpha_beta_search(self, node):
        infinity = float('inf')
        best_val = -infinity
        beta = infinity

        successors = node.getSucc()
        best_state = None
        for state in successors:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        print("AlphaBeta:  Utility Value of Root Node: = " + str(best_val))
        print("AlphaBeta:  Best State is: " + best_state.Name)
        return best_state

    def max_value(self, node, alpha, beta):
        print("AlphaBeta–>MAX: Visited Node :: " + node.Name)
        if node.isLeaf():
            return node.nodeValue()
        infinity = float('inf')
        value = -infinity

        successors = node.getSucc()
        for state in successors:
            value = max(value, self.min_value(state, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def min_value(self, node, alpha, beta):
        print("AlphaBeta–>MIN: Visited Node :: " + node.Name)
        if node.isLeaf():
            return node.nodeValue()
        infinity = float('inf')
        value = infinity

        successors = node.getSucc()
        for state in successors:
            value = min(value, self.max_value(state, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)

        return value
