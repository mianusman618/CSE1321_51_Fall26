user_input=int(input("Enter a num to see its factorial : "))
fact=1
while user_input>0:
    fact=fact*user_input
    user_input-=1
print("Factorial is = ",fact)