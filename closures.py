def logger(func, *args, **kwargs):
    # print(args, kwargs)
    def inner(*args, **kwargs):
        print(f'LOG::Calling {func.__name__} with positional arguments: {args} and keyword arguments: {kwargs}')
        func(*args, **kwargs)

    return inner


def i_print_my_params(a, b, c, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(kwargs)


@logger
def i_print_my_params_too(a, b, c, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(kwargs)

print('-'*80, '\nCalling an undecorated function, should just do its job.\n', '-'*80)
i_print_my_params(1, 2, 3, 4, 5, action='cut')
print('-'*80)

a_wrapped_func = logger(i_print_my_params)
print('-'*80, '\nCalling wrapped function, should print a log message.\n', '-'*80)
a_wrapped_func(1, 2, 3, 4, 5, action='cut')
print('-'*80)

print('-'*80, '\nCalling decorated function, should also print a log message.\n', '-'*80)
i_print_my_params_too(1, 2, 3, 4, 5, action='paste')
print('-'*80)