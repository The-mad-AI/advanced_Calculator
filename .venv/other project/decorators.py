import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"zaman ejra : {end - start :.4f} sanie")
        return result
    return wrapper
        
        
        
@timer
def slow_function():
    total = 0
    for i in range(10**6):
        total += i
    return total


slow_function()