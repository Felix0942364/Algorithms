import sys
sys.stdin = open('1952.txt', 'r')

def bfs(months, idx):
    while idx < 10:
        if sum(costs[idx:idx+3]) > price[2]:
            bfs(months+[idx, idx+1, idx+2], idx+3)
        idx += 1
    
    if idx >= 10:
        global answer
        tmp = 0
        for i in range(12):
            if i not in months:
                tmp += costs[i]
        tmp += price[2] * len(months) // 3
        answer = min(answer, tmp)
        return

T = int(input())
for test_case in range(1, 1+T):
    price = list(map(int, input().split()))
    workout = list(map(int, input().split()))
    costs = [min(workout[i]*price[0], price[1]) for i in range(12)]
    answer = price[3]
    bfs([], 0)
    print(f'#{test_case}', answer)
