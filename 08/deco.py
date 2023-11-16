import cProfile
from functools import wraps
import pstats

def profile_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        return result, profiler
    return wrapper

def print_stat(profiler):
    stats = pstats.Stats(profiler)
    stats.print_stats()

@profile_deco
def add(a, b):
    return a + b

@profile_deco
def sub(a, b):
    return a - b

result, add_profiler = add(1, 2)
result, add_profiler2 = add(4, 5)
result, sub_profiler = sub(4, 5)

print("Add function:")
print_stat(add_profiler)
print_stat(add_profiler2)

print("Sub function:")
print_stat(sub_profiler)
