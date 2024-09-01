# implement a decorator that cache the return value of a function, so that when it's called  with the same argunment, the cache value is returned instead of re-exicuting the function. 
import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args) 
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(5)
    return a+b

print(long_running_function(2,6))
print(long_running_function(2,9))