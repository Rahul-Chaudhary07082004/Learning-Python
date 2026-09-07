# 6. Transportation mode selection :- 
# choose a mode of transportation based on the distance (eg. < 3km: walk, 3-15km: Bike, >15km: Car)

distance = int(input("give the distance: \n"));

if distance < 3:
    transport = "walk";
elif distance <= 15:
    transport = "bike";
else :
    transport = "car";

print("your transportation mode is",transport);