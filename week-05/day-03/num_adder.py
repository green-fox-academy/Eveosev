def num_adder(n):
    if n > 1:
        return n + num_adder(n - 1)
    else:
        return 1

print(num_adder(20))