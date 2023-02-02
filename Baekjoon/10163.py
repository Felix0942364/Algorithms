grid = [[0 for _ in range(1001)] for _ in range(1001)]
T = int(input())

for idx in range(1, T+1):
    x, y, w, h = map(int, input().split())
    for _y in range(y, y+h):
        grid[_y][x:x+w] = [idx]*w

for idx in range(1, T+1):
    result = 0
    for cnt in range(1001):
        result += grid[cnt].count(idx)
    print(result)