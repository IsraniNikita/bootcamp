class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, s):
        title, author = s.split("|")
        return cls(title, author)

class Novel(Book):
    def __init__(self, title, author):
        super().__init__(title, author)

n = Novel.from_string("Dune|Herbert")
print(n.title, n.author, isinstance(n, Novel))  # True
