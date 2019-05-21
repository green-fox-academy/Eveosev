from USADollar import USADollar
from HungarianForint import HungarianForint

class BankAccount(USADollar, HungarianForint):
    def __init__(self, name = "", pin = "", Currency = ""):
        self.name = name
        self.pin = pin
        if Currency == "USD":
            USADollar.__init__(self, 0)
        if Currency == "HUF":
            HungarianForint.__init__(self, 0)

    def deposit(self, value):
        if value >= 0:
            self.value = self.value + value
        return self.value
    
    def withdraw(self, pin, amount):
        if pin == self.pin:
            if self.value >= amount:
                self.value = self.value - amount
                return amount
            else: 
                return 0
        else: 
            return 0
