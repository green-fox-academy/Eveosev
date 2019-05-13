class Sharpie():
    def __init__(self, color, width):
        self.ink_amount = 100.0
        self.color = str(color)
        self.width = float(width)
    
    def use(self):
        self.ink_amount -= 1
        print(f"Your ink amount remain {self.ink_amount}")
        
sharpie1 = Sharpie('green', 5)
sharpie1.use()
