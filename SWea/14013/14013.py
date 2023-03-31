from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, 1+int(input())):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    memo = [100*N] * (1<<N)
    memo[0] = 0
    q = deque([(0, 0)])

    while q:
        s, i = q.popleft()
        for j in range(N):
            if s & 1<<j:
                continue
            elif memo[s]+lst[i][j] < memo[s|1<<j]:
                memo[s|1<<j] = memo[s]+lst[i][j]
                q.append((s|1<<j, i+1))
    print(f'#{tc} {memo[-1]}')