# key and value both are given by you
# List -> everything -> sequential order -> matters
# syntax 
# {"key":"value"}

chai_types = {"masala": "spicy", "ginger": "zesty", "mint": "refreshing"};
print(chai_types["masala"]);

print(chai_types.get("ginger")); 
# this is case sensitive , .get("gingery") -> return nothing and ["masalaa"] -> gives keyword error 

# to change item in dictionary

chai_types["mint"] = "Bold";
print(chai_types);

# can also iterate through whole dictionary

for chai in chai_types:
    print(chai, chai_types[chai]);

for key, value in chai_types.items():
    print(key, value);

# item = key + value

# add item in dictionary
chai_types["earl grey"] = "citrus";
print(chai_types);

# .pop("key") -> Remove item from dictionary and returns the removed value
print(chai_types.pop("masala"));

# .popitem() -> Remove last added item from dictionary
print(chai_types.popitem());

# del -> Delete reference from memory
del chai_types["mint"];

# .clear() -> To remove all items from dictionary
print(chai_types.clear());

keys = ["masala", "Ginger", "Lemon"];
default_value = "Delicious";
new_dict = dict.fromkeys(keys, default_value);
print(new_dict);