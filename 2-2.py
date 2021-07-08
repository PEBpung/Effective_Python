def generate(num):
    for n in num:
        n += 1
        yield n

it = iter(generate([1, 2, 3]))
print(next(it), end=' ')
print(next(it))

