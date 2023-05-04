def log_call(func):
    def wrapper(*args, **kwargs):
        returning = func(*args, **kwargs)
        print(f'Функція {func.__name__}, приймає аргументи args {args}, kwargs {kwargs}, та повертає {returning}')
        return  returning
    return wrapper

@log_call
def temp(C):
    return (C * 1.8) + 32
print(temp(32))
print(temp(40))
print(temp(50))