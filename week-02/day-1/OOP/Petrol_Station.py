"""
Create Station and Car classes
  Station
    gas_amount
    refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
  Car
    gas_amount
    capacity
    create constructor for Car where:
      initialize gas_amount -> 0
      initialize capacity -> 100
"""

class Car(object):
    def __init__(self, gas_amount, capacity):
        self.gas_amount = gas_amount
        self.capacity = capacity

class Station(Car):
    def __init__(self, gas_Amount):
        Car.__init__(self, 0, 100)
        self.gas_Amount = gas_Amount
    
    def refill(self):
        self.gas_Amount -= self.capacity
        self.gas_amount += self.capacity
        print(f"The gas_Amount decreases {self.capacity} and the gas_amount increases {self.capacity}")

Station1 = Station(2000)
Station1.refill()
