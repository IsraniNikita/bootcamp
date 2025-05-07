from contextlib import suppress

my_dict = {"name": "Nikita"}

with suppress(KeyError):
    print(my_dict["age"])
