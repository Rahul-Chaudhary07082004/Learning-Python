# 3. Grade Calculator :- 
# Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)

score = input("Give the student's score: \n");
score_in_int = int(score);

if score_in_int > 100:
    print("Please verify your score.")
    exit();

if score_in_int >= 90:
    print("Grade A");
elif score_in_int >= 80:
    print("Grade B");
elif score_in_int >= 70:
    print("Grade C");
elif score_in_int >= 60:
    print("Grade D");
else :
    print("Grade F");