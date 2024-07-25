def knapsack(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    # print(weights)
    # print(dp)
    for i in range(1, n + 1):
        for w in range(W + 1):
            # print(weights[i-1] ,w)
            if weights[i-1] <= w:
                # print(w,weights[i-1],w-weights[i-1])
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
            # print(dp)
    
    return dp[n][W]