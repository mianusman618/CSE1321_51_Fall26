def cal_price(price,qty):
    return price*qty
def apply_discount(total,mem):
    if mem=="GOLD":
        return (10/100)*total
    elif mem=="SILVER":
        return (5/100)*total
    else:
        return 0
#print(apply_discount(110,"GOLD"))
while True:
    cust_choice=input("Another Customer (Y/N) : ")
    cust_choice=cust_choice.upper()
    if cust_choice=="N":
        break
    elif cust_choice=="Y":
        sub_total=0
        items=0
        while True:
            price=int(input("Item price (0 to finish): "))
            if price==0:
                break
            qty=int(input("Quantity: "))
            if price<0 or qty<0:
                print("Price or QTy can not be negative")
            items+=1
            sub_total+=cal_price(price,qty)
        print("Subtotal =",sub_total)
        print("items purchased = ",items)

    else:
        print("Wrong Input")
