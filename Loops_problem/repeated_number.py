# find the first non-repeated charater
string_char = "rohtikrohitskumarrohit"

for char in string_char:
    if string_char.count(char) == 1:
        print(char)
        break