from collections import defaultdict

words = ["apple", "banana", "avocado", "blueberry", "cherry"]
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))
