import sys
from collections import Counter

num_1 = int(input())
num_list_1 = list(sys.stdin.readline().strip().split())

num_2 = int(input())
num_list_2 = list(sys.stdin.readline().strip().split())

# Counter로 개수 새기
counter = Counter(num_list_1)

result = [str(counter[target_number]) for target_number in num_list_2]

answer = ' '.join(result)
print(answer)