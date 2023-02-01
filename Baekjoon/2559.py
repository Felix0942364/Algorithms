N, K = map(int, input().split())
raw_data = list(map(int, input().split()))

data = list()
for _ in range(K):
    data.append(raw_data.pop())

tmp = sum(data)
res = tmp
while raw_data:
    add = raw_data.pop()
    data.append(add)
    rm = data.pop(0)
    tmp += add
    tmp -= rm
    if tmp > res:
        res = tmp

print(res)