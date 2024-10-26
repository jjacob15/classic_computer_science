def climbing_stairs(n,memo=None):
    if memo is None:
        memo = {}

    if n in memo: 
        return memo[n]
    if n < 0: return None
    if n == 0: return [[]]

    all_results = []
    for step in [1,2]:
        completed_step = n - step
        result = climbing_stairs(completed_step,memo)
        if result is not None:
            memo[completed_step] = result
            for a in result:
                a.append(step)
                all_results.append(a)
        else:
            memo[completed_step] = result
    return all_results

def climbing_stairs_count(n,memo=None):
    if memo is None:
        memo = {}
    if n in memo: return memo[n]
    if n < 0: return None
    if n == 0: return [[]]

    choices = 0
    for step in [1,2]:
        completed_step = n - step
        result = climbing_stairs(completed_step)
        memo[completed_step] = result
        if result is not None:
            for a in result:
                a.append(step)
                choices+=1

    return choices

#INSIGHT -> for 1 stair there is only one way to get there. for two there are two ways to get there. 
# Now counting back, its fib
def climbing_stairs_tabluation(n):
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2

    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i - 2]

    return dp[-1]

print(climbing_stairs_tabluation(2))
print(climbing_stairs_tabluation(3))