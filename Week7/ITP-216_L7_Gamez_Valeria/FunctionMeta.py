import functools


def log_deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('function name:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        print('function output follows\n')
        func(*args, **kwargs)
    return wrapper

@log_deco
def flowers(name, color):
    print('I love ', name, '.', sep='')

flowers('daffodils', color='blue')
print('function name:', flowers.__name__)
