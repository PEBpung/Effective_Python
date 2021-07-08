class MyError(Exception):
    pass

def my_generator():
    yield 1
    try:
        yield 2
    except MyError:
        print('MyError 발생!', end=' ')
    else:
        yield 3
    yield 4

it = my_generator()
print(next(it), end=' ')  
print(next(it), end=' ') 
print(it.throw(MyError('test error')))

