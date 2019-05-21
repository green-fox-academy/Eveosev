class Paperback_book():
    def __init__(self, title, author, release_year, page_number):
        self.w_per_page = 10
        self.title = title
        self.author = author
        self.release_year = release_year
        self.page_number = page_number
        self.weight = self.w_per_page * self.page_number + 20
       
    def Info(self):
        return [self.author, self.title, self.release_year]

