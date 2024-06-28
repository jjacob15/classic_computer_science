def jumpingOnClouds(c):
    # Write your code here
    pos = 0
    length = len(c)
    jump = 0
    while pos < length-1:
        if pos + 2 < length:
            s = c[pos+2]
            if s == 0:
                pos += 2
            else:
                pos += 1
        else:
            pos += 1
        jump += 1
    return jump


r = jumpingOnClouds([0, 0, 0, 1, 0, 0])
print(r)
r = jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
print(r)
