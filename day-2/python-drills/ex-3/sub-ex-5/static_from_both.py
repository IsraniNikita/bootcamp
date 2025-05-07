class Book:
    @staticmethod
    def is_valid_isbn(isbn):
        return isinstance(isbn, str) and len(isbn) == 13

print("From class:", Book.is_valid_isbn("1234567890123"))

b = Book()
print("From instance:", b.is_valid_isbn("1234567890123"))
