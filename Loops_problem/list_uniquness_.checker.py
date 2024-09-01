# check if all elements in a list are unique. if a duplicate is found, exit the loop and print the duplicate
items = ["apple", "banana", "orrange", "apple", "mango","mango"]
unique_item = set()
for item in items:
    if item in unique_item:
        print("Unique item is founded :",item)
        
    unique_item.add(item)