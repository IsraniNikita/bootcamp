class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

n = Novel("1984", "Orwell", "Dystopian")
print(n.genre)
