#the idea is to use all the values once based on their weights
#and fit to the max capacity.
#to find the best values by weight, you find its ratio v/w
# order by desc.
# iterating through the ratios, you get each item by their ratio and reduce capacity

def fractional_knapsack(values, weights, capacity):
    # Calculate value to weight ratio
    ratio = [(v / w, w) for v, w in zip(values, weights)]
    
    # print(ratio)
    # Sort items by value to weight ratio in descending order
    ratio.sort(reverse=True, key=lambda x: x[0])
    # print(ratio)

    max_value = 0
    for r, w in ratio:
        if capacity >= w:
            max_value += r * w
            capacity -= w
            # print("adding", r, w,capacity)
        else:
            max_value += r * capacity
            # print("else adding", r, capacity)
            break

    return max_value

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
