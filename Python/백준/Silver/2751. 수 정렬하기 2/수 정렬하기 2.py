import sys
num = int(input())

num_list = []

for _ in range(num):
    num_list.append(int(sys.stdin.readline().strip()))
    
num_list.sort()

for _ in num_list:
    print(_)