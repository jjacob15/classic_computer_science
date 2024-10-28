# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    
    # Initialize the dp table with size (m+1)x(n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the base cases
    for i in range(m + 1):
        dp[i][0] = i  # Deletion cost for word1 to become empty
    for j in range(n + 1):
        dp[0][j] = j  # Insertion cost to form word2 from an empty string
    
    # Populate the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j],    # Delete
                               dp[i][j - 1],    # Insert
                               dp[i - 1][j - 1] # Replace
                              ) + 1
    
    for row in dp:
        print(row)
    # The minimum edit distance
    return dp[m][n]



# minDistance("horse","ros")
# minDistance("cats","cat")
minDistance("cat456","cat123")