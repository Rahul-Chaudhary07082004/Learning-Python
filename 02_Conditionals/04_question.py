# 4. Fruit ripeness checker :- 
# determine if a fruit is ripe, overripe or unripe based on its colour. (eg. Banana:Green- unripe, Yellow- ripe, Brown- overripe) 

fruit = input("Tell me the fruit name: \n");
if fruit != "Banana":
    print("we dont have information yet")
    exit();
colour = input("What's the colour of the fruit ? \n");

if fruit == "Banana":
    if colour == "green":
        print("Fruit is unripe")
    elif colour == "brown":
        print("Fruit is overripe")
    elif colour == "yellow":
        print("Fruit is ripe")
