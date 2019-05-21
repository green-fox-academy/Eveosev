class Book(object):
    def __init__(self, author, title, release_year):
        self.author = author
        self.title = title
        self.release_year = release_year
    
    def toString(self):
        print(f"{self.author} : {self.title} ({self.release_year})")
    
#book1 = Book('Douglas Adams', 'The Hitchhiker"s Guide to the Galaxy', '1979')
#book1.toString()

class Bookself():
    bookself = []
    def __init__(self, author, title, release_year):
        self.author = author
        self.title = title
        self.release_year = release_year

    def addbook(self):
        Bookself.bookself.append([self.author, self.title, self.release_year])
    
    def removebook(self):
        Bookself.bookself.remove([self.author, self.title, self.release_year])

    def earliestPublished(self):
        self.esortedbookself = sorted(Bookself.bookself, key = lambda x : int(x[2]))
        return self.esortedbookself[0]
    
    def lastestPublished(self):
        self.lsortedbookself = sorted(Bookself.bookself, key = lambda x : int(x[2]), reverse = True)
        return self.lsortedbookself[0]

    def favouriteAuthor(self):
        Authorset = {}
        for row in Bookself.bookself:
            Authorset[row[0]] = Authorset.get(row[0], 0) + 1      
        sorted_Authorset = sorted(Authorset.items(), key = lambda x:x[1], reverse = True)
        self.fAuthorset = []
        for row in sorted_Authorset:
            if row[1] == sorted_Authorset[0][1]:
                self.fAuthorset.append(row[0])
            elif row[1] <= sorted_Authorset[0][1]:
                break
        return self.fAuthorset

    def toString(self):
        self.number = len(Bookself.bookself)
        print(f"The number of books is {self.number})")
        print(self.earliestPublished())
        print(self.lastestPublished())
        print(self.favouriteAuthor())

book2 = Bookself('Douglas Adams', 'The Hitchhiker"s Guide to the Galaxy', '1979')
book3 = Bookself('Douglas', 'The Hitchhiker"s Guide to the Galaxy', '1980')
book2.addbook()
book3.addbook()
book3.earliestPublished()
book3.favouriteAuthor()
book3.lastestPublished()
book3.toString()
