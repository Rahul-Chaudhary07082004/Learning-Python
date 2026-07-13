# Strings can be wirte with ' ', " ", """ """

Chai_1 = "Lemon Tea"
first_Char = Chai_1[0]
print(first_Char) # L

slice_Chai = Chai_1[0:5]
print(slice_Chai) # [included:excluded], Lemon

num_List = "0123456789"

print(num_List[:]) # 0123456789
print(num_List[3:]) # 3456789
print(num_List[:7]) # 0123456

print(num_List[1:7:2]) # [included:excluded:hopping], 135

Chai_2 = "Masala Chai"

print(Chai_2.lower()) # masala chai

print(Chai_2.upper()) # MASALA CHAI

Chai_3 = "   Oolong chai    "
print(Chai_3.strip()) # Remove extra spaces from string, "Oolong chai"

print(Chai_2.replace("Masala","Lemon")) # Lemon Chai

Chai_4 = "Lemon, Ginger, Mint"
print(Chai_4.split(", ")) # ["Lemon", "Ginger", "Mint"]
# empty split() by default gives spaces, convert string to list => return list

print(Chai_2.find("Chai")) # find the target in given string 7th index

print(Chai_2.find("tea")) # couldn't find, -1 

Chai_5 = "Masala chai chai chai"
print(Chai_5.count("chai")) # counts the target in the given string, 3

Chai_Type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, Chai_Type)) # .format() => insert the values to {} placeholders, "I ordered 2 cups of Masala chai"

Chai_6 = ["Lemon", "Masala", "Ginger"]
print("" .join(Chai_6)) # join the string / list to string, LemonMasalaGinger
print(", " .join(Chai_6)) # Lemon, Masala, Ginger 

Chai_7 = "He said,\"Masala chai is awesome\""
print(Chai_7) # "He said,"Masala chai is awesome"

Chai_8 = r"c:\user\rk"
print(Chai_8) # r is used for raw string, c:\user\rk

Chai_9 = "c:\\user\\rk"
print(Chai_9) # without r, c:\user\rk,
# Chai_9 = "c:\user\rk"
# print(Chai_9) gives error 