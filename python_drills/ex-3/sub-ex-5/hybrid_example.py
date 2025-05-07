class Library:
    books = []

    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_valid_book(book):
        return hasattr(book, 'title') and hasattr(book, 'author')

    @classmethod
    def total_books(cls):
        return len(cls.books)

    def add_book(self, book):
        if self.is_valid_book(book):
            Library.books.append(book)
            print(f"{book.title} added to {self.name}")
        else:
            print("Invalid book")

class SimpleBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author

lib = Library("Central Library")
book = SimpleBook("1984", "George Orwell")
lib.add_book(book)

print("Total books in system:", Library.total_books())
