def fib1(n: int, memo: dict = {}) -> int:
    if n < 2:
        return n
    
    if n in memo:
        return memo[n]
    memo[n] =  fib1(n-1) + fib1(n-2)
    return memo[n]

