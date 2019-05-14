import random
def dividebyzero():
    x = random.randint(0, 100)
    if x == 0:
        print("Fail")
    else:
        print(f"{x / 10}")
        
dividebyzero()