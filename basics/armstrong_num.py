#INSIGHT -> Armstrongs number is 153 is the sum of each number raised to the power of the number of digits 
# 153 == 1^3 + 5^3 + 3^3
import math
def armstrong(n):
    l = len(str(n))
    result = 0
    c = n
    while n > 0:
        tail = n%10
        result += math.pow(tail,l)
        n = n//10
    
    print(result == c)






























    # length = len(str(n))
    # c = n
    # result =0
    # while c > 0:
    #     tail = c %10
    #     result += math.pow(tail,length)
    #     c = c//10
    # print(result == n)
armstrong(153)
armstrong(371)