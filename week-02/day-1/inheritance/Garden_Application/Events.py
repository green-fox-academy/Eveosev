from  Garden import Garden

class Events(Garden):
    def __init__(self):
        Garden.__init__(self)
        self.plants = []
    
    def add_plant(self, plant):
        self.plants.append(plant)
    
    def info(self):
        for row in self.plants:
            print(row)
            if row.water_amount <= 5:
                print(f"The {row.color} {row.species} needs water")
            else:
                print(f"The {row.color} {row.species} doesn't need water")
    
    def water_Flower(self, amount):
        for row in self.plants:
            if row.species == "Flower":
                if row.water_amount <= 5:
                    row.water_amount = row.water_amount + 0.75 * amount

    def water_tree(self, amount):
        for row in self.plants:
            if row.species == "Tree":
                if row.water_amount <= 10:
                    row.water_amount = row.water_amount + 0.4 * amount

#Test
Y_flower = Garden("yellow", "Flower", 2)
B_flower = Garden("blue", "Flower", 2)
P_tree = Garden("purple", "Tree", 2)
O_tree = Garden("orange", "Tree", 2)
plants = Events()
plants.add_plant(Y_flower)
plants.add_plant(B_flower)
plants.add_plant(P_tree)
plants.add_plant(O_tree)
print(plants.info())
plants.water_Flower(40)
print(plants.info())
plants.water_Flower(70)
print(plants.info())
