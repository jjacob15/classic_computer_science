# You need to maximize the profit. You can only rob non adjacent homes as it would trigger the alarm.
#INSIGHT -> when you define the base cases, don't worry about any conditions. If you use or disuse values from your tabulations
# depends on the state i of the iteration.
def house_robber(nums):
    dp  = [0] *(len(nums))

    dp[0] = nums[0] # think of the base case as if only one house was available you would rob that no matter what
    dp[1] = max(nums[0],nums[1]) #think if only two houses were avaiable you would either rob the first one or 
                                 #the second one. Not both 

    for i in range(2,len(nums)):
        dp[i] = max(dp[i-1],dp[i-2]+nums[i]) # you are looking the max of last hour or the 2 house behind you + current


    return dp[-1]


print(house_robber([1,2,3,1]))
print(house_robber([2,7,9,3,1]))