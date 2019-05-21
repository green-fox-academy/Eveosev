import random

class cab():
    def __init__(self):
        self.goal = str(random.randint(1000,9999))
        self.counter = 0
        self.state = "playing"
    
    def guess(self, g):
        self.g = str(g)
        self.tips = {'cow': 0, 'bull': 0}
        for digit in self.g:
            if digit in self.goal:
                if self.goal.index(digit) == self.g.index(digit):
                    self.tips['cow'] = self.tips.get('cow') + 1
                else:
                    self.tips['bull'] = self.tips.get('bull') + 1
        if self.tips['cow'] == 4:
            self.state = "finished"
        return f"{self.tips['cow']} cow {self.tips['bull']} bull"
    
