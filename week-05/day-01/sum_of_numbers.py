# Given a list with the following items: 
#1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Calculate the sum of the even numbers which are below or equal to 10.

nums = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

#method 1
from functools import reduce

sum_of_required_nums = reduce(lambda x,y: x+y, tuple(filter(lambda x: x <= 10, nums)))

print(sum_of_required_nums)

#method 2
sum_of_required_nums = sum([x for x in nums if x <= 10])

print(sum_of_required_nums)