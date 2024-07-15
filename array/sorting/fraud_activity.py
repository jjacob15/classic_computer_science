import heapq
def fraud(expenditure,d):
    def add(num,low,high):
        if not low or num <= -low[0]:
            heapq.heappush(low, -num)
        else:
            heapq.heappush(high, num)
        balance(low, high)

    def remove(num,low,high):
        if num <=-low[0]:
            low.remove(-num)
            heapq.heapify(low)
        else:
            high.remove(num)
            heapq.heapify(high)
        balance(low,high)
        
    def balance(low,high):
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))


    def get_median(low,high,d):
        if d%2==1:
            return -low[0]
        return (-low[0] + high[0]) / 2

    notification =0
    low,high = [],[]

    print(d)
    for num in expenditure[:d]:
        add(num, low, high)

    for i in range(d,len(expenditure)):
        median = get_median(low,high,d)
        print(median, low, high)    
        if expenditure[i] >=2 *median:
            notification+=1
        
        remove(expenditure[i-d],low,high)
        add(expenditure[i], low, high)

        print(low,high)            

    return notification












def fraud_with_array(expenditure,d):
    def get_median(counts,d):
        count =0
        median_pos = (d//2) + 1
        if d%2==0:
            first = None
            for i,c in enumerate(counts):
                count += c
                if count >= median_pos and first is None:
                    first = i
                if count >= median_pos:
                    return (first + i)/2
        else:
            for i, c in enumerate(counts):
                count +=c
                if count >=  median_pos:
                    return i
    
    count = [0] * 201
    notification = 0
    for i in range(d):
        count[expenditure[i]] +=1
    
    for i in range(d,len(expenditure)):
        median = get_median(count,d)
        if expenditure[i] >= median * 2:
            notification +=1

        count[expenditure[i]] +=1
        count[expenditure[i-d]] -=1

    return notification
