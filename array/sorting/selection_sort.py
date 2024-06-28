# complexity is O(n2) in the worst and average case. Space complexity is O(1) as it only requires same amount of space
def selection_sort(arr):
    for i in range(len(arr)):
        mi = i
        for j in range(i,len(arr)):
            if arr[j] < arr[mi]:
                mi = j

        if mi == i: continue
        arr[i],arr[mi] = arr[mi],arr[i]

    return arr
