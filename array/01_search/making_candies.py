# Karl loves playing games on social networking sites. His current favorite is CandyMaker, where the goal
#  is to make candies. Karl just started a level in which he must accumulate n  candies starting with m  
# machines and w workers. In a single pass, he can make m x w candies. After each pass, he can decide
#  whether to spend some of his candies to buy more machines or hire more workers. Buying a machine or
#  hiring a worker costs p units, and there is no limit to the number of machines he can own or workers he
#  can employ.

# m = 1
# w = 2
# p = 1 
# n = 60

# 1 x 2 = 2 candies and 2 machines
# 3 x 2 = 6 candies add 2 machines
# 6 x 5 = 30 candies add 3 machines and 3 workers
# 6 x 5 = 30 + 30 

# it takes 4 passes
# INSIGHTS -> Ceiling Division. Use ceiling division to find the how many resources are needed to meet a 
# target. Instead of 10/3 = 3.333 math.ceil(10/3) = 4. This will take care of the partial effort and make more sense.
# INSIGHTS -> instead of incrementally working to the target, always use division to find the remainder. Here 
# when  production < cost, we find the difference then do remainder /(machine * workers) to find the remaining rounds.
# This greatly enhances performance

import math
def canProduceCandiesInRounds(machines,workers,price,target, rounds):
    if machines >= math.ceil(target/workers):
        return True
    
    production = machines * workers
    rounds -= 1
    if rounds == 0:
        return False
    
    while True:
        remainder = target - production
        rounds_to_remainder = math.ceil(remainder/(machines*workers))
        if rounds_to_remainder <= rounds:
            return True
        
        if production < price:
            remainder = price - production
            rounds_to_remainder = math.ceil(remainder/(machines*workers))
            rounds  -= rounds_to_remainder
            if rounds < 1:
                return False
            production += rounds_to_remainder * machines * workers
        
        production -= price

        if machines > workers:
            workers+=1
        else:
            machines+=1
    
    return False

def minimumPasses(machines, workers, cost, target):
    # Write your code here
    l, r = 1,10**12
    while l < r:
        mid = (l+r)//2
        if canProduceCandiesInRounds(machines,workers,cost,target,mid):
            r = mid
        else:
            l = mid +1
    return l
