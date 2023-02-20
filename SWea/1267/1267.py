import sys
sys.stdin = open("1267.txt", "r")

for test_case in range(1,11):
    N, E = map(int, input().split())
    nodes = list(map(int, input().split()))
    ascending_dic = {idx : [] for idx in range(1, 1+N)}
    descending_dic = {idx : [] for idx in range(1, 1+N)}
    
    answer = []
    
    while nodes:
        child = nodes.pop()
        parent = nodes.pop()
        ascending_dic[child].append(parent)
        descending_dic[parent].append(child)
        
    while descending_dic:
        temp = list(descending_dic.items())[:]
        for k, i in temp:
            if not i:
                answer.append(k)
                for idx in ascending_dic[k]:
                    descending_dic[idx].remove(k)
                descending_dic.pop(k)
                
    answer = list(map(str, reversed(answer)))
    print("#{} {}".format(test_case, " ".join(answer)))
