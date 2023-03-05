import sys
sys.stdin = open('2112.txt', 'r')


def streak_valid(lst):
    tmp = 0
    prev = None
    for c in lst:
        if c == prev:
            tmp += 1
        else:
            prev = c
            tmp = 1
        if tmp >= streak:
            return True
    return False


def check():
    global width
    global depth
    global streak
    for c in range(width):
        lst = [tmp[r][c] for r in range(depth)]
        if streak_valid(lst):
            continue
        else:
            return False
    return True


def dfs(cnt, idx):
    global answer
    global width
    global depth
    if cnt > answer or idx >= depth:
        return
    if check():
        answer = min(cnt, answer)
        return
    dfs(cnt, idx+1)
    tmp[idx] = [0]*width
    dfs(cnt+1, idx+1)
    tmp[idx] = [1]*width
    dfs(cnt+1, idx+1)
    tmp[idx] = array[idx][:]


T = int(input())
for test_case in range(1, T+1):
    depth, width, streak = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(depth)]
    tmp = [row[:] for row in array]
    answer = depth
    dfs(0, 0)
    print('#{} {}'.format(test_case, answer))
