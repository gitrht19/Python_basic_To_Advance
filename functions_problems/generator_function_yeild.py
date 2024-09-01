# write a generator function that yeilds even numbers up to a specified limit
def generator(limit):
    for i in range(2, limit+1,2):
        yield(i)

for num in generator(10):
    print(num)