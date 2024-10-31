                                
#                                 candidates = [2, 3] and target = 4

#                                              findCombinations(0, 4, [])
#                                    /                                      \
#                         Include 2 /                                        \ Exclude 2
#                                  /                                          \
#               findCombinations(0, 2, [2])                                    findCombinations(1, 4, [])
#                      /              \                                               /          \
#         Include 2 /                  \ Exclude 2                          Include 3 /           \ Exclude 3
#                  /                    \                                             /             \
# findCombinations(0, 0, [2, 2])   findCombinations(1, 2, [2])   findCombinations(1, 1, [3])   findCombinations(2, 4, [])

#                 |                     |                       |                         |
#                [2, 2]             (invalid)               (invalid)                 (invalid)


#INSIGHT-> this is DFS using  backtracking. when you hit the leaf, you backtrack, exlude the last item and then DO NOT CHANGE THE REMAINING. This is
# to now try with the right node. 

def combintationSum(arr,target):
    result = []
    
    def backtrack(remaining,start,combination):
        if remaining == 0:
            result.append(list(combination))
            return 
        
        if start ==len(arr) or remaining < 0:
            return
        
        combination.append(arr[start])
        backtrack(remaining - arr[start],start,combination) 
        combination.remove(arr[start])
        print(remaining,combination)
        backtrack(remaining,start+1,combination)

    backtrack(target,0,[])


    print(result)
        


ans= combintationSum([2,3,5],8)
print(ans)
