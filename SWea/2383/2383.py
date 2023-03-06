import sys
sys.stdin = open('2383.txt', 'r')


def time(selection):
    def update_queue():
        print(stair_occ)
        return [[stair_occ[n_s][j] - 1 for j in range(len(stair_occ[n_s])) if stair_occ[n_s][j] - 1 != 0] for i in range(n_s)]
    global answer
    global distances
    global stair_time
    global n_s

    time = 0
    queue_lst = [[distances[i][j]+1 for i, k in enumerate(selection) if j == k] for j in range(n_s)]

    for queue in queue_lst:
        queue.sort()
    
    print(queue_lst)

    stair_occ = [[] for _ in range(n_s)]
    
    while not all(queue == [] for queue in queue_lst):
        print(queue_lst)
        print(time)
        for stair in range(n_s):
            while queue_lst[stair] and queue_lst[stair][0] >= time and len(stair_occ[stair]) < 3:
                queue_lst[stair].pop(0)
                stair_occ[stair].append(stair_time[stair])
        stair_occ = update_queue()
        time += 1
            
    answer = min(answer, time)

def dfs(selection):
    global n_s
    global n_p
    if len(selection) == n_p:
        print(n_p, selection)
        time(selection)
        return
    
    for i in range(n_s):
        dfs(selection + [i])


T = int(input())
for test_case in range(1, 1+T):
    arr_size = int(input())
    array = [list(map(int, input().split())) for _ in range(arr_size)]
    people = [(r,c) for r in range(arr_size) for c in range(arr_size) if array[r][c] == 1]
    stairs = [(r,c) for r in range(arr_size) for c in range(arr_size) if array[r][c] > 1]
    distances = [[abs(p_r-s_r)+abs(p_c-s_c) for s_r, s_c in stairs] for p_r, p_c in people]
    stair_time = [array[r][c] for r in range(arr_size) for c in range(arr_size) if array[r][c] > 1]
    n_p = len(people)
    n_s = len(stairs)
    answer = 2 * arr_size + 10
    dfs([])
    print(f'#{test_case}', answer)

