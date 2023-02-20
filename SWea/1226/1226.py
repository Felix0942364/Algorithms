import sys
from collections import deque
sys.stdin = open("1226_input.txt", "r")

def call_map_array():
    map_lst = [list(map(int, input()))]
    map_size = len(map_lst[0])
    for _ in range(map_size-1):
        map_lst += [list(map(int, input()))]
    return map_lst, map_size

def find_position(val, array, size):
    for idx, row in enumerate(array):
        if val in row:
            return row.index(val), idx

def find_path(start, goal, array, size):
    start = find_position(start, array, size)
    goal = find_position(goal, array, size)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    stack = deque()
    stack.append(start)

    while stack:
        row, column = stack.pop()
        if (row, column) == goal:
            return True
        array[row][column] = 1
        for i in range(4):
            if 0 <= row+dr[i] < size and 0 <= column+dc[i] < size:
                if array[row+dr[i]][column+dc[i]] != 1:
                    stack.append((row+dr[i], column+dc[i]))
    return False

def solve(start, goal):
    array, size = call_map_array()
    return find_path(start, goal, array, size)

T = 10

for test_case in range(1, T + 1):
    case = int(input())
    start, goal = 2, 3
    print(f'#{case} {int(solve(start, goal))}')
