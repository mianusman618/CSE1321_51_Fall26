age_str=input("Enter Your Age : ")
age_int=int(age_str)
if age_int >= 18:
    print("You are allowed to vote")
    print("another line in if block")
else:
    print("You are not allowed to vote")
print("rest of the program")