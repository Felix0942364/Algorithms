import sys
sys.stdin = open("1211_input.txt", "r")

T = 10
for test_case in range(1,T+1):
    t = input()
    std = list(map(int, input().split()))
    x_index = list()
    count = 0

    for i in std:
        if i:
            x_index.append(count)            
        count+=1
    intersections = list()

    for i in range(1,98+1):
        tmp_lst = list(map(int, input().split()))
        for x in x_index[:-1]:
            if tmp_lst[x+1]:
                intersections.append((i,x))
    input()

    res = 0
    total = 10000
    for pos in x_index:
        tmp = 0
        tmp_pos = pos
        for _, y in intersections:
            if y == tmp_pos:
                tmp_pos = x_index[x_index.index(y)+1]
                tmp += tmp_pos-y 
            elif y == x_index[x_index.index(tmp_pos)-1]:
                tmp += tmp_pos-y
                tmp_pos = y
        if tmp <= total:
            total = tmp
            res = pos
    print('#{} {}'.format(test_case, res))