n, k = map(int, input().split())
lst = [map(int,input().split()) for _ in range(n)]
count = [0]*12
for s, grade in lst:
    count[6*s+grade-1] += 1
result = 0
for val in count:
    result += val//k
    result += bool(val%k)
print(result)