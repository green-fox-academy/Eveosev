#Given a list with the following items:
#1, 3, -2 , -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# #Create a new list which contains only the even numbers

num = [1, 3, -2 , -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
#Method 1

even_nums = tuple(filter(lambda x: x % 2 == 0, num))

print(even_nums)

#Method 2
print([x for x in num if x % 2 == 0])
