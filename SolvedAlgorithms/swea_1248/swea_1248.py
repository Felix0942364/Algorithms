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
            print('input : ', parent_node, child_node, lst)
            self.insert(parent_node, child_node)
            print(self.key, self.left, self.right)
            if self.left:
                print(self.left, self.left.key, self.left.left, self.left.right)
            if self.right:
                print(self.right, self.right.key, self.right.left, self.right.right)

    def insert(self, parent, child):
        tmp = self.search(parent)
        if not tmp.left:
            tmp.left = Tree(child)
        elif not tmp.right:
            tmp.right = Tree(child)
        self = tmp

    def PrintTree(self):
        print(self.key, end=',')
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()

    def search(self, key_):
        if self.key == key_:
            return self
        else:
            if self.left:
                self.left.search(key_)
            if self.right:
                self.right.search(key_)

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

def solve(test_case):
    node, edge, pos_1, pos_2 = input().split()
    lst = [1, 2, 1, 3, 2, 4, 2, 5, 3, 6, 3, 7]
    tree = Tree(1)
    built_tree = tree.build_tree(lst)

T = int(input())
T = 1
for test_case in range(1, T + 1):
    solve(test_case)