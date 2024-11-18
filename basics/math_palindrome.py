def is_number_palindrome(n):
    def reverse(n):
        result = 0
        while n != 0:
            mod = n % 10
            result = result * 10 + mod
            n = n // 10
        return result

    print(reverse(n)==n)
    return reverse(n) == n


is_number_palindrome(121)
is_number_palindrome(1221)
is_number_palindrome(1223)