class Book:
    def describe(self):
        return "Generic Book"

class Novel(Book):
    def describe(self):
        return "Novel: A specific type of book"

n = Novel()
print(n.describe())
