# [3,1,2] -> the subsequences of this arr are
# {}
# 3
# 1
# 2
# 3,1
# 1,2
# 3,2
# 3,1,2 -> note order. It cannot be 321

#INSIGHT-> when you draw the decision tree you will recognize that you need the index to know when you are at the bottom so the base 
# case is when i >= n break



def subsequences(i,arr,n,take,result=[]):
    # with any subsequence, you want to go down the full depth of the decision tree before you take the next element
    # therefore the base case is checking the lenght of the arr
    if i >=n:
        print(result)
        return 
    result.append(arr[i])
    subsequences(i+1,arr,n,"take",result)
    result.pop()
    subsequences(i+1,arr,n,"not take",result)

subsequences(0,[3,1,2],3,"start")



def sum_subsequences(i,arr,n,result=[]):
    if i >=n:
        if sum(result) == 2:
            print(result)
        return 
    result.append(arr[i])
    sum_subsequences(i+1,arr,n,result)
    result.pop()
    sum_subsequences(i+1,arr,n,result)

# sum_subsequences(0,[1,1,2],3)

#INSIGHT -> returning a True will replace the function with True, and that breaks the recursion.
def one_sum_subsequences(i,arr,n,result=[]):
    if i >=n:
        if sum(result) == 2:
            print(result)
            return True
        else:
            return False
    result.append(arr[i])
    if one_sum_subsequences(i+1,arr,n,result):
        return True
    result.pop()
    if one_sum_subsequences(i+1,arr,n,result):
        return True

# one_sum_subsequences(0,[1,1,2],3)

# to count keep track of count of l and r and return sum.
def count_sum_subsequences(i,arr,n,result=[]):
    if i >=n:
        if sum(result) == 2:
            return 1
        return 0
    result.append(arr[i])
    l = count_sum_subsequences(i+1,arr,n,result)
    result.pop()
    r = count_sum_subsequences(i+1, arr, n, result)
    return l + r

c = count_sum_subsequences(0,[1,1,2],3)
# print(c)