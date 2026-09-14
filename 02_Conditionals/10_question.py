# Pet food recommendation 
# Recommend a type of pet food based on the pet's species and age. (eg. Dog <2 years - puppy food, Cat >5 years - senior cat food)

pet_type = input("who is your pet ? \n")
pet_age = int(input("what is your pet's age ? \n"))

if pet_type == "dog":
    if pet_age < 2:
        pet_food = "puppy food"
    else:
        pet_food = "adult dog food"

elif pet_type == "cat":
    if pet_age > 5:
        pet_food = "senior cat food"
    else:
        pet_food = "junior cat food"

print("The recommended food for your ", pet_type, " is", pet_food)