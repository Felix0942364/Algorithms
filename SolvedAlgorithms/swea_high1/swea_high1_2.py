import sys
sys.stdin = open("github\Algorithms\SolvedAlgorithms\swea_high1\swea_hight1_input.txt", "r")

def add_dict(dct, occ, val, case):
    occ = tuple(occ)
    if occ in dct:
        if val in dct[occ]:
            dct[occ][val] += case
        else:
            dct[occ][val] = case
    else:
        dct[occ] = {val : case}

def solve(num, weights):
    occupation, value, cases = (0,), 0, 1
    queue = {(occupation) : {value : cases}}
    for cycle in range(num):
        cycle_queue = dict()
        for occu, val_case in queue.items():
            for val, case in val_case.items():
                for j in range(num):
                    if j+1 in occu:
                        continue
                    else:
                        add_dict(cycle_queue, sorted(occu+(j+1,)), val+weights[j], case)
                        if val - weights[j] >= 0:
                            add_dict(cycle_queue, sorted(occu+(j+1,)), val-weights[j], case)
        queue = cycle_queue
    print(f'#{test_case} {sum(queue[tuple(range(num+1))].values())}')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    weights = list(map(int,input().split()))
    solve(N, weights)