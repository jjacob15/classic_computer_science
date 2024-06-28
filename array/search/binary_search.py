def binary_search(arr, item):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == item:
            return mid
        elif item < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


print(binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43], 5))
print(binary_search([1,3,5,7,8,12,15,23,43],4))
print(binary_search([1,3,5,7,8,12,15,23,43,56,68,87],56))
print(binary_search([1,3,5,7,8,12,15,23,43,56,68,87],87))
print(binary_search([1,3,5,7,8,12,15,23,43,56,68,87],1))
print(binary_search([1,3,5,7,8,12,15,23,43,56,68,87],86))
