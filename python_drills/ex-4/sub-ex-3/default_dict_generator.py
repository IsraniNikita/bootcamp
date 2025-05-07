from functools import partial
from collections import defaultdict

# Use a lambda to define recursively nested defaultdicts
nested_dict = lambda: defaultdict(nested_dict)

# Example usage
data = nested_dict()
data['first']['second'] = 'value'

print(data)
print(data['first']['second'])  # Should output: value
