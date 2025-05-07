lst = [1, 2, -3, 4]

print("Any negative?", any(x < 0 for x in lst))
print("All positive?", all(x > 0 for x in lst))
