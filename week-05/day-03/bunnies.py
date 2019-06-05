def bunnies(n):
    if n > 0:
        return 2 + bunnies(n - 1)
    else:
        return 0

print(bunnies(10))