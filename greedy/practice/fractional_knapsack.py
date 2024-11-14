# values= [60,100,120]
# weights= [10,20,30]
# capacity = 50

values= [500]
weights= [30]
capacity = 10

def fractional_knapsack():
    global capacity
    print(values,weights,capacity)
    ratio = [(v/w,w) for v,w in zip(values,weights)]
    print(ratio)

    
    max_value =0

    ratio.sort(reverse=True, key=lambda x: x[0])
    print(ratio)
    for v,w in ratio:
        if w <= capacity:
            max_value += v*w
            capacity -= w
        else:
            max_value += v*capacity
            break
            
        
    

    print(max_value)


fractional_knapsack()
