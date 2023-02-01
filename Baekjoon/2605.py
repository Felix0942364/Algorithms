N = int(input())
lst = list()
for num, pos in enumerate(map(int,input().split())):
    tmp_lst = list()
    tmp_lst = lst[:num-pos] + [str(num+1)] + lst[num-pos:]
    lst = tmp_lst
print(' '.join(lst))