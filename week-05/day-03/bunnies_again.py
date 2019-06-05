def bunnies_again(n):
    if n > 0:
        if n % 2 == 0:
            return 2 + bunnies_again(n - 1)
        elif n % 2 !=0:
            return 3 + bunnies_again(n - 1)
    else:
        return 0

print(bunnies_again(3))
