def sum_digit(n):
    if n / 10 != 0:
        return n % 10 + sum_digit( n // 10 )
    else:
        return 0

print(sum_digit(121))

