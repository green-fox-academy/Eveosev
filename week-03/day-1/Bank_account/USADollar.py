from Currency import Currency

class USADollar(Currency):
    def __init__(self, value = 0):
        Currency.__init__(self, "USD", "Federal Reserve System", 0)
        self.value = value

