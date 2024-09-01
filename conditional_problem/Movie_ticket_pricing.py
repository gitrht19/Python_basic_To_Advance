# QMovie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednessday.

age = int(input("Enter your age :- "))
day = input("What is it today :- ")

price = 12 if age >=18 else 8
if day == "wednessday":
    price -= 2
print("Ticket price is for you $",price)