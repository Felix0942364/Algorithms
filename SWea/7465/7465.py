import sys
sys.stdin = open('7465.txt', 'r')


T = int(input())
for test_case in range(1, 1+T):
    node, edge = map(int, input().split())

    graph = [[] for _ in range(node + 1)]
    visited = [False] * (node + 1)
    visited[0] = [True]

    for _ in range(edge):
        node_1, node_2 = map(int, input().split())
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    crowd = 0
    for i in range(node + 1):
        if graph[i] and not visited[i]:
            crowd += 1

            queue = graph[i]
            visited[i] = True

            while queue:
                n = queue.pop()
                if visited[n]:
                    continue
                visited[n] = True
                queue.extend(graph[n])

    crowd += visited.count(False)

    print(f'#{test_case}', crowd)
