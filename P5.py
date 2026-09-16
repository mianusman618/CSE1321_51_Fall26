user_input=int(input("Enter a number : "))

if user_input%3==0 and user_input%5==0:
    print("Divisible by both 3 and 5")
elif user_input % 5 == 0:
    print("Divisible by 5")
elif user_input%3==0:
    print("Divisible by 3")