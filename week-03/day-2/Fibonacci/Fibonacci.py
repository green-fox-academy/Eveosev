def fibonacci(index):
    Fib_sequence = [0, 1]
    if index == 2:
        return Fib_sequence
    elif index > 2:
        for i in range(2,index):
            Fib_sequence.append(Fib_sequence[i - 1] 
            + Fib_sequence[i - 2])
        return Fib_sequence
    else:
        return f"Error"