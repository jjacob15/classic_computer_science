def how_sum(target, arr, memo=None):
    if memo is None:
        memo = {}
    if target in memo: return memo[target]
    if target < 0: return None
    if target == 0: return []
    
    for i in range(len(arr)):
        remainder = target - arr[i]
        result_arr = how_sum(remainder, arr, memo)
        if result_arr != None:
            result_arr.append(arr[i])
            memo[target] = result_arr
            return memo[target] 
    
    memo[target] = None
    return memo[target]


def how_sum_tab(target,nums):
    dp = [None for _ in range(target+1)]
    dp[0] =[]
    
    for i in range(target):
        if dp[i] is not None:
            for num in nums:
                if i+num <= target:
                    copy = [*dp[i]]
                    copy.append(num)
                    dp[i+num] = copy

    return dp[target]

def how_sum_tab_all(target,nums):
    dp = [None for _ in range(target+1)]
    dp[0] =[[]]
    
    for i in range(target):
        if dp[i] is not None:
            for num in nums:
                if i+num <= target:
                    for arr in dp[i]:
                        copy = [*arr]
                        copy.append(num)
                        if dp[i+num] is None: dp[i+num] = []
                        dp[i+num].append(copy)  

    return dp[target]