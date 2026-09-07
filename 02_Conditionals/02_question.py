# Movie ticket pricing :- 
# movie tickets are priced based on age: $12 for adults (18 or over), $8 for children. Everyone gets a $2 discount on wednesday. 

age = input("Please tell me what's your age ? \n");
age_in_int = int(age);

day = input("Please tell me what's day is today ? \n");

price = 12 if age_in_int >= 18 else 8;

if day == "wednesday":
    price = price - 2;

print("Ticket price for you is $",price);