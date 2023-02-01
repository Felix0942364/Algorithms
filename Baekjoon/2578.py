raw, call = list(), list()

for _ in range(5):
    for val in list(map(int,input().split())):
        raw += [val]
for _ in range(5):
    for val in list(map(int,input().split())):
        call += [val]

bingo_array = [False for _ in range(25)]
hor, ver = list(), list()
for i in range(5):
    hor.append([bingo_array[i*5+j] for j in range(5)])
    ver.append([bingo_array[i+j*5] for j in range(5)])
dia1 = [bingo_array[6*i] for i in range(5)]
dia2 = [bingo_array[4 + 4*i] for i in range(5)]
check_lst = list()
check_lst.append(hor)
check_lst.append(ver)
check_lst.append(dia1)
check_lst.append(dia2)

count = 0
tick = 3

while call:
    count += 1
    val = call.pop(0)
    idx = raw.index(val)
    bingo_array[idx] = True
    print(val, idx, bingo_array)
    if check_lst.count([True,True,True,True,True]) == 3:
        break
    print(check_lst)

print(count)