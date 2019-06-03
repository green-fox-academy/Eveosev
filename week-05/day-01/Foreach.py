# Foreach
# Create a function called foreach which can take an iterable and an other function. Apply the function for all the elements in the iterable.

def foreach(function, iterator):
    results = []
    for i in iterator:
        results.append(function(i))
    return results

nums = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

#method 1
required_nums = tuple(foreach(lambda x: x**2 > 20, nums))

print(required_nums)