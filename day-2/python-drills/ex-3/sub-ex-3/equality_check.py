class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return (self.title, self.author) == (other.title, other.author)

b1 = Book("1984", "Orwell")
b2 = Book("1984", "Orwell")
print(b1 == b2)  # True
