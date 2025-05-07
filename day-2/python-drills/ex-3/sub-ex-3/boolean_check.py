class Resource:
    def __init__(self, available=True):
        self.available = available

    def __bool__(self):
        return self.available

r = Resource(False)
if r:
    print("Available")
else:
    print("Not available")
