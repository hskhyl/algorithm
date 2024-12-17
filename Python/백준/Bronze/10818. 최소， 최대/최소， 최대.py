import sys
num = int(input())
num_list = list(map(int,sys.stdin.readline().strip().split()))
# print(num_list)

min_num = min(num_list)
max_num = max(num_list)
print(min_num, max_num)