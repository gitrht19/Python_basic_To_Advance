# Recommandation a type of pet food based on the pet's species and age (eg. Dog: >2 years - Puppy food, cat>5 years - Senior cat food)
age=int(input("enter the age of animal in years:"))
if(age<2):
    print("use only milk for both")
elif(age>=2 and age<=5):
    print("use the puppy food for the dog, and simple cat food gor cat")
else: 
    print("use the senior category food for both")