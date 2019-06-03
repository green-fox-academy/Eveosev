# Given a list with the following items: 
# 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Create a new list which contains the numbers if their squared value is above 20.

nums = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

#method 1
required_nums = tuple(filter(lambda x: x**2 > 20, nums))

print(required_nums)

#method 2
required_nums = [x for x in nums if x ** 2 > 20]
print(required_nums)
