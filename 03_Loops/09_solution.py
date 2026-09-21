# list uniqueness checker 
# check if all elements in a list are unique. if a duplicate is found, exit the loop and print the duplicate

items = ["apple", "banana", "orange", "apple", "mango"]
is_duplicate = set()

for item in items:
    if item in is_duplicate:
        print("Duplicate found:", item)
        break
    is_duplicate.add(item)
