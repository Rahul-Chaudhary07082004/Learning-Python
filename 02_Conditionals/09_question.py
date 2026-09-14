# Leap year checker 
# Determine if a year is leap year (leap years are divisible by 4, but not by 100 unless also divisible by 400)

Year = input("Enter the year: \n");
year_in_int = int(Year);

if (year_in_int % 400 == 0) or (year_in_int % 4 == 0 and year_in_int % 100 != 0):
    print(year_in_int, "is a leap year")
else:
    print(year_in_int, "is NOT a leap year")
