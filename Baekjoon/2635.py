n = int(input())
result = 0
result_lst = []
for i in range(n//2,n+1):
    tmp1 = n - i
    tmp2 = i - tmp1
    count = 3
    tmp_lst = [n, i, tmp1]
    while tmp2 >= 0:
        tmp_lst += [tmp2]
        tmp1, tmp2 = tmp2, tmp1-tmp2
        count += 1

    if count > result:
        result = count
        result_lst = tmp_lst

print(result)
print(' '.join(list(map(str,result_lst))))
