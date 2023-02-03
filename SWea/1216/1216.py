import sys
sys.stdin = open("1216_input.txt", "r")

for test_case in range(1, 11):
    tc = input()
    hor_array = [list(input()) for _ in range(100)]
    ver_array = [[hor_array[y][x] for y in range(100)] for x in range(100)]
    
    result = 0
    for idx in range(100):
        for diff in range(100):
            for size in range(100-diff+1):
                if size < result:
                    continue
                if hor_array[idx][diff:diff+size//2] == hor_array[idx][diff+size-1:diff+size-1-size//2:-1]:
                    if size>result:
                        result = size
                if ver_array[idx][diff:diff+size//2] == ver_array[idx][diff+size-1:diff+size-1-size//2:-1]:
                    if size>result:
                        result = size

    print('#{} {}'.format(tc, result))
