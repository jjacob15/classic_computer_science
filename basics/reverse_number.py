def reverse_number(num):
    result = 0
    while num != 0:
        mod = num % 10
        result = result * 10 + mod
        num = num // 10
    return result
reverse_number(123456)