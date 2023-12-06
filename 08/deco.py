from typing import Callable, Any
from cProfile import Profile
import pstats
import time


def profile_deco(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        profiler = Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        wrapper.ps.add(profiler)
        return result

    wrapper.ps = pstats.Stats()

    def print_stat():
        wrapper.ps.print_stats()

    wrapper.print_stat = print_stat

    return wrapper


@profile_deco
def sleep_3() -> None:
    return time.sleep(3)


@profile_deco
def sleep_1() -> None:
    return time.sleep(1)


sleep_1(), sleep_1()
sleep_3()

sleep_1.print_stat()
sleep_3.print_stat()
