def cal_ticket(age,day):
    price=0
    if age<13:
        price=8
    elif age<65:
        price=12
    elif age>=65:
        price=7
    if day=="E" or day=="e":
        price+=3
    return float(price)

tickets=int(input("How many tickets? : "))
total_price=0
for i in range(1,tickets+1):
    age=float(input(f"Ticket {i} Age: "))
    day=input(f"Ticket {i} day: ")
    day.lower()
    if age>0 and (day=="e" or day=="w"):
        price=cal_ticket(age, day)
        print(f"Ticket {i} price: {price:.2f}")
        total_price+=price
    else:
        print("Invalid input")
print("Total price = ",total_price)