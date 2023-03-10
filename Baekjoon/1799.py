def dfs(idx, cnt, ref_lst, mx_idx):
    global tmp
    if idx == mx_idx:
        tmp = max(tmp, cnt)
        return
    
    dfs(idx+1, cnt, ref_lst, mx_idx)
    r, c = ref_lst[idx]
    if not dia[r-c] and not dia_r[r+c]:
        dia[r-c] = 1
        dia_r[r+c] = 1
        dfs(idx+1, cnt+1, ref_lst, mx_idx)
        dia[r-c] = 0
        dia_r[r+c] = 0

N = int(input())
array = [(r,c) for r in range(N) for c, v in enumerate(list(map(int, input().split())))  if v]
white = list()
black = list()

for r, c in array:
    if (r+c)%2:
        white.append((r, c))
    else:
        black.append((r, c))

wh_idx = len(white)
bl_idx = len(black)

dia = [0]*2*N
dia_r = [0]*2*N

answer = 0
tmp = 0
dfs(0,0,white,wh_idx)
answer += tmp
tmp = 0
dfs(0,0,black,bl_idx)

print(answer + tmp)
