def suggest_clothing(temp):
    if temp> 70:
        print("more than 70")
    elif temp >50 and temp<70:
        print("between 50 and 70")
    elif temp<50:
        print("less than 50")
No_readings=int(input("How many readings? : "))
for i in range(1,No_readings+1):
    temp=int(input(f"Temperature {i} (F): "))
    suggest_clothing(temp)