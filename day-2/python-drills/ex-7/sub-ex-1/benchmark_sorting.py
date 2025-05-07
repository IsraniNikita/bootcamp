import timeit

def custom_sort(arr):
    arr.sort()
    return arr

builtin_time = timeit.timeit('sorted(range(1000))', number=1000)

custom_time = timeit.timeit('custom_sort(list(range(1000)))', number=1000, globals=globals())

print(f"Built-in sorted time: {builtin_time} seconds")
print(f"Custom sort time: {custom_time} seconds")