# Choose a mode of transportation bassed on the distance (eg. <3km:walk, 3-15km:bike, >15km:car).
distance = int(input("Enter distance in KM :- "))
if distance < 3:
    transport = "Walk"
elif distance >3 and distance < 15:
    transport = "Bike"
else:
    transport = "Car"

print("Ai recommanded you the way of transport :- ",transport)