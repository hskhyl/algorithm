import sys

N = int(sys.stdin.readline().rstrip())

def minimum_to_N(N):
    dp = [0]*(N + 1)
    
    for number in range(2, N+1):
        dp[number] = dp[number - 1] + 1 # 1로 빼서 이전꺼랑 더하면 되니까
        
        # 그런데 마냥 1만 빼서 이전꺼랑 더한다고 최적일 수 없음 배수일 수 있기 때문
        if number % 3 == 0:
            dp[number] = min(dp[number], dp[number // 3] + 1)

        if number % 2 == 0:  
            dp[number] = min(dp[number], dp[number // 2] + 1)
        

    
    return dp[N]

print(minimum_to_N(N))