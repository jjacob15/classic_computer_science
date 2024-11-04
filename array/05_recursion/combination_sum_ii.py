# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
# 0(2^n*n)
def combintationSum2(arr,target):
    result = []
    arr.sort() #sorting so we can exclude adjacent like values.
    def backtrack(start, remaining,combination):
        # print(start,remaining,combination)
        if remaining == 0:
            result.append(list(combination))
            return 
        
        if  remaining < 0:
            return
        
        for i in range(start, len(arr)):
            if i > start and arr[i-1]==arr[i]:
                continue
            combination.append(arr[i])
            backtrack(i+1, remaining - arr[i],combination) 
            combination.pop()
    

    backtrack(0,target,[])


    print(result)

# def combintationSum2(arr,target):
#     result = []
#     arr.sort() #sorting so we can exclude adjacent like values.
#     def backtrack(remaining,idx,combination):
#         if remaining == 0:
#             result.append(list(combination))
#             return 
        
#         if idx ==len(arr) or remaining < 0:
#             return
        
#         combination.append(arr[idx])
#         backtrack(remaining - arr[idx],idx,combination) 
#         combination.remove(arr[idx])
#         next_idx = idx+1 #as usual, but keep it in here.
#         while next_idx <len(arr) and arr[idx] == arr[next_idx]:
#             next_idx+=1 # while current idx and next one is the same increment the idx.
#         backtrack(remaining,next_idx,combination) 

#     backtrack(target,0,[])


#     print(result)
        


ans= combintationSum2([2,5,1,4,3],10)
# ans= combintationSum2([2,5,2,1,2],5)
# print(ans)
