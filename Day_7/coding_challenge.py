import time

def time_decorator(func):
    def wrapper(*args, **kargs):
        start_time = time.time()
        result = func(*args, **kargs)
        end_time =time.time()
        print(f"function took {end_time - start_time:.2f} seconds to execute")
        return result
    return wrapper

# @time_decorator
# def time_taken():
#     time.sleep(5)

# time_taken()