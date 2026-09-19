# Factorial calculator 
# Compute the factorial of a number using a while loop

number = int(input("give a number to find the factorial: \n"))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial of given number is", factorial)