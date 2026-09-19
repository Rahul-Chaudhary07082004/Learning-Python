# sum of even numbers
# calculate the sum of even numbers upto a given number n 

n = int(input("enter the number to find the sum of even numbers till n: \n"))
sum_of_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_of_even += i
print("The sum of even number till ",n, "is", sum_of_even)