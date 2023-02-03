import sys
sys.stdin = open("1215_input.txt", "r")

for test_case in range(1, 11):
    size = int(input())
    hor_array = [list(input()) for _ in range(8)]
    ver_array = [[hor_array[y][x] for y in range(8)] for x in range(8)]
    
    cnt = 0
    for idx in range(8):
        for diff in range(8-size+1):
            if hor_array[idx][diff:diff+size//2] == hor_array[idx][diff+size-1:diff+size-1-size//2:-1]:
                cnt += 1
            if ver_array[idx][diff:diff+size//2] == ver_array[idx][diff+size-1:diff+size-1-size//2:-1]:
                cnt += 1

    print('#{} {}'.format(test_case, cnt))
