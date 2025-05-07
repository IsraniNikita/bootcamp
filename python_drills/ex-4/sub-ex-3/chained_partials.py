from functools import partial

# Create a customized print function with partial
custom_print = partial(print, end=' ', sep='|')

custom_print('Hello', 'World')  # Output: Hello|World
custom_print('Python', 'is', 'fun')  # Output: Python|is|fun
