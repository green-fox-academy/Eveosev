def greatest_common_divisor(a, b):
    if a > b:
        a, b = b, a
    if b % a == 0:
        return a
    else:
        return greatest_common_divisor(b % a, a)


print(greatest_common_divisor(144, 196))