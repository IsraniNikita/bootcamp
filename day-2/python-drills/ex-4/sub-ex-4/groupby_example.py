from itertools import groupby
from operator import itemgetter

data = [
    {"dept": "IT", "name": "Alice"},
    {"dept": "IT", "name": "Bob"},
    {"dept": "HR", "name": "Carol"},
    {"dept": "HR", "name": "Dave"}
]

# Sort by 'dept' before grouping
data.sort(key=itemgetter("dept"))
grouped = groupby(data, key=itemgetter("dept"))

for key, group in grouped:
    print(f"{key}: {[item['name'] for item in group]}")
