import sys
sys.stdin = open('1949.txt', 'r')

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def hiking_route(pos, dir, dig):
    global depth
    global arr_size
    x, y = pos
    dx, dy = dir
    pos_height = array[y][x]
    
    if dig and pos == dig[0:2]:
        pos_height -= dig[2]
        
    if 0 <= x+dx < arr_size and 0 <= y+dy < arr_size and not visited[y+dy][x+dx]:
        if pos_height > array[y+dy][x+dx]:
            return (x+dx, y+dy), dig
        elif not dig and pos_height > array[y+dy][x+dx] - depth:
            return (x+dx, y+dy), (x+dx, y+dy, array[y+dy][x+dx] - pos_height + 1)

    return False, False

def dfs(pos, dig, length):
    global answer
    answer = max(answer, length)
    
    for dir in directions:
        new_pos, new_dig = hiking_route(pos, dir, dig)
        if new_pos:
            nx, ny = new_pos
            visited[ny][nx] = True
            dfs(new_pos, new_dig, length+1)
            visited[ny][nx] = False


T = int(input())
for test_case in range(1, 1+T):
    arr_size, depth = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(arr_size)]
    visited = [[False] * arr_size for _ in range(arr_size)]
    summit = 0
    for tmp in array:
        summit = max(max(tmp), summit)    
    summits = [(x, y) for x in range(arr_size) for y in range(arr_size) if array[y][x] == summit]
    
    answer = 0
    for summit in summits:
        s_x, s_y = summit
        visited[s_y][s_x] = True
        dfs(summit, False, 1)
        visited[s_y][s_x] = False

    print(f'#{test_case}', answer)
