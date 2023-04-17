def create_sum(func):
    def wrapper(*arg, **kwargs):
        func(arg, kwargs)
        print('test')

    return wrapper


@create_sum
def test_opp():
    print(1)
