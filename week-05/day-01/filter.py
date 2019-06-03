# Filter
# Create your own filter function. It should take an iterable and an other function.

def Filter(function, iterator):
    results = []
    results.append(i for i in iterator if function(i) is True)   
    return results[0]

nums = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

required_nums = tuple(Filter(lambda x: x**2 > 20, nums))

print(required_nums)