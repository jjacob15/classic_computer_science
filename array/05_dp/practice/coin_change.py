# Function to calculate the total distinct ways to make a sum using n coins of different denominations
def coin_change(coins,target):
    dp = [float("inf")] * (target+1)
    dp[0] = 0

# def count_ways_to_make_change(coins, target):
#     # Initialize DP array to store number of ways to make each amount
#     dp = [0] * (target + 1)
#     dp[0] = 1  # Base case: 1 way to make amount 0 (using no coins)

#     # Iterate over each coin
#     for coin in coins:
#         # For each coin, update the ways for all amounts from coin to target
#         for amount in range(coin, target + 1):
#             dp[amount] += dp[amount - coin]
    
#     print(dp)
#     # dp[target] will contain the number of ways to make the target amount
#     return dp[target]

# def coin_change(coins, target):
#     # Initialize DP array with "infinity" values
#     dp = [float('inf')] * (target + 1)
#     dp[0] = 0  # Base case: 0 coins needed to make amount 0
    
#     # Iterate over each coin
#     for coin in coins:
#         # Iterate over all possible amounts from coin to target
#         for amount in range(coin, target + 1):
#             dp[amount] = min(dp[amount], dp[amount - coin] + 1)
#             print(coin, amount,dp)
    
#     print(dp)

#     # If dp[target] is still infinity, return -1 (impossible to form the target amount)
#     return dp[target] if dp[target] != float('inf') else -1


# Driver Code
if __name__ == "__main__":
    coins = [1, 2, 3]
    target_sum = 5
    print(coin_change(coins, target_sum))
    # print(count_ways_to_make_change(coins, target_sum))