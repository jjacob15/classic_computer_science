                                
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
# to check the right node. 
#INSIGHT -> unlike subsequence, if you draw the decision tree, as we can use one number any number of times, you don't use the idx to check the levels of the tree,
# but use remaining to check if its under zero to break. we also check if the idx hit the end of the arr to stop.

def combintationSum(arr,target):
    result = []
    
    def backtrack(remaining,idx,combination):
        print("trying",combination)
        if remaining == 0:
            result.append(list(combination))
            return 
        
        if idx ==len(arr) or remaining < 0:
            return
        
        combination.append(arr[idx])
        backtrack(remaining - arr[idx],idx,combination) 
        print("Backtrack",idx+1)
        combination.remove(arr[idx])
        backtrack(remaining,idx+1,combination) #even though we increased the index, we are not using the second value here,
        # we evaluate [2,2,2] first then start with adding that next idx value

    backtrack(target,0,[])


    print(result)
        


ans= combintationSum([2,3,5],8)
print(ans)
