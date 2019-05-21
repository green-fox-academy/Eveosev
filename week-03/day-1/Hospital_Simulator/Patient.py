import random
class Patient():
    def __init__(self, severity = random.randint(1,10)):
        self.severity = severity

    def retreive(self):
        self.severity = 0

    def treat(self):
        self.severity -= 1
