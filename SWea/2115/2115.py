import sys
sys.stdin = open('2115.txt', 'r')

def max_price(pos, streak, capacity):
    row, col = pos
    price = 0
    for i in range(1<<streak):
        tmp1 = 0
        tmp2 = 0
        for j in range(streak):
            if i & (1<<j):
                tmp1 += array[row][col+j]
                tmp2 += sqr_arr[row][col+j]
        if tmp1 <= capacity:
            price = max(price, tmp2)
    return price


def honey(pos_1, pos_2, streak, capacity):
    global answer
    area1 = max_price(pos_1, streak, capacity)
    area2 = max_price(pos_2, streak, capacity)
    answer = max(answer, area1 + area2)
    
    
T = int(input())
for test_case in range(1, 1+T):
    N, M, C = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    sqr_arr = [[array[i][j]**2 for j in range(N)] for i in range(N)]
    answer = 0
    for r_1 in range(N):
        for c_1 in range(N-M+1):
            for r_2 in range(r_1, N):
                for c_2 in range(N-M+1):
                    if r_1 == r_2 and c_1 + M > c_2 :
                        continue
                    honey((r_1, c_1), (r_2, c_2), M, C)
    print('#{} {}'.format(test_case, answer))
 