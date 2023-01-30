import sys
sys.stdin = open("SolvedAlgorithms\swea_1249\swea_1249_input.txt", "r")

def build_map(map_size):
    map_array = list()
    for idx in range(map_size):
        map_array.append([int(val) for val in str(input())])
    return map_array

def min_path_value(map_size, map_array):
    def validation(val,x,y):
        if 0<=x<map_size and 0<=y<map_size:
            if to_visit[x+y*map_size]:
                to_visit[x+y*map_size] = 0
                return val+map_array[x][y], x, y

    visited = [(0,0,0)]
    to_visit = [1]*map_size**2
    while visited:
        val, x, y = visited.pop(0)
        if (x, y) == (map_size-1, map_size-1):
            return val
        tmp_lst = list()
        tmp_lst += [validation(val, x+1, y)]
        tmp_lst += [validation(val, x-1, y)]
        tmp_lst += [validation(val, x, y+1)]
        tmp_lst += [validation(val, x, y-1)]
        visited += list(filter(None,tmp_lst))
        visited.sort()

def solve(test_case):
    map_size = int(input())
    print(f'#{test_case} {min_path_value(map_size, build_map(map_size))}')

T = int(input())
for test_case in range(1, T + 1):
    solve(test_case)