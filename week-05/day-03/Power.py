def power(base, n):
    if n == 0:
        return 1
    else:
        return base * power(base, n - 1)

print(power(3,3))