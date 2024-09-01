#Q. Classify a person's age group : Chid (<13), Teenager(13-19), Adult(20-59), Senior(60+).

user_age = int(input("Give me a age for discuss about the age classification :- "))

if user_age >0 and user_age < 13:
    print(f"According to the given age by you {user_age} : you are in a Child Category!")

elif user_age > 12 and user_age < 20:
    print(f"According to the given age by you {user_age} : you are in a Teenager Category!")

elif user_age > 19 and user_age <= 59:
    print(f"According to the given age by you {user_age} : you are in a Adult Category!")

elif user_age >=60:
    print(f"According to the given age by you {user_age} : you are in a Senior Category!")
elif user_age < 0:
    print(f"According to the given age by you {user_age} : Paida lene se phle v tm kavi negative nhi ho skte ho! Number correct dalo.")
else:
    print(f"According to the given age by you {user_age} : Somthing went Wrong.")