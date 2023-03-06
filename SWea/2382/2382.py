import sys
sys.stdin = open('2382.txt', 'r')

idx_refactor = [None, 0, 2, 1, 3]
directions = [(-1,0), (0,-1), (1, 0), (0, 1)]

def move(row, column, size, d_idx):
    dr, dc = directions[d_idx]
    n_r, n_c = row + dr, column + dc
    if n_r in [0, arr_size - 1] or n_c in [0,arr_size - 1]:
        if size == 1:
            return
        tmp_arr[n_r][n_c].append((n_r, n_c, size // 2, (d_idx+2)%4))
    else:
        tmp_arr[n_r][n_c].append((n_r, n_c, size, d_idx))

T = int(input())
for test_case in range(1, 1+T):
    arr_size, test_time, cluster = map(int, input().split())
    
    microbes = [None] * cluster
    for i in range(cluster):
        r, c, s, d = map(int, input().split())
        microbes[i] = (r, c, s, idx_refactor[d])

    for t in range(test_time):
        queue = microbes
        tmp_arr = [[[] for _ in range(arr_size)] for _ in range(arr_size)]
        
        for r, c, s, d in queue:
            move(r,c,s,d)
        
        new_queue = list()
        for row in range(arr_size):
            for col in range(arr_size):
                if tmp_arr[row][col]:
                    new_size = 0
                    new_dir = None
                    tmp = 0
                    for r, c, s, d in tmp_arr[row][col]:
                        new_size += s
                        if s > tmp:
                            tmp = s
                            new_dir = d
                    new_queue.append((row, col, new_size, new_dir))
        microbes = new_queue
    
    print(f'#{test_case}', sum([x[2] for x in microbes]))
