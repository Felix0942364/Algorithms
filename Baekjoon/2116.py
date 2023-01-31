case = int(input())
dice_list = list()
for _ in range(case):
    dice_list.append(list(map(int, input().split())))
dice_arrangement = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

result = 0
for dice_start in range(1,7):
    tmp = 0
    tmp_list = [dice[:] for dice in dice_list]
    for dice in tmp_list:
        bottom_index = dice.index(dice_start)
        top_index = dice_arrangement[bottom_index]
        dice_start = dice[top_index]
        
        dice[bottom_index] = 0
        dice[top_index] = 0 

        tmp += max(dice)
    if tmp > result:
        result = tmp

print(result)