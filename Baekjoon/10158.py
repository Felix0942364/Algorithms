def transform(val, std):
    if val >= 2*std:
        return val-2*std
    elif val > std:
        return 2*std-val
    else:
        return val

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

res_x = x+ t%(2*w)
res_y = y+ t%(2*h)

res_x = transform(res_x, w)
res_y = transform(res_y, h)

print(res_x, res_y)