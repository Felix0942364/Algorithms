import sys
sys.stdin = open('input.txt', 'r')

# def match(b, t):
#     sum_t = 0
#     sum_b = 0
#     ref = []
#     for i, char in enumerate(b[::-1]):
#         sum_b |= int(char)*(1<<i)
#         ref += [1<<i]
#     for i, char in enumerate(t[::-1]):
#         sum_t += int(char)*(3**i)
#     for i, char in enumerate(t[::-1]):
#         for new_char in [0, 1, 2]:
#             if (sum_t + (new_char- int(char))*(3**i)) - sum_b in ref:
#                 return sum_t + (new_char- int(char))*(3**i)

# for tc in range(1, 1+int(input())):
#     print(f"#{tc} {match(input(), input())}")

def s_b(lst):
    sum_b = 0
    for i, val in enumerate(lst[::-1]):
        sum_b |= val*(1<<i)
    return sum_b

def s_t(lst):
    sum_t = 0
    for i, val in enumerate(lst[::-1]):
        sum_t += val*(3**i)
    return sum_t

def match(b, t):
    for i in range(1,len(b)):
        b[i] += 1
        b[i] %= 2
        for j in range(len(t)):
            for _ in range(2):
                t[j] += 1
                t[j] %= 3
                if (s_t(t) == s_b(b)):
                    return s_b(b)
            t[j] += 1
            t[j] %= 3
        b[i] += 1
        b[i] %= 2

for tc in range(1, 1+int(input())):
    print(f"#{tc} {match(list(map(int,list(input()))), list(map(int,list(input()))))}")