# 5. Weather Activity Suggestion :- 
# Suggest an activity based on the weather (eg. Sunny- Go for the walk, Rainy- Read a book, Snowy- Build a Snowman).

today_weather = input("Tell me the weather: \n");

if today_weather == "sunny":
    activity = "Go for a walk";
elif today_weather == "rainy":
    activity = "Read a book";
elif today_weather == "snowy":
    activity = "Build a Snowman";

print(activity);