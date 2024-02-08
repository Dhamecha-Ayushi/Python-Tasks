import coding_challenge

def my_decorator(func):
    def wrapper():
        print("Befor function call...")
        func()
        print("After function call...")
    return wrapper
@coding_challenge.time_decorator
@my_decorator
def say_hello():
    print("Hello..!")
    coding_challenge.time.sleep(2)
    
say_hello()