def  count(arr,target):
    prefix={}
    prefix_sum =0
    total_count =0
    for n in arr:
        prefix_sum += n
        if prefix_sum == target:
            total_count +=1
        if prefix_sum - target in prefix:
            total_count += 1

        prefix[prefix_sum] =1

    print(total_count)

count([3,1,2,4],6)