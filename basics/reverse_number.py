#insight - As modulus gives you the remainder, modulus of 10 with give you the last element. Even if its zero. 
# instead of subtracting, use floor divide to remove the tail number
def reverse_number(num):
    result = 0
    while num != 0:
        mod = num % 10
        result = result * 10
        result += mod
        num = num // 10
    print(result)
    return result
reverse_number(123456)