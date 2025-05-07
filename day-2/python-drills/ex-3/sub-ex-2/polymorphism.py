class Book:
    def describe(self):
        return "General book"

class Novel(Book):
    def describe(self):
        return "A thrilling novel"

books = [Book(), Novel()]
for b in books:
    print(b.describe())
