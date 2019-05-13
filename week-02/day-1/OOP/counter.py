class Counter:
    def __init__(self, value = 0):
        self.counter = value
        
    def add(self, number = 1):
        self.counter += number
        
    def get(self):
        print(f"The current value is {self.counter}")
        
    def reset(self):
        self.counter = 0
        