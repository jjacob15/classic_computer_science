#the obj is to find the min difference between the values of the array
# INSIGHT ->  THE MIN DIFFERENCE BETWEEN TWO ELEMENTS CAN ONLY BE BETWEEN TWO ADJACANT VALUES
#SO SORT THE ARRAY AND THEN DO THE CHECK.
def minimumAbsoluteDifference(arr):
    arr.sort()
    
    min_diff = float("inf") 
    for i in range(len(arr)-1):
        diff = arr[i] - arr[i+1]
        if abs(diff) < min_diff:
            min_diff = abs(diff)
            
    return min_diff