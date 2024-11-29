#INSIGHT-> all divisors.. Instead of doing a remainder till the number, go till the square root of the number 
# and check add not only the remainder by the n//i
import math

def divisor(n):
    sqrtN = int(math.sqrt(n))
    result = []
    for i in range(1,sqrtN):
        if n % i == 0:
            result.append(i)
        
            if i != n:
                result.append(n//i)
    
    print(result)

divisor(50)    