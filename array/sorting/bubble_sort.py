#complexity is (n2) in the worst and average case. Space complexity is O(1) as it only requires same amount of space
def bubble_sort(arr):

    swap = True
    while True:
        if not swap: break
        swap = False
        for i in range(len(arr)-2):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
                swap = True

    return arr


