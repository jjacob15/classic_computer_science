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