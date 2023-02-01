def distance(p1, p2):
    def coordinates(p):
        if p[0] == 1:
            return (p[1],Y)
        elif p[0] == 2:
            return (p[1],0)
        elif p[0] == 3:
            return (0, Y-p[1])
        elif p[0] == 4:
            return (X, Y-p[1])
    if p1[0] == p2[0]:
        return abs(p1[1] - p2[1])
    elif set((p1[0], p2[0])) == {1,2}:
        if p1[1] + p2[1] > X:
            return Y+ (X-p1[1]) + (X-p2[1])
        return Y+ p1[1] + p2[1]
    elif set((p1[0], p2[0])) == {3,4}:
        if p1[1] + p2[1] > Y:
            return X + (Y-p1[1]) + (Y-p2[1])
        return X + p1[1] + p2[1]
    else: # {1,3}, {1,4}, {2,3}, {2,4}
        c1 = coordinates(p1)
        c2 = coordinates(p2)
        c3 = (X*(max((p1[0], p2[0]))-3), Y*(2-min((p1[0],p2[0]))))
        return abs(c3[0]-c1[0])+abs(c3[1]-c1[1])+abs(c3[0]-c2[0])+abs(c3[1]-c2[1])

X, Y = map(int, input().split())
N = int(input())

raw_data = [list(map(int,input().split())) for _ in range(N)]
person = list(map(int,input().split()))

result = 0
for shop in raw_data:
    result += distance(person, shop)

print(result)