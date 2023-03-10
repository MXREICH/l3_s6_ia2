class Node:
    def __init__(self, value=1000, children=None):
        self.value = value
        self.children = children

    def getSucc(self):
        assert self is not None
        return self.children

    def isLeaf(self):
        assert self is not None
        return len(self.children) == 0

    def nodeValue(self):
        assert self is not None
        return self.value
