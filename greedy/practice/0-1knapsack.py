# value = [60,100,120]
# weight = [1,2,4]
# capacity = 8
value = [5,3,5,3,2]
weight = [1, 2, 4, 2, 5]
capacity = 10


def knapsack():
    n = len(value)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n+1)]

    for v in range(1, n+1):
        for w in range(1, capacity+1):
            if w >= weight[v-1]:
                dp[v][w] = max(dp[v-1][w],
                               value[v-1] + dp[v-1][w - weight[v-1]])
                
                print(w - weight[v-1],w - weight[v-1])
            else:
                dp[v][w] = dp[v-1][w]

    for row in dp:
        print(row)
    print(dp[n][capacity])
knapsack()
