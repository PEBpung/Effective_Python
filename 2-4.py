def my_generator():
    received = yield 1
    print(f'받은값 = {received}')

it = iter(my_generator())
output = next(it)
print(f'출력값 = {output}')

try:
    next(it)
except StopIteration:
    pass

