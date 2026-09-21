# prime number checker 
# check if a number is a prime number 

number = int(input("give a number: \n"))
is_prime = True

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
