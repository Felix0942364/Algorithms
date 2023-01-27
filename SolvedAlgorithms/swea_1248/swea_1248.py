import sys
sys.stdin = open("SolvedAlgorithms\swea_1248\swea_1248_input.txt", "r")

class Tree:
    def __init__(self, key_):
        self.key = key_
        self.left = 0
        self.right = 0

    def build_tree(self, lst):
        while lst:
            parent_node = lst.pop(0)
            child_node = lst.pop(0)
            self.insert(parent_node, child_node)

    def insert(self, parent, child):
        tmp = self.search(parent)
        if not tmp.left:
            tmp.left = Tree(child)
        elif not tmp.right:
            tmp.right = Tree(child)
        self = tmp

    def search(self, num):
        if self.key == num:
            return self
        else:
            if self.left:
                self.left.search(num)
            if self.right:
                self.right.search(num)

def solve():
    lst = [1, 2, 1, 3, 2, 4, 2, 5, 3, 6, 3, 7]
    tree = Tree(1)
    built_tree = tree.build_tree(lst)

solve()

