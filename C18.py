country=input("Enter Your Country : ")
if country=="US":
    age_str=input("Enter Your Age : ")
    age_int=int(age_str)
    if age_int >= 18:
        print("You are allowed to vote")
        print("another line in if block")
        if age_int>25:
            print("You dont need guardian")
        else:
            print("You need an adult guardian")
    else:
        print("You are not allowed to vote")
else:
    print("Voting Laws Unknown")
print("rest of the program")