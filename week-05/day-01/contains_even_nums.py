# Given a list with the following items: 
# 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Determine whether it contains even numbers or not using any().

nums = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

comparation = tuple(map(lambda n: n % 2 == 0, nums))

print(f"{True in comparation}")
