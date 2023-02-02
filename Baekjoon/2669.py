lst = [list(map(int, input().split())) for _ in range(4)]
result = set()
for x1, y1, x2, y2 in lst:
    tmp_lst = list()
    for x_ in range(x1,x2):
        for y_ in range(y1, y2):
            tmp_lst.append((x_,y_))
    result.update(set(tmp_lst))
print(len(result))