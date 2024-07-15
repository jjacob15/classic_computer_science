def countSwaps(a):
    # Write your code here
    swap = 0
    breakLoop = True
    
    while True:
        if not breakLoop:
            break
        breakLoop = False
        for i in range(1, len(a)):
            if a[i-1] > a[i]:
                a[i-1],a[i] = a[i],a[i-1]
                swap +=1
                breakLoop = True

    print(f"Array is sorted in {swap} swaps.")      
    print(f"First Element: {a[0]}") 
    print(f"Last Element: {a[-1]}") 


countSwaps([6,4,1])