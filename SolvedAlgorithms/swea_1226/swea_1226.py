import sys
sys.stdin = open("SolvedAlgorithms\swea_1226\swea_1226_input.txt", "r")

def call_map_array():
    map_lst = list(input())
    map_size = len(map_lst)
    for i in range(map_size-1):
        map_lst += str(input())
    map_lst = [int(x) for x in map_lst]
    return map_lst, map_size

def find_position(val, array, size):
    tmp = array.index(val)
    x = tmp % size
    y = tmp // size
    return x, y

def find_path(start, goal, array, size):
    current_x, current_y = find_position(start, array, size)
    goal_x, goal_y = find_position(goal, array, size)
    queue = []
    queue.append((current_x, current_y))
    while queue:
        current_x, current_y = queue.pop()
        if array[(current_x+1) + current_y*size] == 0 or array[(current_x+1) + current_y*size] == goal:
            queue.append((current_x+1, current_y))
            array[(current_x+1) + current_y*size] = 4
        if array[(current_x-1) + current_y*size] == 0 or array[(current_x-1) + current_y*size] == goal:
            queue.append((current_x-1, current_y))
            array[(current_x-1) + current_y*size] = 4
        if array[current_x + (current_y+1)*size] == 0 or array[current_x + (current_y+1)*size] == goal:
            queue.append((current_x, current_y+1))
            array[current_x + (current_y+1)*size] = 4
        if array[current_x + (current_y-1)*size] == 0 or array[current_x + (current_y-1)*size] == goal:
            queue.append((current_x, current_y-1))
            array[current_x + (current_y-1)*size] = 4
        if (goal_x, goal_y) in queue:
            return True
    return False

def solve(start, goal):
    (array, size) = call_map_array()
    return find_path(start, goal, array, size)

T = 10

for test_case in range(1, T + 1):
    case = int(input())
    start, goal = 2, 3
    print(f'#{case} {int(solve(start, goal))}')
