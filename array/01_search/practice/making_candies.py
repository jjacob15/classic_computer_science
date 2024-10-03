# machines = 1
# workers = 2
# price = 1 
# target = 60

# 1 x 2 = 2 candies and 2 machines
# 3 x 2 = 6 candies add 2 machines
# 6 x 5 = 30 candies add 3 machines and 3 workers
# 6 x 5 = 30 + 30 
import math
def canProduceCandiesInRound(machines,workers, price, target, round):
    if machines >= math.ceil(target/workers):
        return True
    production = machines * workers

    while True:
        remainder = target - production
        rounds_to_remainder = math.ceil(remainder/(machines * workers))
        if rounds_to_remainder <= round:
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
        if canProduceCandiesInRound(machines,workers,cost,target,mid):
            r = mid
        else:
            l = mid +1
    return l



