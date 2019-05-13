class Sharpie():
    def __init__(self, color, width):
        self.ink_amount = 100.0
        self.color = str(color)
        self.width = float(width)
    
    def use(self):
        self.ink_amount -= 1
        print(f"Your ink amount remain {self.ink_amount}")
       
class SharpieSet(Sharpie):
    def __init__(self):
        self.sharpieset = [Sharpie('green', 1.0), Sharpie('black', 2.0), Sharpie('White', 3.0)]
        
    def count_usable(self):
        for i in range(len(self.sharpieset)):
            if self.sharpieset[i].ink_amount > 0:
                print(f"Sharp {i+1} is usable")
                
    def remove_trash(self):
        for i in range(len(self.sharpieset)):
            if self.sharpieset[i].ink_amount == 0:
                self.sharpieset.remove(self.sharpieset[i])

sharpieset = SharpieSet()
sharpieset.count_usable()
