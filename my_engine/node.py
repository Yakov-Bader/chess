class Node:

    def __init__(self, move, val):
        self._children = []
        self._val = val
        self._father= None
        self._children_max = -100000
        self._children_min = 100000
        self._move = move

    def add_child(self, child):
        self._children.append(child)
        child.father = self

    @property
    def father(self):
        return self._father

    @father.setter
    def father(self, father):
        self._father = father

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @property
    def children_max(self):
        return self._children_max

    @children_max.setter
    def children_max(self, children_max):
        self._children_max = children_max

    @property
    def children_min(self):
        return self._children_min

    @children_min.setter
    def children_min(self, children_min):
        self._children_min = children_min

    @property
    def move(self):
        return self._move

    @property
    def children(self):
        return self._children

