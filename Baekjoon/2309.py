'''
20
7
23
19
10
15
25
8
13
'''
def solve(lst):
    total = sum(lst)
    for i in range(9):
        for j in range(9):
            if not i == j:
                if total - lst[i] - lst[j] == 100:
                    tmp1, tmp2 = lst[i], lst[j]
                    lst.remove(tmp1)
                    lst.remove(tmp2)
                    return lst
    return

dwarves = list()
for _ in range(9):
    dwarves.append(int(input()))
    
dwarves.sort()
solve(dwarves)
for dwarf in dwarves:
    print(dwarf)
