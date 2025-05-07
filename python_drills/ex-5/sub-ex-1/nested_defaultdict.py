from collections import defaultdict

nested = defaultdict(lambda: defaultdict(int))
nested["dept"]["employees"] += 5
nested["dept"]["projects"] += 2

print(dict(nested))
