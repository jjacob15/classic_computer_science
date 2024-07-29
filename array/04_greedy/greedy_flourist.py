# the idea here is each person buys one flower as the base cost, then the second round, we increment the
# multiplier by one and run. 
# The best way to do that is modulus, as i%k will be zero each time we finish one group. The only caveat is the ignore 
# the first case when i == 0
def  greedy_flourist(k,c):
    c.sort(reverse=True)
    total_cost = 0
    multi = 1
    for i in range(len(c)):
        if i % k == 0 and i > 0:
            multi += 1        
        total_cost += multi * c[i]
    
    return total_cost