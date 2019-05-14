import random

class Aircraft(object):
    def __init__(self, types):
        self.types = types
        self.ammunition = 0
        self.ammo = 0
        if self.types == 'F16':
            self.max_ammo = 8
            self.base_damage = 30
        else: 
            self.max_ammo = 12
            self.base_damage = 50
    
    def getStatus(self):
        print(f"Type {self.types}, Ammo: {self.ammo}, Base Damage: {self.base_damage}, All Damage: {self.damage}")
     
    def getType(self):
        print(f'The type of the aircraft is {self.types}')
        
    def fight(self):
        self.damage = self.ammo * self.base_damage
        print(f'Deals {self.damage} damage')
        
    def refill(self,fill = random.randint(100,300)):
        self.remaining = fill
        if self.types == 'F16':
            if self.remaining > self 
            self.ammo = 
            
    def isPriority(self):
        if self.types == 'F16':
            return True
        else:
            return False
        
        




F16 = Aircraft('F16')
F35 = Aircraft('F35')