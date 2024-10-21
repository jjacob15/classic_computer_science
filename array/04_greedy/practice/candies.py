arr = [4,6,4,5,6,2]
# she should give [1,2,1,2,3,1], so total it to 10 candies.
arr = [2,4,2,6,1,7,8,9,2,1]
# result 19


def candies(arr):
    r = [1]* len(arr)
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            r[i] = r[i-1]+1

    for i in range(len(arr)-2,-1,-1):
        if arr[i] > arr[i+1] and r[i] <= r[i+1]:
            r[i] = r[i+1]+1

    return sum(r)


print(candies(arr))