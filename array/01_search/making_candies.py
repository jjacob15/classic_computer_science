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

def computeCandiesOnPass(m,w,p,target, passCount):
    
    candiesMade =0
    while candiesMade < target:
        candiesMade += m * w
        if candiesMade >= target //2:
            continue
        candiesMadeHalf = candiesMade // 2
        if m < w:
            m+= candiesMadeHalf
            candiesMade -= candiesMadeHalf
        
            
