# Map
# Create your own map function. It should take an iterable and an other function.

def Map(function, iterator):
    results = []
    for i in iterator:
        results.append(function(i))
    return results


nums = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

required_nums = tuple(Map(lambda x: x**2 > 20, nums))

print(required_nums)