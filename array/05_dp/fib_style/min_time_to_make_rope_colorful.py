# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

# Return the minimum time Bob needs to make the rope colorful.

# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.

# INSIGHT -> the neededTime[i] is updated dynamically to store the maximum time for the current "block" of same-colored balloons. This is an efficient way to track decisions and ensures that you don’t need additional space or a complex data structure to manage the solution.

# bbbb [5,4,8,1]
# becomes
# bbbb [ 5, 5, 8, 8]
# instead of worrying about pointers when you take 4 instead of 5, just replace 4 with 5 and you will have sorted the problem of tracking what you used.

from typing import List

def minCost(colors: str, neededTime: List[int]) -> int:
    totalTime = 0
    n = len(colors)
    
    # Iterate over the colors
    for i in range(1, n):
        # If two adjacent balloons have the same color
        if colors[i] == colors[i - 1]:
            # Remove the one with the smaller neededTime
            totalTime += min(neededTime[i], neededTime[i - 1])
            # Keep the larger neededTime for the next comparison
            neededTime[i] = max(neededTime[i], neededTime[i - 1])

    return totalTime


minCost("abaac",[1,2,3,4,5]) #3
minCost("abc",[1,2,3]) #0
minCost("aabaa",[1,2,3,4,1]) #2
minCost("aaabbbabbbb",[3,5,10,7,5,3,5,5,4,8,1]) #26