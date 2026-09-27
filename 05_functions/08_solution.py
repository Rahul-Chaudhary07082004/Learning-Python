# Function with **kwargs
# Create a function that accepts any number of keyword arguments and print them in the format key:value

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}", end= " ")

print_kwargs(name = "Rahul", power = "love")