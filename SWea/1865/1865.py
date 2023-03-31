import sys
sys.stdin = open("1865.txt", "r")
from collections import deque

T = int(input())
for test_case in range(1, 1+T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    result = [0]*(1<<N)
    result[0] = 1
    queue = deque([(0, 0)])
    while queue:
        idx, set = queue.popleft()
        for j in range(N):
            if 1<<j & set:
                continue
            if result[set|1<<j] < result[set]*lst[idx][j]:
                result[set|1<<j] = result[set]*lst[idx][j]
                queue.append((idx+1, set|1<<j))
    print('#{} {:.6f}'.format(test_case, result[1<<N-1]/100**(N-1)))