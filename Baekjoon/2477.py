'''
7
4 50
2 160
3 30
1 60
3 20
1 100
'''
class orchard():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.points = [(0,0)]
        
    def trace(self, tup):
        num, val = tup
        if num == 1:
            self.x += val
            self.points.append((self.x, self.y))
        elif num == 2:
            self.x -= val
            self.points.append((self.x, self.y))
        elif num == 3:
            self.y -= val
            self.points.append((self.x, self.y))
        elif num == 4:
            self.y += val
            self.points.append((self.x, self.y))
    
    def area(self):
        def cross_product(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return x1*y2-x2*y1
        
        result = 0
        for i in range(len(self.points)-1):
            result += cross_product(self.points[i], self.points[i+1])
        return abs(result)/2
    
density = int(input())
felix_orchard = orchard()

while True:
    felix_orchard.trace(tuple(map(int, input().split())))
    if felix_orchard.points[-1] == (0,0):
        break

print(int(density*felix_orchard.area()))