# Determine if a year is a leap year.( Leap year is divisible by 4, but not by 100 unless also divisible by 400).
year = 2014

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("This is a Leap Year")
else:
    print("It is not a Leap year")