# Check if a password is "Week", "Medium",or "Strong". Criteria: <6 Chars(Week), 6-10 chars(Medium),>10 Char Strong
Password = "Rcdkj83k"
length = len(Password)
if length < 6:
    Criteria = "Week"
elif length > 6 and length < 10:
    Criteria = "Medium"
else:
    Criteria = "Strong"
print(Criteria)