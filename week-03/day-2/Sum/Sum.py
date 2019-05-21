class Sum():
    def __init__(self, List):
        self.List = List

    def getSum(self):
        if self.List is not None:
            return sum(self.List)
        return None

