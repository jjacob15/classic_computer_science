#INSIGHT -> a number is prime if it only has 2 divisors.
import math
def is_prime(n):
    sqrtN = int(math.sqrt(n))
    divisors = []
    for i in range(1,sqrtN):    
        if n % i == 0:
            divisors.append(i)
            if n != i:
                divisors.append(n//i)
    print(len(divisors) == 2)
    return len(divisors) == 2

is_prime(7)
is_prime(10)
