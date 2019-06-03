# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14

# Calculate the average of the odd numbers.

nums = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

#mehtod 1 - filter()
odds = tuple(filter(lambda x: x % 2 != 0, nums))

avg_odds = sum(odds) / len(odds)

print(avg_odds)

#method 2
avg_odds = sum([x for x in nums if x % 2 != 0]) / len([x for x in nums if x % 2 != 0])

print(avg_odds)

#method 3 - reduce()
from functools import reduce

odds = tuple(filter(lambda x: x % 2 != 0, nums))

avg_odds = reduce(lambda x,y: x+y, odds) / len(odds)

print(avg_odds)

#method 4 
from statistics import mean

avg_odds = mean([x for x in nums if x % 2 != 0])

print(avg_odds)