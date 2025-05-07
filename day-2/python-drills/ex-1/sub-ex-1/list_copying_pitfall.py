a = [1, 2, 3]
b = a      # Same reference
b.append(4)
print("a after b.append:", a)

a = [1, 2, 3]
b = a[:]   # Shallow copy
b.append(4)
print("a (copied) after b.append:", a)
print("b (copied):", b)
