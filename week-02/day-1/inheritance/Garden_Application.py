
class Garden(Flower, Tree):
    def __init__(self, flowers = ['yellow Flower', 'blue Flower'], trees = ['purple Tree', 'orange Tree'],
                 flowers_water_amount = [0,1], trees_water_amount = [0, 5]):
        self.flowers = flowers
        self.trees = trees
        self.flowers_water_amount = flowers_water_amount
        self.trees_water_amount = trees_water_amount
       
    def info(self):
        for i in range(len(self.flowers_water_amount)):
            if self.flowers_water_amount[i] >= 5:
                print(f"The {self.flowers[i]} dosen't need water")
            else:
                print(f"The {self.flowers[i]} needs water")
        for i in range(len(self.trees_water_amount)):
            if self.trees_water_amount[i] >= 5:
                print(f"The {self.trees[i]} dosen't need water")
            else:
                print(f"The {self.trees[i]} needs water")
      
    def watering_flowers(self, amount):
        for i in range(len(self.flowers_water_amount)):
             if self.flowers_water_amount[i] >= 5:
                 print(f"The {self.flowers[i]} dosen't need water")
             else:
                self.flowers_water_amount[i] = self.flowers_water_amount[i] + 0.75 * amount
                if self.flowers_water_amount[i] <= 5:
                    print(f"The {self.flowers[i]} needs water")
                else:
                    print(f"The {self.flowers[i]} dosen't need water")
  
    def watering_trees(self, amount):
        for i in range(len(self.trees_water_amount)):
             if self.trees_water_amount[i] >= 10:
                 print(f"The {self.trees[i]} dosen't need water")
             else:
                self.trees_water_amount[i] = self.flowers_water_amount[i] + 0.4 * amount
                if self.flowers_water_amount[i] <= 10:
                    print(f"The {self.trees[i]} needs water")
                else:
                    print(f"The {self.trees[i]} dosen't need water")

garden = Garden()
garden.info()
garden.watering_flowers(40)
garden.watering_trees(70)