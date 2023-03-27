directions = [(-1,0,0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]
ripe = [(h, n, m) for m in range(M) for n in range(N) for h in range(H) if box[h][n][m] == 1]
queue = ripe
result = -1
while queue:
    ripe = list()
    while queue:
        h, n, m = queue.pop()
        for dh, dn, dm in directions:
            if 0<= m+dm < M and 0 <= n+dn < N and 0 <= h + dh < H:
                if box[h+dh][n+dn][m+dm] == 0 and not visited[h+dh][n+dn][m+dm]:
                    visited[h+dh][n+dn][m+dm] = True
                    ripe.append((h+dh, n+dn, m+dm))
    queue = ripe
    result += 1

if [1 for m in range(M) for n in range(N) for h in range(H) if box[h][n][m] == 0 and not visited[h][n][m]]:
    result = -1

print(result)