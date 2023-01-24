import sys
sys.stdin = open("SolvedAlgorithms\swea_1249\swea_1249_input.txt", "r")

def build_dict(people, coordinates):
    tmp_dict = dict()
    case = [('start', coordinates.pop(0), coordinates.pop(0)), ('end', coordinates.pop(0), coordinates.pop(0))]
    for idx in range(people):
        case.append((idx, coordinates.pop(0), coordinates.pop(0)))
    for key1, x1, y1 in case:
        for key2, x2, y2 in case:
            if not key1 in tmp_dict.keys():
                tmp_dict[key1] = dict()
            if not key2 in tmp_dict[key1].keys():
                tmp_dict[key1][key2] = []
            tmp_dict[key1][key2] = abs(x2 - x1) + abs(y2 - y1)
    return tmp_dict
    
def find_min_path(people, coordinates):
    case_dict = build_dict(people, coordinates)
    res = 200 * people
    value, route = 0, ['start']
    queue = [(value, route)]
    while queue:
        value, route = queue.pop()
        if sorted(route[1:]) == list(range(people)):
            value += case_dict[route[-1]]['end']
            if res > value:
                res = value
            continue
        for idx in range(people):
            if not idx in route:
                if value < res:
                    queue.append((value + case_dict[route[-1]][idx], route + [idx]))
    return res
    
# shell to call input
def solve(test_case):
    people = int(input())
    coordinates = list(map(int, input().split()))
    print(f'#{test_case} {find_min_path(people, coordinates)}')

T = int(input())
T = 10
for test_case in range(1, T + 1):
    solve(test_case)