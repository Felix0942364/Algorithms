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

    min_val = {i:[] for i in range(101)}
    for pos in x_index:
        tmp = pos
        for _, y in intersections:
            if y == tmp:
                tmp = x_index[x_index.index(y)+1]
            elif y == x_index[x_index.index(tmp)-1]:
                tmp = y
        min_val[abs(tmp-pos)] = pos
    for lst in min_val.values:
        tmp
    
    # todo : return minimum dictionary value, if needed look through dictionary methods