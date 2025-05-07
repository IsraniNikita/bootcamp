nums = [5, -1, 2, -3]
fixed = [x if x >= 0 else 0 for x in nums]
print(fixed)  # [5, 0, 2, 0]
