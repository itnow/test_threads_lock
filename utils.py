import time
from functools import wraps


def bench(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        t_start = time.time()
        result = f(*args, **kwargs)
        elapsed = time.time() - t_start
        print('=== [{}] - {:.3f} sec'.format(f.__name__, elapsed))
        return result
    return decorated_func


@bench
def fib_r(n):
    """Very slow implementation"""
    def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    res = []
    for x in range(n):
        res.append(fib(x))
    return res
