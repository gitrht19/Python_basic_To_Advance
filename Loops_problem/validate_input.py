# keep asking the user for input until they enter a number between 1 and 10. 

while True:
    num = int(input("Enter a number between 1 to 10 : "))
    if num >=1 and num <=10:
        print(num)
        break
    else:
        print("Try Again")