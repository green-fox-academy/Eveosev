# Given a list with the following items: 
# 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Create a new list which contains the positive items' squared value

nums = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

squared_p_nums = [x**2 for x in nums if x > 0]
print(squared_p_nums)

