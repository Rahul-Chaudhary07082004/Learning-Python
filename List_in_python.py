# list in python is called array

tea_Types = ["Masala", "Green", "Lemon"];
print(tea_Types);

#1. .append("parameter") = takes one parameter and add it at end of list 
tea_Types.append("Mint");
print(tea_Types);

#2. .pop() = remove last element of list. also return the removed value in terminal
tea_Types.pop();
print(tea_Types);

#3. .remove("tatget") = takes target and remove it from list 
tea_Types.remove("Green");
print(tea_Types);

#4. .insert(index, "value") = takes index and value for that index
tea_Types.insert(2, "oolong tea");
print(tea_Types);

#5. .copy() = to make another memory reference of any list so that main don't get affected
new_Tea_Types = tea_Types.copy()
print(new_Tea_Types);

#6. range() = gives the min and max range
cube_num = [y**3 for y in range(5)]
print(cube_num);