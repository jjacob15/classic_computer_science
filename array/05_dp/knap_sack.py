def knapsack(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    # print(weights, values, W)
    # print(dp)
    for i in range(1, n + 1):
        for w in range(W + 1):
            # print(w, weights[i-1])
            if weights[i-1] <= w:
                # print("i",dp[i-1][w],dp[i-1][w-weights[i-1]],values[i-1],dp[i-1][w-weights[i-1]] + values[i-1])
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                # print("e",dp[i-1][w])
                dp[i][w] = dp[i-1][w]
            # print(dp)
    
    return dp[n][W]