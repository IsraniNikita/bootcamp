class Book:
    @staticmethod
    def is_valid_isbn(isbn):
        return isinstance(isbn, str) and len(isbn) == 13

print(Book.is_valid_isbn("1234567890123"))  # True
print(Book.is_valid_isbn(12345))  # False
