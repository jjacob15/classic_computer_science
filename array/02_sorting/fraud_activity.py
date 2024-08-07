# If the amount spent by a client on a particular day is greater than or equal to  the client's median
#  spending for a trailing number of days, they send the client a notification about potential fraud.
#  The bank doesn't send the client any notifications until they have at least that trailing number of 
# prior days' transaction data.

# INSIGHT -> efficient ways to get median of a set of values.
# INSIGHT -> If values are within a known range,such as [0...200] use the counting sort technique.
    # You create an array with that range, and then for each position the element exists, you add one. If you are iterating through a window, add the last 
    # value and decrement the front value. So for an array of [3,2,3,2,5] -> iterate and create [0,0,2,2,0,1] 
    # which equates to 2 "2"s and 2 "3"s and 1 "5"
    # to get a median out of this array, first check the len of the input array [3,2,3,2,5] is even
    # for even cases you want the (median pos + median pos +1) /2
    # for odd cases just median pos value.
    # median pos = len//2 +1

#   ELSE use a min max heapq.
    # two arrays, low and high. Where the high queue is adding value normally so when you pop, you get the least value. 
    # The low queue, adds value with inverted sign to pop the highest value.
    # to add if the num is less than or equal to the - low[0](because values are negative here) the heappush into here
    # else push to high array and BALANCE.
    # balance takes both the high and low and if len(low) > len(high) +1
    # pushpop from low and insert into high else the other way around.
    # median is for even -low[0] +high[0] /2 else -low[0]




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

    for num in expenditure[:d]:
        add(num, low, high)

    for i in range(d,len(expenditure)):
        median = get_median(low,high,d)
        if expenditure[i] >=2 *median:
            notification+=1
        
        remove(expenditure[i-d],low,high)
        add(expenditure[i], low, high)

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
