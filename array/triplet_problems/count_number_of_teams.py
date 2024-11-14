
# Count Number of Teams
# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

# Example 1:

# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
# Example 2:

# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
# Example 3:

# Input: rating = [1,2,3,4]
# Output: 4
# Subsequence

# INSIGHT->backtracking works but get TLE
# INSIGHT->This is a triplet problem. You start at index 1 and count values less that to the left and greater than tot he right. MULTIPLYING LEFT AND RIGHT GIVES YOU THE NUMBER OF
# COMBOS



def numTeams(ratings):
    n = len(ratings)
    result = 0
    for i in range(1,n-1):
        left_lesser = right_greater =0
        for j in range(i):
            if ratings[j] < ratings[i]:
                left_lesser+=1
                print("lesser",ratings[j],"than",ratings[i])

        for j in range(i+1,n):
            if ratings[j] > ratings[i]:
                right_greater+=1
                print("greater",ratings[j],"than",ratings[i])
        result += left_lesser * right_greater


        left_greater = i - left_lesser #straight forward i - left lesser gives you all greater than below i
        right_lesser = n - i - 1 - right_greater #n -i -1 (to remove the middle element) - the right greater
        result += left_greater * right_lesser

    return result



numTeams([2,5,3,4,1])