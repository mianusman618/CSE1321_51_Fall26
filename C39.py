user_input=int(input("Enter No of Rows : "))
for row in range(user_input):#0,1,2,3,4,5,6,7,8,9
    for sp in range(user_input-(row+1)):
        print(" ",end="")
    for col in range(row+1):
        print("*",end="")
    print()
#    *
#   **
#  ***
# ****