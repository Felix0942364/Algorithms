idx = int(input())
lst = list(map(int, input().split()))
tmp1 = 1
tmp2 = 1
result = 1
for i in range(idx-1):
    if lst[i] < lst[i+1]:
        tmp1 += 1
        tmp2 = 1
        if tmp1 > result:
            result = tmp1
    elif lst[i] > lst[i+1]:
        tmp1 = 1
        tmp2 += 1
        if tmp2 > result:
            result = tmp2
    elif lst[i] == lst[i+1]:
        tmp1 += 1
        tmp2 += 1
        if max(tmp1,tmp2) > result:
            result = max(tmp1,tmp2)
print(result)