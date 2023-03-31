import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    visited = [False]*(1<<N)
    result = 0
    stack = [(0,0)]
    while stack:
        set, sum = stack.pop()
        if sum == M:
            result += 1
            continue
        for i in range(N):
            if set & 1<<i or visited[set|1<<i]:
                continue
            if sum + lst[i]<= M:
                visited[set|1<<i] = True         
                stack.append((set|1<<i, sum + lst[i]))
    print(f"#{test_case} {result}")