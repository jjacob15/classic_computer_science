def fraud(expenditure,d):
    isEven = d % 2 == 0
    window = sorted(expenditure[:d])
    notices = 0

    def insert_sorted(arr, value):
        for i in range(len(arr)):
            if value < arr[i]:
                arr.insert(i, value)
                return
        arr.append(value)

    for i in range(d, len(expenditure)):
        medianTransaction = 0
        if isEven:
            medianTransaction = (window[d//2 - 1] + window[d//2]) / 2
        else:
            medianTransaction = window[d//2]
        
        if expenditure[i] >= medianTransaction * 2:
            notices += 1
        
        # Update the window
        window.remove(expenditure[i - d])
        insert_sorted(window, expenditure[i])
    
    return notices