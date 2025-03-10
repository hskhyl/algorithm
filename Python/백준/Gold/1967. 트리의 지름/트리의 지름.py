import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, dist):
    global max_distance, farthest_node
    if dist > max_distance:
        max_distance = dist
        farthest_node = node

    for next_node, weight in tree[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, dist + weight)

# 입력 받기
n = int(input().strip())
tree = defaultdict(list)

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))  # 무방향 그래프이므로 양방향 추가

# Step 1: 루트(1)에서 가장 먼 노드 찾기
visited = [False] * (n + 1)
max_distance = 0
farthest_node = 0

visited[1] = True
dfs(1, 0)  # 루트에서 시작

# Step 2: farthest_node에서 가장 먼 노드 찾기
visited = [False] * (n + 1)
max_distance = 0

visited[farthest_node] = True
dfs(farthest_node, 0)  # 가장 먼 노드에서 시작

print(max_distance)
