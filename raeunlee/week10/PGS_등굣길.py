def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)] # dp 테이블 초기화
    dp[1][1] = 1
    
    for i, j in puddles: # 웅덩이가 있는 곳은 -1로 표시
        dp[j][i] = -1
    
 
    for y in range(1, n+1):
        for x in range(1, m+1):
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
            dp[y][x] += (dp[y-1][x] + dp[y][x-1]) % 1000000007
    print(dp)
    return dp[y][x]