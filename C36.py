num=int(input("Enter a number : "))
count=0
while num>0:
    num=num//10
    print(num)
    count+=1
print("Num of digits = ",count)