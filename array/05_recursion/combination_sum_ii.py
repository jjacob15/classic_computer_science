# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

def combintationSum2(arr,target):
    result = []
    arr.sort() #sorting so we can exclude adjacent like values.
    def backtrack(remaining,idx,combination):
        if remaining == 0:
            result.append(list(combination))
            return 
        
        if idx ==len(arr) or remaining < 0:
            return
        
        combination.append(arr[idx])
        backtrack(remaining - arr[idx],idx,combination) 
        combination.remove(arr[idx])
        next_idx = idx+1 #as usual, but keep it in here.
        while next_idx <len(arr) and arr[idx] == arr[next_idx]:
            next_idx+=1 # while current idx and next one is the same increment the idx.
        backtrack(remaining,next_idx,combination) 

    backtrack(target,0,[])


    print(result)
        


ans= combintationSum2([1,1,1,2,2],4)
print(ans)
