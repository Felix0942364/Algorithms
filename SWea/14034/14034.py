from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 1+int(input())):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 200000
    visited = [False] * (1<<N)
    q = deque(((0,0),))
    while q:
        i, s = q.pop()
        if s >= S:
            result = min(result, s)
            if result == S:
                break
            continue
        for j in range(i, N):
            q.append((j+1, s + lst[j]))
    print("#{} {}".format(tc, result-S))