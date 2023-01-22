dic = {
    "start" : {0 : 140, 1:80, 'start' : 0, 'end' : 200},
    "end" : {0 : 80, 1 : 120, 'start' : 200, 'end' : 0},
    0 : {0 : 0, 1 : 50, 'start' : 140, 'end' : 80},
    1 : {0 : 50, 1 : 0, 'start' : 80, 'end' : 120}
}
people = 2
res = 200 * people
value, route = 0, ['start']
queue = [(value, route)]
while queue:
    value, route = queue.pop()
    if sorted(route[1:]) == list(range(people)):
        value += dic[route[-1]]['end']
        if res > value:
            res = value
            print('added', res)
        continue
    for idx in range(people):
        if not idx in route:
            if value < res:
                queue.append((value + dic[route[-1]][idx], route + [idx]))

print(res)