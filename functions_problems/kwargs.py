# create a function that accepts any number of keyword arguments and prints them in the format key:value.

def print_function(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_function(nmae="rohit",surename = "sah")