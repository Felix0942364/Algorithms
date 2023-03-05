import sys
sys.stdin = open('5644.txt', 'r')

directions = {0:(0,0), 1:(-1,0), 2:(0,1), 3: (1,0), 4: (0,-1)}

T = int(input())
for test_case in range(1, 1+T):
    movement, battery_chargers = map(int, input().split())
    
    a_position = [(0,0)]
    b_position = [(9,9)]
    a_movement = list(map(int, input().split()))
    b_movement = list(map(int, input().split()))

    for a in a_movement:
        r, c = a_position[-1]
        dr, dc = directions[a]
        a_position.append((r + dr, c + dc))

    for b in b_movement:
        r, c = b_position[-1]
        dr, dc = directions[b]
        b_position.append((r + dr, c + dc))

    reference = list()
    index = -1
    array = [[[] for _ in range(10)] for _ in range(10)]
    for _ in range(battery_chargers):
        column, row, radius, intensity = map(int, input().split())
        reference.append(intensity)
        index += 1
        ptr_1 = row - 1
        ptr_2 = row - 1
        while radius > -1:
            for c in range(column - radius - 1, column + radius):
                if 0 <= c < 10:
                    if 0 <= ptr_1 < 10:
                        array[ptr_1][c].append(index)
                    if 0 <= ptr_2 < 10 and ptr_2 != row - 1:
                        array[ptr_2][c].append(index)
            ptr_1 -= 1
            ptr_2 += 1
            radius -= 1

    # check = list()
    # for r in range(10):
    #     for c in range(10):
    #         if len(array[r][c]) > 2:
    #             check.append(array[r][c])
    
    # restriction = list()
    # for i in range(len(check)):
    #     for j in range(len(check[i])):
    #         for k in range(len(check[i])):
    #             if j != k:
    #                 pass

    result = 0
    tmp1 = 0
    for t in range(movement+1):
        a_r, a_c = a_position[t]
        b_r, b_c = b_position[t]
        tmp2 = 0
        if array[a_r][a_c] and array[b_r][b_c]:
            for i in array[a_r][a_c]:
                for j in array[b_r][b_c]:
                    if i == j:
                        tmp2 = max(tmp2, reference[i])
                    else:
                        tmp2 = max(tmp2, reference[i] + reference[j])
        else:
            for idx in array[a_r][a_c]:
                tmp2 = max(tmp2, reference[idx])
            for idx in array[b_r][b_c]:
                tmp2 = max(tmp2, reference[idx])
        tmp1 += tmp2

    print(f'#{test_case}', result)