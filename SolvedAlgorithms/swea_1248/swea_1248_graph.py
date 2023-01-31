import sys
sys.stdin = open("SolvedAlgorithms\swea_1248\swea_1248_input.txt", "r")

class Graph():
    def __init__(self, node):
        self.dic = {idx : [] for idx in range(1, node+1)}

    def build_graph(self, lst):
        while lst:
            key = lst.pop(0)
            value = lst.pop(0)
            self.dic[key] += [value]

    def commen_graph(self, val1, val2):
        lst1 = self.traverse_graph(val1)
        lst2 = self.traverse_graph(val2)
        while lst1[-1] == lst2[-1] and lst1[-2] == lst2[-2]:
            lst1.pop()
            lst2.pop()
        return lst1[-1]

    def traverse_graph(self, val):
        tmp_lst = [val]
        check = 1
        while check:
            check -= 1
            for item in self.dic.items():
                for branch in item[1]:
                    if branch == tmp_lst[-1]:
                        tmp_lst.append(item[0])
                        check += 1
        return tmp_lst

    def size(self, value):
        tmp = 1
        if not self.dic[value]:
            return tmp
        else:
            for child_branch in self.dic[value]:
                tmp += self.size(child_branch)
            return tmp

def solve(test_case):
    N, E , val1, val2 = map(int, input().split())
    data_lst = list(map(int, input().split()))
    graph1 = Graph(N)
    graph1.build_graph(data_lst)
    commen_root = graph1.commen_graph(val1, val2)
    print(f'#{test_case} {commen_root} {graph1.size(commen_root)}')


T = int(input())
for test_case in range(1, T + 1):
    solve(test_case)