import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_dict(cls, d):
        return cls(d["title"], d["author"])

    @classmethod
    def from_json(cls, json_str):
        d = json.loads(json_str)
        return cls.from_dict(d)

b1 = Book.from_dict({"title": "Sapiens", "author": "Harari"})
b2 = Book.from_json('{"title": "Homo Deus", "author": "Harari"}')

print(b1.title, b1.author)
print(b2.title, b2.author)
