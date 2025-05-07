from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4]
counter = Counter(numbers)
print(counter.most_common(2))
