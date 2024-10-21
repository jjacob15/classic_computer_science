# two pointer technique with a sorted array. left and right and the the left + right > target reduce right or else increase left
def find_sum(arr, target):
    left = 0
    right = len(arr) - 1
    found = False
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            found = True
            break
        elif target < s:
            right -= 1
        else:
            left += 1

    return found
