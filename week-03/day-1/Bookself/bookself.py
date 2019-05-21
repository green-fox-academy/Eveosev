from Hardcover_book import Hardcover_book
from Paperback_book import Paperback_book
class Bookself():
    def __init__(self):
        self.bookself = []
    
    def addbook(self, book):
        self.bookself.append(book)

    def getLightestBook(self):
        self.weightSet = []
        for i in range(len(self.bookself)):
            self.weightSet.append(self.bookself[i].weight)
        MinWeight = min(self.weightSet)
        for i in range(len(self.bookself)):
            if MinWeight == self.bookself[i].weight:
                print(f"{self.bookself[i].Info()}")

    def getMostPage_Author(self):
        self.pageSet = {}
        for i in range(len(self.bookself)):
            self.pageSet[self.bookself[i].author] = self.pageSet.get(self.bookself[i].author, 0) + self.bookself[i].page_number
        self.Mostpages = max(list(self.pageSet.values()))
        for i in self.pageSet:
            if self.pageSet[i] == self.Mostpages:
                print(f"{i} wrote the most pages with {self.pageSet[i]} pages")


#Test 
HBook1 = Hardcover_book('a', 'Peter', 1990, 80)
HBook2 = Hardcover_book('b', 'Mary', 1978, 100)
PBook1 = Paperback_book('c', 'Tony', 2001, 20)
PBook2 = Paperback_book('d', 'Lucy', 1987, 20)
PBook3 = Paperback_book('e', 'Lucy', 1987, 110)
bookself = Bookself()
bookself.addbook(HBook1)
bookself.addbook(HBook2)
bookself.addbook(PBook1)
bookself.addbook(PBook2)
bookself.addbook(PBook3)
bookself.getLightestBook()
bookself.getMostPage_Author()

