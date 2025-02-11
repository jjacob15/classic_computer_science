def move_zeros_to_end(arr):
    slow =0
    for fast in range(1,len(arr)):
        if arr[fast] != 0:
            print(slow)
            slow+=1
            arr[slow],arr[fast] = arr[fast],arr[slow]
            print(arr)
    print(arr)
    pass

# move_zeros_to_end([ 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1])
move_zeros_to_end([ 1 ,2 ,3 ,0 ,4 ,0 ,1])