def debug(func): # debug takes a function (func) as input
    def wrapper(*args, **kwargs): # *args collect all normal arguments "rahul" and **kwargs collect keyword arguments name="rahul"
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}:{v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("hello") # with decorator 

# def hello():
#     print("hello")
# hello = debug(hello)    {without decorator}

@debug
def greet(name, greeting):
    print(f"{greeting} {name}")

hello() # calling: hello with args and kwargs , next line :- hello
greet("rahul", "hello") # calling greet with args rahul, hello and kwargs, next line:-  hello rahul

