class Book:
    @staticmethod
    def stat():
        print("Static method")

    @classmethod
    def klass(cls):
        print("Class method, cls is:", cls)

Book.stat()
Book.klass()

b = Book()
b.stat()
b.klass()
