
class Animal():
    def __init__(self):
      self.hunger = 50
      self.thirst = 50
    
    def eat(self):
        self.hunger -= 1
        print(f"Your hunger value is {self.hunger}")
        
    def drink(self):
        self.thirst -= 1
     
    def play(self):
        self.hunger += 1
        self.thirst += 1
        print(f"Your hunger value is {self.hunger}")
        print(f"Your drink valule i {self.thirst}")
    
class Farm(Animal):
    def __init__(self, slots):
        Animal.__init__(self)
        self.slots = slots
        self.animalset = [Animal(), Animal(), Animal()]
    
    def breed(self):
        if self.slots > 0:
            self.animalset.append(Animal())
            self.slots -= 1
            print(f"The remaining slot(s) is/are {self.slots}")
        else:
            print("There is no more space")
            
    def slaugter(self):
        for i in range(len(self.animalset)):
            if self.animalset[i].hungry < self.animalset[i+1].hungry:
                self.animalset[i], self.animalset[i+1] = self.animalset[i+1], self.animalset[i]
        self.animalset.remove(self.animalset[-1])

                

animalset = Farm(2)
animalset.breed()
animalset.play()
