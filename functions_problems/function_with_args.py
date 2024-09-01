'''
# write a function that takes variable number of arguments and returns their sum
def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4,4))

'''

def sum_of(*args):
    print(args)
    for i in args:
        print(i * 3)
    return args
print(sum_of(1,2,3))