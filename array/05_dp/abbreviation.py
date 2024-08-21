# daBcd, ABC. check if ABC can be constructed from daBcd. you can delete and make character uppercase. You can only delete lowercase a not upper.
# INSIGHT -> as with every dp, you fill the 2D array if the condition is met for that row and column and if the next condition fails,
#  you look up the last i-1 and j-1 and pick that value.
# Here the condtions are 
#   if the values match then 1
#   if lower of b == a then take the last column,row value or last row value.
#   if a is upper then zero
#   else last row value.


#     A B D E
#   1 0 0 0 0
# A 1 1 0 0 0
# b 1 1 1 0 0
# c 1 1 1 0 0
# D 1 0 0 1 0
# E 1 0 0 0 1
 
#     A F D E
#   1 0 0 0 0
# A 1 1 0 0 0
# b 1 1 0 0 0
# c 1 1 0 0 0
# D 1 0 0 0 0
# E 1 0 0 0 0


def abb(a,b):
    # Write your code here
    # Write your code here
    # print(a,b)
    dp=[ [1]+ [0]*(len(b)) for i in range(len(a)+1)]
    # dp[i][0] always 1('YES') cuz b got 0 length
    
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                # same upper case
                dp[i][j]=dp[i-1][j-1]
            elif a[i-1]==b[j-1].lower():
                # same lower case
                dp[i][j]=max(dp[i-1][j-1], dp[i-1][j])
            elif a[i-1].isupper():
                dp[i][j]=0
            else:
                dp[i][j]=dp[i-1][j]

    # for arr in dp:
    #     print(arr)

    if dp[len(a)][len(b)]:
        return 'YES'
    else:
        return 'NO'    

