import sys
sys.stdin = open("SolvedAlgorithms\swea_1247\swea_1247_input.txt", "r")

def coordinate_organizer(coordinate_lst):
    def x_y_pop(lst):
        return lst.pop(0), lst.pop(0)   

    tmp_list = []
    while coordinate_lst:
        tmp_list.append(x_y_pop(coordinate_lst))
    return tmp_list

def build_dict(coordinates):
    coordinate_lst = coordinate_organizer(coordinates)
    tmp_dict = dict()
    idx = 0
    for x1, y1 in coordinate_lst:
        for x2, y2 in coordinate_lst:
            if not idx in tmp_dict.keys():
                tmp_dict[idx] = []
            tmp_dict[idx] += [abs(x2 - x1) + abs(y2 - y1)]
        idx += 1
    return tmp_dict

def build_cases(people):
    lst = [[]]
    for iter in range(people):
        tmp = []
        for case in lst:
            for idx in range(people):
                if idx in case:
                    continue
                tmp.append(case + [idx])
        lst = tmp[:]
    return lst
    
def find_min_path(people, coordinates):
    order_cases = build_cases(people)
    case_dict = build_dict(coordinates)
    res = 200 * people
    while order_cases:
        case = order_cases.pop()
        order = [0] + [x+2 for x in case] + [1] 
        tmp = 0
        for idx in range(len(order)-1):
            tmp += case_dict[order[idx]][order[idx+1]]
        if tmp < res:
            res = tmp
    return res
    
# shell to call input
def solve(test_case):
    people = int(input())
    coordinates = list(map(int, input().split()))
    print(f'#{test_case} {find_min_path(people, coordinates)}')

T = int(input())
for test_case in range(1, T + 1):
    solve(test_case)