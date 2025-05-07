from collections import OrderedDict

ordered = OrderedDict()
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3

for key, value in ordered.items():
    print(key, value)
