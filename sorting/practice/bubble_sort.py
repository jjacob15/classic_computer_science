def bubble_sort(arr):
    swap = True
    while True:
        if not swap:
            break

        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
                swap = True

    return arr


arr =[32,22,1,5,2,4,12,4,7,23,4,332]
print(bubble_sort(arr))