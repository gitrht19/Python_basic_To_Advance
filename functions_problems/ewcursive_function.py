# create a recursive function to calculate the factorial of a number
def recursion(num):
    if num == 0:
        return 1
    else:
        return num * recursion(num-1)
print(recursion(5))