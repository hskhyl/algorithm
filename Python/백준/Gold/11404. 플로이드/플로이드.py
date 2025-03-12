import sys

def floyd_warshall(n, graph):
    INF = float('inf')
    # 비용 행렬 초기화
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 자기 자신으로 가는 비용은 0
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    # 주어진 간선 정보로 초기화 (중복 노선이 있을 경우 최소 비용만 저장)
    for a, b, c in graph:
        dist[a][b] = min(dist[a][b], c)

    # 플로이드–워셜 알고리즘 수행
    for k in range(1, n + 1):  # 경유지
        for i in range(1, n + 1):  # 출발 도시
            for j in range(1, n + 1):  # 도착 도시
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 도달할 수 없는 경우 0으로 변경
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] == INF:
                dist[i][j] = 0

    return dist

def main():
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])  # 도시 개수
    m = int(data[1])  # 버스 개수
    graph = [tuple(map(int, line.split())) for line in data[2:m+2]]

    result = floyd_warshall(n, graph)

    # 결과 출력
    for i in range(1, n + 1):
        print(" ".join(map(str, result[i][1:])))

if __name__ == "__main__":
    main()
