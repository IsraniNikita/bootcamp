# List comprehension
lst = [x for x in range(10) if x % 2 == 0]
print("List comprehension:", lst)

# Generator expression
gen = (x for x in range(10) if x % 2 == 0)
print("Generator output:", list(gen))
