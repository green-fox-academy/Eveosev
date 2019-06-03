# Create a generator which will always yield the next Fibonacci number.

def fibonacci():
    i = 1
    f = {'n-2': 1, 'n-1': 1}
    while True:
        if i <= 1:
            yield 1
        else :
            yield f['n-2'] + f['n-1']
            f['n-2'], f['n-1'] = f['n-1'], f['n-2'] + f['n-1']
        i = i + 1

fibonacci_seq = fibonacci()
for j in range(30):
    print(next(fibonacci_seq))

