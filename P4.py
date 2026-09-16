Num1=int(input("Enter First Number : "))
Num2=int(input("Enter Second Number : "))
Num3=int(input("Enter Third Number : "))
if Num1 > Num2 and Num1 > Num3:
    print("Num1 is largest")
elif Num2 > Num1:
    if Num2 > Num3:
        print("Num2 is largest")
elif Num3 > Num2 and Num3 > Num1:
    print("Num3 is largest")
else:
    print("All numbers are equal")