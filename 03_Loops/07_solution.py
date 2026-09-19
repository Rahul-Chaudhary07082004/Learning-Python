# Validate input
# keep asking the user for input untill they enter a number between 1 and 10

while True:
    number = int(input("give a number b/w 1 and 10: \n"))
    if 1<= number <= 10:
        print("thanks")
        break
    else:
        print("invalid number found !")