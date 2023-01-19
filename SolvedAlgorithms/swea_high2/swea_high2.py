import sys
sys.stdin = open("github\Algorithms\SolvedAlgorithms\swea_high2\swea_high2_input.txt", "r")

def solve(num, weight):
    pass

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    weights = list(map(int,input().split()))
    solve(N, weights)
