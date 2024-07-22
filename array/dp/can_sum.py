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
    dp1 = [False for _ in range(target+1)]
    dp[0] = True #keep base case as True
    dp1[0] = (0,True) #keep base case as True

    print(target,arr)
    #the idea is the iterate through each number until you reach the target
    #at each position
    for i in range(target):
        if dp[i]: # if value exists in dp 
            for num in arr: #iterate through the values
                if i + num  <= target:
                    dp[i+num] = True #
                    dp1[i+num] = (i+num,True)
    # print(dp1)
    return dp[target]

    