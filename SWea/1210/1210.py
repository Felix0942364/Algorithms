import sys
sys.stdin = open("1210_input.txt", "r")

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
    intersections.sort()

    tmp_lst = list(map(int,input().split()))
    for x in x_index:
        if tmp_lst[x] == 2:
            pos = x

    for _, y in intersections[-1:0:-1]:
        if y == pos:
            pos = x_index[x_index.index(y)+1]
        elif y == x_index[x_index.index(pos)-1]:
            pos = y
    print('#{} {}'.format(t, pos))