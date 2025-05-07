class Book:
    @classmethod
    def describe(cls):
        return f"I am a {cls.__name__}"

class Novel(Book):
    @classmethod
    def describe(cls):
        return f"Novel class: {super().describe()}"

print(Book.describe())
print(Novel.describe())
