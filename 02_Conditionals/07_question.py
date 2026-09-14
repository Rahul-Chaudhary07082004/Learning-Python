# 7. Coffee customization :- 
# customize a coffee order: "small", "medium", or "large" with an option for "extra shot" of espresso.

order_size = input("Sir! Please tell me the order size \n");
extra_shot = True;

if extra_shot:
    coffee = order_size + " coffee with an extra shot."
else:
    coffee = order_size + " coffee."

print("order " + coffee);