from Currency import Currency

class HungarianForint(Currency):
    def __init__(self, value = 0):
        Currency.__init__(self, "HUF", "Hungarian National Bank", 0)
        self.value = value
