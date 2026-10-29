file = open('test.py', 'w') # in write mode if file doesn't exist then it will create the file 

try:
    file.write('chai aur code') # if you want to write something in the created file
finally:
    file.close() # this closes the file 

# new syntax for same work 
# this will do exactly the same work as the above code do 
with open('test.py', 'w') as file:
    file.write('chai aur code') 