# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
#INSIGHT -> for subsequeuce, if no match, top or left value, else diagonal value. Diagonal value indicates the last characters matched.
#     a c e
#   0 0 0 0
# a 0 1 1 1
# b 0 1 1 1
# c 0 1 2 2
# d 0 1 2 2
# e 0 1 2 3

 
def longestCommonSubsequence(text1,text2):
    dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

    # print(dp)
    for i in range(1,len(text1)+1):        
        for j in range(1,len(text2)+1):        
            # print(text1[i-1],text2[j-1])
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1 #means take the LCS for the last i-1 and j-1 string size
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    print(dp[-1][-1])
    return dp[-1][-1]

longestCommonSubsequence("abcde","ace") #3
longestCommonSubsequence("abc","abc") #3
longestCommonSubsequence("abc","def") #0
longestCommonSubsequence("bl","yby") #1
longestCommonSubsequence("abcba","abcbcba") #5
longestCommonSubsequence("bsb","b") #1
longestCommonSubsequence("b","bsb") #1
longestCommonSubsequence("bsbininm","jmjkbkjkv") #1
