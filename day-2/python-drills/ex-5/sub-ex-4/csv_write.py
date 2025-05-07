import csv

data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
with open("output.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)
print("CSV written to output.csv")
