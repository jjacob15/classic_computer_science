
def print_n_times(n):
    if n < 1:
        return
    
    print(n,"jaison")
    print_n_times(n-1)

# print_n_times(5)

def print_n_times_backtracking(n):
    if n < 1:
        return
    
    print_n_times_backtracking(n-1) #INSIGHT -> backtracking is the idea of going down to the base case and then invoking the result of the function. Like merge sort. 
    #you work from the bottom up.
    print(n,"jaison")

# print_n_times_backtracking(5)


def sum_of_n(n,total):
    if n == 0:
        print(total)
        return
    
    sum_of_n(n-1,total+n)

# sum_of_n(10,0)    

def swap(arr):
    def swap_internal(arr,l,r):
        if l>=r:
            return;

        arr[l],arr[r] = arr[r],arr[l]
        swap_internal(arr,l+1,r-1)
    swap_internal(arr,0,len(arr)-1)

    print(arr)

# swap([1,2,3,4,5,6,7,8,9,10]) 


def is_palindrome(str):
    def internal(i,str,n):
        if i >= n//2:
            return True
        if str[i] != str[n-i-1]: return False
        
        return internal(i+1,str,n)  #INSIGHT think of internal(i+1,str,n) becoming True when it reaches the base case. so return True.
    return internal(0,str,len(str))

# result = is_palindrome("repaper")
# print(result)
# result = is_palindrome("repaper1")
# print(result)
#0(2^n*n) because for each element there are 2 choices. The final n is the result.append and copy

#INSIGHT -> this is a subsequence. only one directional 
def findSubsequence(arr):
    result = []

    def backtrack(index,current):
        if index == len(arr):
            result.append(list(current))
            return

        current.append(arr[index])
        backtrack(index+1,current)
        current.pop()
        backtrack(index+1,current)

    backtrack(0,[])
    return result


print(findSubsequence([3,1,2]))