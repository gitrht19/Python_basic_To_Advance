# calculate the sum of even numbers up to given number n/

even_numbers = [0,1,2,3,4,5,6,7,8,3,4,5,2]
sum_of_even_numbers = 0
for even_num in even_numbers:
    if even_num%2 == 0:
        sum_of_even_numbers += 1
print("Sum of even numbers is : ",sum_of_even_numbers)