#INSIGHT -> Euclidean algorithm states, you can subtract the greater value with the lower value until one of them becomes zero. The other number becomes the 
# GCD Greatest common denominator or Highest common factor
def gcd(N1,N2):
    if N1 ==0:
        print(N2)
        return N2
    if N2 == 0:
        print(N1)
        return N1
    if N1 > N2:
        gcd(N1 -N2, N2)
    else:
        gcd(N1, N2-N1)


gcd(9,12)
gcd(25,12)