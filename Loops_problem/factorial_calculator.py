# compute the factorial of a number using a while loop  

fact_num = int(input("Enter number for calculate a number of factorial :- "))
factorial = 1

while fact_num > 0:
    factorial *= fact_num
    fact_num -= 1
print(factorial)