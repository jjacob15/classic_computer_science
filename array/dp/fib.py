def fib(n):
    dp = [0] * (n+2)
    dp[1] = 1
    for i in range(0, n):
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]
    return dp[n]
