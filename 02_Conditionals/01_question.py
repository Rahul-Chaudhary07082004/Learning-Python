# 1. Age group categorization :- 
# classify a person's age group: Child(<13), Teenager(13-19), Adult(20-59), Senior(60+).

age = input("Provide the age: ");
age_in_int = int(age);

if (age_in_int < 13):
    print("Child");
elif (age_in_int < 20):
    print("Teenager");
elif (age_in_int < 60):
    print("Adult");
else: 
    print("Senior");
