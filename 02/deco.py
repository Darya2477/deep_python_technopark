import time

def mean(k):
    def decorator(func):
        timings = []

        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time

            timings.append(execution_time)
            if len(timings) > k:
                timings.pop(0)
            
            average_time = sum(timings) / len(timings)
            print(f"Average execution time of last {k} calls: {average_time}")

            return result
        
        return wrapper
    
    return decorator
