class Book:
    def __init__(self, title):
        self.title = title

    def __lt__(self, other):
        return self.title < other.title

books = [Book("Zebra"), Book("Animal Farm"), Book("1984")]
books.sort()
print([b.title for b in books])  # ['1984', 'Animal Farm', 'Zebra']
