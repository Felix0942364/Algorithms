def traverse(node, tmp, visited):
    if visited[node]:
        return tmp[node]
    
    visited[node] = True
    tmp_lst = []
    for next_node in graph_rev[node]:
        tmp_lst.append(traverse(next_node, tmp, visited))
    else:
        visited[node] = True
    tmp[node] = max(tmp_lst)

def solve():
    tmp = [0]*(N+1)
    visited = [True] + [False]*N
    for i in range(1,N+1):
        if graph_rev[i] == 0:
            tmp[i] = reference[i]
            visited[i] = True
    for i in range(1, N+1):
        continue

    return max(tmp)

T = int(input())
for tc in range(1, T+1):
    MAX = 1000;
    N = int(input())
    reference = {}
    graph_rev = {}
    for key in range(1, 1+N):
        time, *lst = map(int, input().split())
        reference[key] = time
        graph_rev[key] = lst
    
    visited = [False]*(N+1)
    result = MAX*N
    for half in range(1, N+1):
        reference[half] /=2
        result = min(result, solve())
        reference[half] *=2
    print(f'#{tc} {result}')