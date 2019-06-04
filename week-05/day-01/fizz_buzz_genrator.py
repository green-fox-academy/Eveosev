# Fizz Buzz generator
# Create a generator which will always yield the next item from the fizz buzz sequence.

def fizz_buzz_generator():
    i = 1
    while True:
        if i % 3 == 0 and i % 5 == 0:
            yield 'FizzBuzz'
            i = i + 1
        elif i % 3 == 0 and i % 5 != 0:
            yield 'Fizz'
            i = i + 1
        elif i % 3 != 0 and i % 5 == 0:
            yield 'Buzz'
            i = i + 1
        else:
            yield i
            i = i + 1

fizz_buzz = fizz_buzz_generator()
for j in range(30):
    print(next(fizz_buzz))

#Update
def fizz_buzz_generator2():
    i = 1
    while True:
        yield 'Fizz'*(i % 3 == 0) + 'Buzz'*(i % 5 == 0) or i
        i = i + 1

fizz_buzz = fizz_buzz_generator2()
for j in range(30):
    print(next(fizz_buzz))
