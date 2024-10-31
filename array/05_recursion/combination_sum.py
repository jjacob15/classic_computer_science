def combintationSum(arr,target):
    result = []

    def backtrack(idx,remain,comb):
        if idx == len(arr):
            return
        if remain == target:
            result.append(list(comb))
        
        for i in range(idx,len(arr)):
            comb.append(arr[i])
            backtrack(i+1,target -arr[i],comb)
            comb.pop()


    backtrack(0,target,[])

    return result
    
    
ans= combintationSum([2,3,5],8)
print(ans)
