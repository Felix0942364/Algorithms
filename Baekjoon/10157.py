def solve(x, y, idx):
    if idx > x*y:
        return '0'
    res_x, res_y = 1, 0
    count = 0
    for i in range(0, (x+y)//2+2, 2):
        for y_pos in range(y-i):
            count+=1
            res_y+=1
            if count == idx:
                return str(res_x), str(res_y)
        for x_pos in range(x-i-1):
            count+=1
            res_x+=1
            if count == idx:
                return str(res_x), str(res_y)
        for y_neg in range(y-i-1):
            count+=1
            res_y-=1
            if count == idx:
                return str(res_x), str(res_y)
        for x_neg in range(x-i-2):
            count+=1
            res_x-=1
            if count == idx:
                return str(res_x), str(res_y)
    
x, y = map(int, input().split())
idx = int(input())
print(' '.join(solve(x,y,idx)))