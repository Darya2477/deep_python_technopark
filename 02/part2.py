import time

def mean(k):
    def decorator(func):
        call_times = []

        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            call_times.append(end_time - start_time)
            call_times = call_times[-k:]

            avg_time = sum(call_times) / len(call_times) if call_times else 0
            print(f"Среднее время последних {k} вызовов: {avg_time} секунд")

            return result

        return wrapper

    return decorator

@mean(10)
def foo(arg1):
    pass

@mean(2)
def boo(arg1):
    pass

for _ in range(100):
    foo("Walter")
