import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function_name):
    def wrapper_function():
        start_time = time.time()
        function_name()
        end_time = time.time()
        print(f"{function_name.__name__} run speed {end_time - start_time} seconds")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()

# Output
# fast_function run speed 0.0 seconds
# slow_function run speed 0.0 seconds
