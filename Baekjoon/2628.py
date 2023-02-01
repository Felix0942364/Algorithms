x, y = map(int,input().split())
n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]

lst_x = [0,x] + [lst[i][1] for i in range(n) if lst[i][0] == 1]
lst_y = [0,y] + [lst[i][1] for i in range(n) if lst[i][0] == 0]
lst_x.sort(); lst_y.sort()

max_x, max_y = 0, 0
for idx in range(len(lst_x)-1):
    tmp = lst_x[idx+1] - lst_x[idx]
    if tmp > max_x:
        max_x = tmp
for idx in range(len(lst_y)-1):
    tmp = lst_y[idx+1] - lst_y[idx]
    if tmp > max_y:
        max_y = tmp
        
print(max_x*max_y)