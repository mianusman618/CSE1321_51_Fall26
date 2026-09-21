user_input=int(input("Enter a number between 1 & 10 : "))
while user_input < 1 or user_input > 10:
    user_input = int(input("Enter a number between 1 & 10 : "))
print("Number accepted")