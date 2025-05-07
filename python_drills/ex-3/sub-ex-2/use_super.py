class Book:
    def describe(self):
        return "Book"

class Novel(Book):
    def describe(self):
        return "Novel -> " + super().describe()

n = Novel()
print(n.describe())
