


# A
# AB
# ABC
# ABCD
# ABCDE
def p14(n):
    for i in range(1,n+1):
        print("".join([chr(ord("A")+j) for j in range(i)]))

# 1      1
# 12    21
# 123  321
# 12344321
def p12(n):
    for i in range(1,n+1):
        line = [str(j) for j in range(1,i+1)]
        line.extend([" " * (2*n - 2*i)])
        line.extend([str(j) for j in range(i,0,-1)])
        print("".join(line))

# 1,6,1     8-2(i) 1
# 2,4,2     8-2(i) 2
# 3,2,3     8-2(i) 3

# 4,0,4     
# 1
# 01
# 010
# 1010
# 10101
def p11(n):
    counter = 1
    for i in range(1,n+1):
        arr = []
        for j in range(i):
            arr.append(str(counter%2))
            counter+=1
        print("".join(arr))


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
def p10(n):
    for i in range(2*n - 1):
        if i < n:
            print("*"*(i+1))
        else:
            print("*"*(2*n-i-1))

#     *    
#    ***   
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *
def p9():
    for i in range(5):
        line = [" " * (5-i-1)]
        line.extend("*"* (2* i +1))
        line.extend([" " * (5-i-1)])
        print("".join(line))    
    for i in range(5-1,-1,-1):
        line = [" " * (5-i-1)]
        line.extend("*"* (2* i +1))
        line.extend([" " * (5-i-1)])
        print("".join(line))

# *********
#  ******* 
#   *****
#    ***
#     *
def p8():
    for i in range(5-1,-1,-1):
        line = [" " * (5-i-1)]
        line.extend("*"* (2* i +1))
        line.extend([" " * (5-i-1)])
        print("".join(line))
 
#     *    
#    ***   
#   *****
#  *******
# *********
def p7():
    for i in range(5):
        line = [" " * (5-i-1)]
        line.extend("*"* (2* i +1))
        line.extend([" " * (5-i-1)])
        print("".join(line))

# 12345
# 1234
# 123
# 12
# 1
def p6():
    for i in range(5+1,1,-1):
        line = [str(j) for j in range(1,i)]
        print("".join(line))

# ******
# *****
# ****
# ***
# **
# *
def p5():
    for i in range(5+1,0,-1):
        print("*"*i)
# 1
# 22
# 333
# 4444
# 55555
def p4():
    for i in range(1,5+1):
        line = [str(i) for x in range(1,i+1)]
        print("".join(line))

# 1
# 12
# 123
# 1234
# 12345
def p3():
    for i in range(1,5+1):
        line = [str(x) for x in range(1,i+1)]
        print("".join(line))
# p3()        

# *
# **
# ***
# ****
# *****
def p2():
    for j in range(1,5+1):
        print("*"*j)

def p1():
    for _ in range(5):
        print("*"*5)