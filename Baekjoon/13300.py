n, k = map(int, input().split())
lst = [map(int,input().split()) for _ in range(n)]
tmp_lst = [0]*12
for s, grade in lst:
    tmp_lst[s+grade*6] += 1

result = 0
for val in tmp_lst:
    result += val//k
    result += val%k
print(result)