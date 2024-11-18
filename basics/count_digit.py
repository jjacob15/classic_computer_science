def count_digit(num):
    m = 10
    result = num
    length = 0
    while result % m != num:
        length+=1
        m = m * 10
    print(length + 1)
    return length + 1

count_digit(0)