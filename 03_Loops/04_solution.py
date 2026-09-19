# Reverse a string
# Reverse a string using a loop

input_str = input("give string to reverse: \n")
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str
print(reversed_str)