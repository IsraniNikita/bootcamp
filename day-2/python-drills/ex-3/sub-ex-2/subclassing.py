class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Novel(Book):
    pass

novel = Novel("1984", "Orwell")
print(novel.title, "-", novel.author)
