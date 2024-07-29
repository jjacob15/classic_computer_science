# INSIGHT HERE IS IF ITS A PREDETERMINED SET OF VALUES YOU ARE LOOKING FOR, COMPUTE THE VALUE FIRST
# AND CHECK IF YOUR ARRAY HAS THAT VALUE. Instead of the other way around.
# we keep two dict, one with the v2 value and another with v3 from v2. If the value of k existss in v3 count+1

from collections import defaultdict

def counting_triplets(arr,r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)

    count =0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1
        
    return count