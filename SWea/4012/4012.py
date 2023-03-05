import sys
sys.stdin = open('4012.txt', 'r')


T = int(input())
for test_case in range(1, 1+T):
    array_size = int(input())
    array = list()
    total = 0
    for i in range(array_size):
        array.append(list(map(int, input().split())))

    result = 200000
    for i in range(1 << array_size):
        if bin(i).count('1') == array_size / 2:
            subset1 = []
            tmp1 = 0
            for j in range(array_size):
                if i & (1 << j):
                    for k in subset1:
                        tmp1 += array[k][j] + array[j][k]
                    subset1.append(j)
            subset2 = []
            tmp2 = 0
            for j in range(array_size):
                if (i ^ ((1 << array_size) - 1)) & (1 << j):
                    for k in subset2:
                        tmp2 += array[k][j] + array[j][k]
                    subset2.append(j)
            result = min(result, abs(tmp1 - tmp2))

    print(f'#{test_case}', result)
