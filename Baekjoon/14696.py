def solve(a, a_lst, b, b_lst):
    a_lst.sort(); b_lst.sort()
    while a_lst and b_lst:
        a_val = a_lst.pop()
        b_val = b_lst.pop()
        if a_val > b_val:
            return 'A'
        elif a_val < b_val:
            return 'B'
    if a_lst:
        return 'A'
    elif b_lst:
        return 'B'
    else:
        return 'D'

T = int(input())

for test_case in range(1,T+1):
    a_num, *a_lst = map(int,input().split())
    b_num, *b_lst = map(int,input().split())
    print(solve(a_num, a_lst, b_num, b_lst))
