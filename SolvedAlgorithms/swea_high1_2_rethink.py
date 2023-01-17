# # import from txt file
# import sys
# sys.stdin = open("input.txt", "r")

# T = int(input())
# for test_case in range(1, T + 1):

# manual input
N = 3
weights = [1,2,4]

# setup cases to test
case = [[1]]
i = 1
r = 1
while i < N:
    i += 1
    r *= i
    tmp1 = []
    for j in range(len(case)):
        for k in range(i):
            tmp2 = case[j][:]
            tmp2.insert(k, i)
            tmp1 += [tmp2[:]]
    case = tmp1[:]
del tmp1, tmp2
print(case)
print(len(case))

count = 0
while case:
    queue = case.pop()
    print(queue)


        
# def DFS(start_node):
#     stack = [start_node, ]
#     while True:
#         if len(stack) == 0:
#             print('All node searched.')
#             return None
#         node = stack.pop()
#         if node == TARGET:
#             print('The target found.')
#             return node
#         children = expand(node)
#         stack.extend(children)

# def BFS(start_node):
#     queue = [start_node, ]
#     while True:
#         if len(queue) == 0:
#             print('All node searched.')
#             return None
#         node = queue.pop(0)
#         if node == TARGET:
#             print('The target found.')
#             return node
#         children = expand(node)
#         queue.extend(children)
