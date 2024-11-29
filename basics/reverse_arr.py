def reverse_arr(arr):
    # print(arr[::-1])
    def swap(arr, l, r):
        if l > r:
            print(arr)
            return
        arr[l],arr[r] = arr[r],arr[l]
        swap(arr,l+1,r-1)
    swap(arr, 0, len(arr)-1)


reverse_arr([1, 2, 3, 4,5])