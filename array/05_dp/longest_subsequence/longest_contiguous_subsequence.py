# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
#INSIGHT -> for subsequeuce, if no match, top or left value, else diagonal value.
#     a c e
#   1 0 0 0
# a 1 1 0 0
# b 1 0 0 0
# c 1 0 0 0
# d 1 0 0 0
# e 1 0 0 0

#     a b
#   1 0 0
# a 1 1 0
# b 1 1 1
# c 1 0 0
# d 1 0 0
# e 1 0 0

 
def longestCommonSubsequence(text1,text2):
    dp = [[1]+[0]*(len(text2)) for _ in range(len(text1)+1)]
    # print(dp)
    for i in range(1,len(text1)+1):        
        for j in range(1,len(text2)+1):        
            # print(text1[i-1],text2[j-1])
            if text1[i-1] == text2[j-1]:
                # means take the LCS for the last i-1 and j-1 string size
                dp[i][j] = min(dp[i-1][j-1], 1) #
    print(max([row[-1] for row in dp]))
    return max([row[-1] for row in dp])

longestCommonSubsequence("abcde","ace") #NO
longestCommonSubsequence("abc","ab") #YES
longestCommonSubsequence("abc","def") #NO
longestCommonSubsequence("abcbcba","abcb") #YES
longestCommonSubsequence("111abcb111","abcb") #YES
