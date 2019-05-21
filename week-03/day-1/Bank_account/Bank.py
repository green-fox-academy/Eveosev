from USADollar import USADollar
from HungarianForint import HungarianForint
from BankAccount import BankAccount

class Bank():
    def __init__(self):
        self.bankaccount = []

    def creatAccount(self, account):
        self.bankaccount.append(account)

    def getAllMoney(self, name):
        self.account_money = 0
        for i in range(len(self.bankaccount)):
            if name == self.bankaccount[i].name:
                self.account_money = self.account_money + self.value
        return f"The accounts' money of {name} is {self.account_money}"



