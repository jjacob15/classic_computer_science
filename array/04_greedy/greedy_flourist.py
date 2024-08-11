# A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new
#  customers and the money he makes. To do this, he decides he'll multiply the price of each flower by the
#  number of that customer's previously purchased flowers plus . The first flower will be original price,
#  the next will be (1+1)* c0st and so on.

# So 3 friends buying flowers[1,2,3,4], would buy 4,3 and 2 are original price. Then one friend should buy the 
# last flower at price 1 at (1+1)*1 = 2 so the total is 4+3+2+2 = 11
#
# INSIGHT -> When you notice cyclic patterns using modulus,. When you hit a modulus of zero, increment the 
# multiplier 
# the idea here is each person buys one flower as the base cost, then the second round, we increment the
# multiplier by one and run. Say 3 people have to buy flowers [1,2,3,4]. The 3 

# The best way to do that is modulus,
#  as i%k will be zero each time we finish one group. The only caveat is the ignore 
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