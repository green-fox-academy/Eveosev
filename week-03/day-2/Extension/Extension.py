def add(a, b):
    return a + b

def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif a > b and a < c:
        return c
    elif a < b and b < c:
        return c
    elif a < b and b > c:
        return b

def median(pool):
    pool.sort()
    n = len(pool)
    if n % 2 == 0:
        return (pool[n // 2] + pool[n // 2 - 1]) / 2
    else:
        return pool[(n - 1) // 2]

def is_vovel(char):
    return char in ['a', 'u', 'o', 'e', 'i']

def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve