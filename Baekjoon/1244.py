def turn_switch(gender, position, switch, max_num):
    def transform(idx,lst):
        lst[idx] += 1
        lst[idx] %= 2

    if gender == 1:
        for multiple in range(position, max_num+1, position):
            transform(multiple-1, switch)
    else:
        transform(position-1, switch)
        if position == 1 or position == max_num:
            pass
        elif 2 * position < max_num:
            for idx in range(1, position):
                if switch[(position-1)-idx] != switch[(position-1)+idx]:
                    break
                transform((position-1)-idx, switch)
                transform((position-1)+idx, switch)
        else:
            for idx in range(1, max_num-position+1):
                if switch[(position-1)-idx] != switch[(position-1)+idx]:
                    break
                transform((position-1)-idx, switch)
                transform((position-1)+idx, switch)

number_of_switch = int(input())
switch_list = list(map(int, input().split()))
number_of_people = int(input())
cases = [tuple(map(int, input().split())) for _ in range(number_of_people)]

for (gender, position) in cases:
    turn_switch(gender, position, switch_list, number_of_switch)

for i in range(1, len(switch_list)+1):
    if i % 20 == 0:
        print(switch_list[i-1])
    else:
        print(switch_list[i-1], end=' ')    