# finding a common child is by using a 2D array of len + 1
# start from 1 and if the last two characters match increment size by one
# else take max of up or left positions

def common_child(s1,s2):
  #     A B C D
  #   0 0 0 0 0
  # A 0 1 1 1 1
  # B 0 1 1 2 2
  # D 0 1 1 2 3
  # C 0 1 1 2 3

  n, m = len(s1), len(s2)
  dp = [[0] * (m+1) for _ in range(n+1)]
  
  for i in range(1, n + 1): # start 1 position ahead of s1 and s2
      for j in range(1, m + 1):
          if s1[i-1] == s2[j-1]: # if the two characters are same, take the old value and increment one
              dp[i][j] = dp[i-1][j-1] + 1
          else:
              dp[i][j] = max(dp[i-1][j], dp[i][j-1]) #or take max of i-1 or j-1
#   print(dp)
  return dp[n][m]
