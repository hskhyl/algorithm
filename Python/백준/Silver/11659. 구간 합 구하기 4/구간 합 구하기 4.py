import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
N_list = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_sum = [0] * (N + 1)

for index in range(1, N + 1):
    prefix_sum[index] = prefix_sum[index - 1] + N_list[index - 1]
    
for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[j] - prefix_sum[i-1])
    