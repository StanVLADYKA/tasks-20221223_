some_list = [2,44,6,7,2]

iterator = iter(some_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration:
    print("stop")