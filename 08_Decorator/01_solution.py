import time

def timer(func):
    def wrapper(*args, **kwargs): # accepts unlimited arguments 
        start = time.time() # start time of function 
        result = func(*args, **kwargs) 
        end = time.time() # end time of function for execution 
        print(f"{func.__name__} takes {end-start} sec to run")
        return result 
    return wrapper

@timer # decorator
def example(n):
    time.sleep(n)

example(2) # example takes 2 sec to run 