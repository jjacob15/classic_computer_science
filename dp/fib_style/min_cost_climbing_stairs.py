# you are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

#INSIGHT -> we figured we needed the min.
# as we compute the cost for the last two steps, you look back accordingly. for 1 step you look dp[i-1] or dp[i-2] for two steps

def min_cost_climbing_stairs(costs):
    n = len(costs)
    dp =  [0] * (len(costs) + 1)
    if n == 1:
        return 0;

    for i in range(2, len(costs) + 1):
        take_one_step = dp[i - 1] + costs[i - 1]
        take_two_steps = dp[i - 2] + costs[i - 2]
        dp[i] = min(take_one_step, take_two_steps)
    print(dp)
    return dp[-1]



# min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1]) == 6
# min_cost_climbing_stairs([10,15,20]) == 15
min_cost_climbing_stairs([0,1,2,3,4,5]) == 15