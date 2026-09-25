user_input=int(input("Enter a number : "))
print("Multiplication Table of ",user_input)
for i in range(1,11):
    print(f"{user_input} * {i} = {user_input*i}")
