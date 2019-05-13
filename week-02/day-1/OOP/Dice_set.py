import random

class DiceSet(object):

    def __init__(self):
        self.dices = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dices)):
            self.dices[i] = random.randint(1, 6)
        return self.dices

    def get_current(self, index = None):
        if index != None:
            return self.dices[index]
        else:
            return self.dices

    def reroll(self, index = None):
        if index != None:
            self.dices[index] = random.randint(1, 6)
        else:
            self.roll()

dice_set = DiceSet()
dice_set.roll()
i = 0
while isinstance(i,int):
    if dice_set.get_current(i) == 6:
        i += 1
    else:
        dice_set.reroll(i)
        dice_set.get_current(i)
    if i == 5 and dice_set.get_current(5) == 6: 
        break
dice_set.get_current()
