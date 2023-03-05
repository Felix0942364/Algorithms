import sys
sys.stdin = open('2105.txt', 'r')


def complete_tour(pos, d, dessert, sides):
    r, c = pos
    dr, dc = direction[d%4]
    for i in range(1, sides[0] + 1):
        if not 0<=r+i*dr<arr_size or not 0<=c+i*dc<arr_size or array[r+i*dr][c+i*dc] in dessert:
            return -1
        else:
            dessert += [array[r+i*dr][c+i*dc]]
    else:
        r += sides[0]*dr
        c += sides[0]*dc
        dr, dc = direction[(d+1)%4]
    for i in range(1, sides[1]):
        if not 0<=r+i*dr<arr_size or not 0<=c+i*dc<arr_size or array[r+i*dr][c+i*dc] in dessert:
            return -1
        else:
            dessert += [array[r+i*dr][c+i*dc]]
    return 2*sum(sides)

def dfs(pos, d, dessert, sides):
    if len(sides) == 2:
        global max_dessert
        max_dessert = max(max_dessert, complete_tour(pos, d, dessert, sides))
        return
    
    r, c = pos
    dr, dc = direction[d%4]
    tmp = list()
    for i in range(1, arr_size):
        if 0<=r+i*dr<arr_size and 0<=c+i*dc<arr_size and array[r+i*dr][c+i*dc] not in dessert + tmp:
            tmp += [array[r+i*dr][c+i*dc]]
            dfs((r+i*dr, c+i*dc), d+1, dessert + tmp, sides + [i])
        else:
            break

direction = [(1,1), (1,-1), (-1,-1), (-1,1)]

T = int(input())
for test_case in range(1, T+1):
    arr_size = int(input())
    array = [list(map(int, input().split())) for _ in range(arr_size)]
    max_dessert = -1
    for r in range(arr_size):
        for c in range(arr_size):
            for d in range(4):
                dfs((r, c), d, [array[r][c]], [])

    print('#{} {}'.format(test_case, max_dessert))
