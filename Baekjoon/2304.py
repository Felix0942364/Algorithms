def solve(i, lst):
    def find_multiple_max(lst):
        maximum_x, maximum_y = max(cases, key=lambda x : x[1])
        i = 0
        res_lst = []
        for x, y in lst:
            if y == maximum_y:
                res_lst.append((x, y))
            i = i + 1
        return res_lst

    max_lst = find_multiple_max(lst)
    x, y = 0, 0
    result = 0
    for x_, y_ in lst:
        if x_ <= max_lst[0][0]:
            if y_ > y:
                result += (x_-x)*y
                x, y = x_, y_
        else:
            break
    lst.reverse()
    x, y = lst[-1][0], 0
    for x_, y_ in lst:
        if x_ >= max_lst[-1][0]:
            if y_ > y:
                result += (x-x_)*y
                x, y = x_, y_
        else:
            break
    return result + max_lst[0][1]*(max_lst[-1][0]-max_lst[0][0]+1)

case_num = int(input())
cases = list()
for _ in range(case_num):
    cases.append(tuple(map(int, input().split())))
cases.sort()

print(solve(case_num, cases))