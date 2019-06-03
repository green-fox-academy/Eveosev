# All positive
# Given a list with the following items: 
# 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Determine whether every number is positive or not using all().
from functools import reduce

nums = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

comparation = tuple(map(lambda x: x > 0, nums))

result = reduce(lambda x,y: x & y, comparation)

print(result)