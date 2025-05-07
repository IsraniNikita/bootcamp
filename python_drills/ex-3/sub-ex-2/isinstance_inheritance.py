class Book:
    pass

class Novel(Book):
    pass

n = Novel()
print(isinstance(n, Book))  # True
