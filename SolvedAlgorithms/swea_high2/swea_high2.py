# import sys
# sys.stdin = open("github\Algorithms\SolvedAlgorithms\swea_high2\swea_high2_input.txt", "r")

# def solve(num, weight):
#     pass

# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     weights = list(map(int,input().split()))
#     solve(N, weights)

num_list = [1,54,888,22,154]
max = [num_list[i+1] for i in range(len(num_list)-1) if num_list[i+1] > num_list[i]]
print(max)