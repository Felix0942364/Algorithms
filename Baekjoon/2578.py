def check(i):
    hor[i//5][i%5] = True
    ver[i%5][i//5] = True
    if i in [0,6,12,18,24]:
        dia1_dic = {0:0,6:1,12:2,18:3,24:4} # dia1_dic = {6*idx:idx for idx in range(5)}
        dia1[dia1_dic[i]] = True    
    if i in [4,8,12,16,20]:
        dia2_dic = {4:0,8:1,12:2,16:3,20:4} # dia1_dic = {20-4*idx:idx for idx in range(5)}
        dia2[dia2_dic[i]] = True
        
raw, call = list(), list()
for _ in range(5):
    for val in list(map(int,input().split())):
        raw += [val]
for _ in range(5):
    for val in list(map(int,input().split())):
        call += [val]
        
hor, ver, dia1, dia2 = list(), list(), list(), list()
for i in range(5):
    hor.append([False for _ in range(5)])
    ver.append([False for _ in range(5)])
    dia1 += [False]
    dia2 += [False]
    
check_lst = hor + ver
check_lst.append(dia1)
check_lst.append(dia2)

count = 0
while call:
    count += 1
    val = call.pop(0)
    idx = raw.index(val)
    check(idx)
    if check_lst.count([True,True,True,True,True]) >= 3:
        break
print(count)