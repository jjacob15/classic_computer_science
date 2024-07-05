def can_sum(target, arr, memo={}):
    if target in memo: return memo[target]
    if target < 0: return False
    if target == 0: return True
    
    for i in range(len(arr)):
        remainder = target - arr[i]
        if can_sum(remainder, arr, memo):
            memo[target] = True
            return True;

    memo[target] = False
    return False


def can_sum_tab(target,arr):
    dp = [False for _ in range(target+1)]
    dp[0] = True

    for i in range(target):
        if dp[i]:
            for num in arr:
                if i + num  <= target:
                    dp[i+num] = True

    return dp[target]

    