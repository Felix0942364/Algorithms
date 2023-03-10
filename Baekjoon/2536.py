from collections import deque
import sys

sys.stdin = open('input.txt', 'r')

def solve():
    x, y = map(int, input().split())
    b = int(input())
    bus_route = {i: [] for i in range(b+1)}
    array = [[[] for _ in range(x+1)] for _ in range(y+1)]
    visited = [[False]*(x+1) for _ in range(y+1)]
    for _ in range(b):
        i, x1, y1, x2, y2 = map(int, input().split())
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                bus_route[i].append((x, y))
                array[y][x].append(i)
    s_x, s_y, g_x, g_y = map(int, input().split())
    queue = deque()
    queue.append((s_x,s_y,0, 0))
    visited[s_y][s_x] = True

    while queue:
        x, y, cnt, vert = queue.popleft()
        if (x, y) == (g_x, g_y):
            return cnt
        
        if vert:
            for bus in array[y][x]:
                for n_x, n_y in bus_route[bus]:
                    if not visited[n_y][n_x] and x != n_x or y != n_y:
                        queue.append((n_x, n_y, cnt+1))
                        visited[n_y][n_x] = True

print(solve())
