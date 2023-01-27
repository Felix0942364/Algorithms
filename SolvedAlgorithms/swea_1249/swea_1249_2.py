import sys
sys.stdin = open("SolvedAlgorithms\swea_1249\swea_1249_input.txt", "r")

def build_map(map_size):
    map_array = list()
    for idx in range(map_size):
        map_array.append([int(val) for val in str(input())])
    return map_array

def queue_element_x(val, x, y, visited, map_size, val_array):
    if 0 <= x < map_size:
        if visited[x + y * map_size]:
            visited[x + y * map_size] = 0
            return val + val_array[x][y], x, y, visited
            
def queue_element_y(val, x, y, visited, map_size, val_array):
    if 0 <= y < map_size:
        if visited[x + y * map_size]:
            visited[x + y * map_size] = 0
            return val + val_array[x][y], x, y, visited

def initial_cutoff(map_size, val_array):
    result = sum(val_array[0] + [val_array[map_size-1][y] for y in range(map_size)]) - val_array[0][map_size-1]
    queue = [(0, 0, 0)]
    while queue:
        val, x, y = queue.pop()
        if val > result:
            continue
        if (x, y) == (map_size-1, map_size-1):
            if val < result:
                result = val
            continue
        tmp = []
        if x+1 < map_size:
            tmp.append((val + val_array[x+1][y], x+1, y))
        if y+1 < map_size:
            tmp.append((val + val_array[x][y+1], x, y+1))
        queue = sorted(tmp, reverse=True)
    return result

def dijkstra(cut_off, map_size, val_array):
    result = cut_off
    initial = [0] + [1]*(map_size**2-1)
    queue = [(0, 0, 0, initial)]
    while queue:
        val, x, y, visited = queue.pop()
        if val > result:
            continue
        if (x, y) == (map_size-1, map_size-1):
            if val < result:
                result = val
            continue
        tmp = []
        tmp.append(queue_element_x(val, x+1, y, visited, map_size, val_array))
        tmp.append(queue_element_x(val, x-1, y, visited, map_size, val_array))
        tmp.append(queue_element_y(val, x, y+1, visited, map_size, val_array))
        tmp.append(queue_element_y(val, x, y-1, visited, map_size, val_array))
        queue += [item for item in tmp if item is not None]
    return result

def min_path_value(map_size, map_array):
    cut_off = initial_cutoff(map_size, map_array)
    return dijkstra(cut_off, map_size, map_array)
    
def solve(test_case):
    map_size = int(input())
    print(f'#{test_case} {min_path_value(map_size, build_map(map_size))}')

T = int(input())
T = 3
for test_case in range(1, T + 1):
    solve(test_case)