N = int(input())
result = set()
for i in range(N):
    x, y = map(int, input().split())
    tmp_lst = list()
    for x_ in range(x,x+10):
        for y_ in range(y, y+10):
            tmp_lst.append((x_,y_))
    result.update(set(tmp_lst))
print(len(result))