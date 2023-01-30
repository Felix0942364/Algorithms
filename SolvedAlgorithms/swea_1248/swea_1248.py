import sys
sys.stdin = open("SolvedAlgorithms\swea_1248\swea_1248_input.txt", "r")

class TreeNode:
    def __init__(self, key_):
        self.key = key_
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{(self.key, self.parent, self.left, self.right)}'

    def build_tree(self, lst):
        while lst:
            parent_node = lst.pop(0)
            child_node = lst.pop(0)
            self.insert(parent_node, child_node)
        return self

    def insert(self, parent, child):
        tmp = self.search(parent)
        print(tmp)
        if not tmp.left:
            tmp.left = TreeNode(child)
            tmp.left.parent = parent
        elif not tmp.right:
            tmp.right = TreeNode(child)
            tmp.right.parent = parent

    def search(self, key):
        if self.key == key:
            return self
        else:
            if self.left is not None:
                left = self.left.search(key)
                if left:
                    return left
            if self.right is not None:
                right = self.right.search(key)
                if right:
                    return right
        return None

    def common_ancestor(self, key1, key2):
        def root_search(root, key, stack):
            tmp = root.search(key)
            stack.append(tmp.parent)
            tmp = root.search(tmp.parent)
            while tmp:
                stack.append(tmp.parent)
                tmp = root.search(tmp.parent)

        stack1, stack2 = [], []
        root_search(self, key1, stack1)
        root_search(self, key2, stack2)
        while stack1[-1] == stack2[-1]:
            stack1.pop()
            stack2.pop()
            if len(stack1)==1 or len(stack2) ==1:
                break
        return len(stack1)+1 + len(stack2)+1

def solve(test_case):
    N, E , key1, key2 = map(int, input().split())
    tree_data = list(map(int, input().split()))
    root = TreeNode(tree_data[0])
    root.build_tree(tree_data)
    print(f'#{test_case} {root.common_ancestor(key1, key2)}')

T = int(input())
for test_case in range(1, T + 1):
    solve(test_case)