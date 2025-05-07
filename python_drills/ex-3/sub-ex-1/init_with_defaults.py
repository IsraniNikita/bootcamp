class Book:
    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

book1 = Book()
book2 = Book("1984", "Orwell")

print(book1.title, "-", book1.author)
print(book2.title, "-", book2.author)
