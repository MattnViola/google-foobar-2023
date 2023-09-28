def solution(n):
    dp = [1] + [0] * n
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            dp[j] += dp[j - i]
    return dp[n] - 1
        
print(solution(200))