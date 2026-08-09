# Tuple is a collection of values that is ordered and cannot be changed after it is created. Think tuple as a read-only list

# creating a tuple 
person = ("Rahul", 23, "India");
print(person);

# Accessing tuples elements 
print(person[0]);
print(person[1]);
print(person[2]);
print(person[-1]);

# Tuple unpacking
(name, age, country) = person;
print(name);
print(age);
print(country);

# Tuple can contain another tuple and can be accessed by indexing 
student = ("Goldie", (89, 76, 70));
print(student[0]);
print(student[1]);
print(student[1][0]);
print(student[1][1]);
print(student[1][2]);

#  Single element tuple , comma is important for the single element tuple
x = (10,);  
y = (10);
print(type(x));
print(type(y));

#  Methods in tuple 
#  count()

numbers = (1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,);
print(numbers.count(1));
print(numbers.count(2));
print(numbers.count(3));
print(numbers.count(4));
print(numbers.count(5));

#  Finding index of a value 
numbers_1 = (89, 90, 95);
print(numbers_1.index(90));