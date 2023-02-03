def replace(y,x,h,w):
    for diff in range(h):
        lsts[y+diff][x] = '.'
    for diff in range(w):
        lsts[y][x+diff] = '.'

def check(y,x,val):
    if lsts[y][x+1] == val:
        if lsts[y][x+2] == val:
            if lsts[y][x+3] == val:
                replace(y,x,0,4)
                return 1
            replace(y,x,0,3)
            replace(y+1,x+1,0,1)
            return 4
        if lsts[y+1][x] == val:
            if lsts[y+1][x+1] == val:
                replace(y,x,0,2)
                replace(y+1,x,0,2)
                return 0
            replace(y,x,0,2)
            replace(y+1,x-1,0,2)
            return 2
        else:
            replace(y,x,0,2)
            replace(y+1,x+1,0,2)
            return 3
    elif lsts[y+1][x+1] == val and lsts[y+1][x-1] == val:
        replace(y,x,0,1)
        replace(y+1,x-1,0,3)
        return 4
    elif lsts[y+1][x+1] == val:
        if lsts[y+2][x+1] == val:
            replace(y,x,2,0)
            replace(y+1,x+1,2,0)
            return 2
        replace(y,x,3,0)
        replace(y+1,x+1,1,0)
        return 4
    elif lsts[y+1][x-1] == val:
        if lsts[y+2][x-1] == val:
            replace(y,x,2,0)
            replace(y+1,x-1,2,0)
            return 3
        replace(y,x,3,0)
        replace(y+1,x-1,1,0)
        return 4
    else:
        replace(y,x,4,0)
        return 1
    
row, column = map(int, input().split())
lsts = [['.']*(column+3)]*3
lsts += [['.']*3+list(input())+['.']*3 for _ in range(row)]
lsts += [['.']*(column+3)]*3

results = [0]*5
y = 3
while y < row+3:
    x = 2
    while x < column+3:
        x += 1
        if lsts[y][x] == '.':
            continue
        results[check(y,x,lsts[y][x])] += 1
    y += 1

for result in results:
    print(result)