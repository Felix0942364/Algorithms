from itertools import combinations

def rules(lst):
    for i in range(0, len(lst), 2):
        if lst[i] + 2 != lst[i+1]:
            return False
    return True

def calculate(lst):
    tmp = lst[0]
    for i in range(1, len(lst),2):
        if lst[i] == '+':
            tmp += lst[i+1]
        elif lst[i] == '-':
            tmp -= lst[i+1]
        elif lst[i] == '*':
            tmp *= lst[i+1]
        else:
            print("error in code")  
            return False
    return tmp

def evaluate(arithmatic, paranthesis):
    parsed_equation = list()
    i = 0
    j = 0
    flag = False
    while i < N:
        if flag or i < paranthesis[j]:
            parsed_equation.append(arithmatic[i])
            i += 1
            continue
        else:
            high_priority = arithmatic[paranthesis[j] : paranthesis[j+1]+1]
            parsed_equation.append(calculate(high_priority))
            i = paranthesis[j+1]+1
            j += 2
            if j >= len(paranthesis): 
                flag = True
    return calculate(parsed_equation)

N = int(input())
base = list(input())
targets = range(0, N, 2)
for i in targets:
    base[i] = int(base[i])

answer = calculate(base)

for n in range(2, N, 2):
    iter = list(combinations(targets, n))
    filtered_iter = filter(rules, iter)
    for paranthesis in filtered_iter:
        tmp = evaluate(base, paranthesis)
        answer = max(answer, tmp)
print(answer)